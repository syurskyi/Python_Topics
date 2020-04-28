# Copyright (C) 2017 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

____ tester ______ Tester
____ gobgp ______ GoBGP
____ exabgp ______ ExaBGP_MRTParse
______ __
______ yaml
____  settings ______ dckr
______ shutil


c_ MRTTester(o..):

    ___ get_mrt_file conf, name):
        # conf: tester or neighbor configuration
        __ 'mrt-file' __ conf:
            mrt_file_path _ __.pa__.expanduser(conf['mrt-file'])

            guest_mrt_file_path _ '{guest_dir}/{filename}'.format(
                guest_dir_self.guest_dir,
                filename_name + '.mrt'
            )
            host_mrt_file_path _ '{host_dir}/{filename}'.format(
                host_dir_self.host_dir,
                filename_name + '.mrt'
            )
            __ no. __.pa__.isfile(host_mrt_file_path):
                shutil.copyfile(mrt_file_path, host_mrt_file_path)
            r_ guest_mrt_file_path

c_ ExaBGPMrtTester(Tester, ExaBGP_MRTParse, MRTTester):

    CONTAINER_NAME_PREFIX _ 'bgperf_exabgp_mrttester_'

    ___ -  name, host_dir, conf, image_'bgperf/exabgp_mrtparse'):
        super(ExaBGPMrtTester, self).- (name, host_dir, conf, image)

    ___ configure_neighbors target_conf):
        tester_mrt_guest_file_path _ get_mrt_file(conf, name)

        neighbors _ list(conf.get('neighbors', {}).values())

        ___ neighbor __ neighbors:
            config _ '''neighbor {0} {{
    peer-as {1};
    router-id {2};
    local-address {3};
    local-as {4};
    api {{
        processes [ inject_mrt ];
    }}
}}'''.format(target_conf['local-address'], target_conf['as'],
             neighbor['router-id'], neighbor['local-address'],
             neighbor['as'])

            mrt_guest_file_path _ get_mrt_file(neighbor,
                                                    neighbor['router-id'])
            __ no. mrt_guest_file_path:
                mrt_guest_file_path _ tester_mrt_guest_file_path

            cmd _ ['/usr/bin/python', '/root/mrtparse/examples/mrt2exabgp.py']
            cmd +_ ['-r {router_id}',
                    '-l {local_as}',
                    '-p {peer_as}',
                    '-L {local_addr}',
                    '-n {peer_addr}',
                    '-G',
                    '{mrt_file_path}']

            config +_ '\n'
            config +_ 'process inject_mrt {\n'
            config +_ '    run {cmd};\n'.format(
                cmd_' '.j..(cmd).format(
                    router_id _ neighbor['router-id'],
                    local_as _ neighbor['as'],
                    peer_as _ target_conf['as'],
                    local_addr _ neighbor['local-address'],
                    peer_addr _ target_conf['local-address'],
                    mrt_file_path _ mrt_guest_file_path
                )
            )
            config +_ '    encoder text;\n'
            config +_ '}\n'

            with open('{0}/{1}.conf'.format(host_dir, neighbor['router-id']), 'w') __ f:
                f.w..(config)

    ___ get_startup_cmd
        peers _ list(conf.get('neighbors', {}).values())

        startup _ ['#!/bin/bash',
                   'ulimit -n 65536']

        cmd _ ['env',
               'exabgp.daemon.daemonize=true',
               'exabgp.daemon.user=root']

        # Higher performances:
        #   exabgp -d config1 config2
        # https://github.com/Exa-Networks/exabgp/wiki/High-Performance
        # WARNING: can not log to files when running multiple configuration
        __ conf.get('high-perf', F..) is T..:
            cmd +_ ['exabgp -d {} >/dev/null 2>&1 &'.format(
                       ' '.j..([
                           '{}/{}.conf'.format(guest_dir, p['router-id']) ___ p __ peers
                       ])
                   )]
            startup +_ [' '.j..(cmd)]
        ____
            ___ p __ peers:
                startup +_ [' '.j..(
                    cmd + [
                        'exabgp.log.destination={0}/{1}'.format(
                            guest_dir, p['router-id']),
                        'exabgp {}/{}.conf'.format(
                            guest_dir, p['router-id']),
                        '&'
                    ])
                ]

        r_ '\n'.j..(startup)


c_ GoBGPMRTTester(Tester, GoBGP, MRTTester):

    CONTAINER_NAME_PREFIX _ 'bgperf_gobgp_mrttester_'

    ___ -  name, host_dir, conf, image_'bgperf/gobgp'):
        super(GoBGPMRTTester, self).- (name, host_dir, conf, image)

    ___ configure_neighbors target_conf):
        conf _ list(conf.get('neighbors', {}).values())[0]

        config _ {
            'global': {
                'config': {
                    'as': conf['as'],
                    'router-id': conf['router-id'],
                }
            },
            'neighbors': [
                {
                    'config': {
                        'neighbor-address': target_conf['local-address'],
                        'peer-as': target_conf['as']
                    }
                }
            ]
        }

        with open('{0}/{1}.conf'.format(host_dir, name), 'w') __ f:
            f.w..(yaml.dump(config, default_flow_style_False))
            config_name _ '{0}.conf'.format(name)

    ___ get_startup_cmd
        conf _ list(conf.get('neighbors', {}).values())[0]

        mrtfile _ get_mrt_file(conf, conf['router-id'])
        __ no. mrtfile:
            mrtfile _ get_mrt_file(conf, name)

        startup _ '''#!/bin/bash
ulimit -n 65536
gobgpd -t yaml -f {1}/{2} -l {3} > {1}/gobgpd.log 2>&1 &
'''.format(conf['local-address'], guest_dir, config_name, 'info')

        cmd _ ['gobgp', 'mrt']
        __ conf.get('only-best', F..):
            cmd.ap..('--only-best')
        cmd +_ ['inject', 'global', mrtfile]
        __ 'count' __ conf:
            cmd.ap..(st..(conf['count']))
        __ 'skip' __ conf:
            cmd.ap..(st..(conf['skip']))

        startup +_ '\n' + ' '.j..(cmd)

        startup +_ '\n' + 'pkill -SIGHUP gobgpd'
        r_ startup
