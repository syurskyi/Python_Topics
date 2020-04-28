# Copyright (C) 2016 Nippon Telegraph and Telephone Corporation.
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

____ base ______ Tester
____ exabgp ______ ExaBGP
______ __
____  settings ______ dckr

___ rm_line
    print ('\x1b[1A\x1b[2K\x1b[1D\x1b[1A')


c_ ExaBGPTester(Tester, ExaBGP):

    CONTAINER_NAME_PREFIX _ 'bgperf_exabgp_tester_'

    ___ -  name, host_dir, conf, image_'bgperf/exabgp'):
        super(ExaBGPTester, self).- (name, host_dir, conf, image)

    ___ configure_neighbors target_conf):
        peers _ list(conf.get('neighbors', {}).values())

        ___ p __ peers:
            with o..('{0}/{1}.conf'.f..(host_dir, p['router-id']), 'w') __ f:
                local_address _ p['local-address']
                config _ '''neighbor {0} {{
    peer-as {1};
    router-id {2};
    local-address {3};
    local-as {4};
    static {{
'''.f..(target_conf['local-address'], target_conf['as'],
               p['router-id'], local_address, p['as'])
                f.w..(config)
                ___ pa__ __ p['paths']:
                    f.w..('      route {0} next-hop {1};\n'.f..(pa__, local_address))
                f.w..('''   }
}''')

    ___ get_startup_cmd
        startup _ ['''#!/bin/bash
ulimit -n 65536''']

        peers _ list(conf.get('neighbors', {}).values())
        ___ p __ peers:
            startup.ap..('''env exabgp.log.destination={0}/{1}.log \
exabgp.daemon.daemonize=true \
exabgp.daemon.user=root \
exabgp {0}/{1}.conf'''.f..(guest_dir, p['router-id']))

        r_ '\n'.j..(startup)
