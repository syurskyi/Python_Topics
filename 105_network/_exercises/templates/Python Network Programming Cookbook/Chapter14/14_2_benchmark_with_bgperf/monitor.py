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

____ gobgp ______ GoBGP
______ __
____  settings ______ dckr
______ yaml
______ json
____ th.. ______ T..
______ t__

c_ Monitor(GoBGP):

    CONTAINER_NAME _ 'bgperf_monitor'

    ___ run conf, dckr_net_name_''):
        ctn _ super(GoBGP, self).run(dckr_net_name)
        config _ {}
        config['global'] _ {
            'config': {
                'as': conf['monitor']['as'],
                'router-id': conf['monitor']['router-id'],
            },
        }
        config ['neighbors'] _ [{'config': {'neighbor-address': conf['target']['local-address'],
                                            'peer-as': conf['target']['as']},
                                 'transport': {'config': {'local-address': conf['monitor']['local-address']}},
                                 'timers': {'config': {'connect-retry': 10}}}]
        with o..('{0}/{1}'.f..(host_dir, 'gobgpd.conf'), 'w') __ f:
            f.w..(yaml.dump(config))
        config_name _ 'gobgpd.conf'
        startup _ '''#!/bin/bash
ulimit -n 65536
gobgpd -t yaml -f {1}/{2} -l {3} > {1}/gobgpd.log 2>&1
'''.f..(conf['monitor']['local-address'], guest_dir, config_name, 'info')
        filename _ '{0}/start.sh'.f..(host_dir)
        with o..(filename, 'w') __ f:
            f.w..(startup)
        __.chmod(filename, 0o777)
        i _ dckr.exec_create(container_self.name, cmd_'{0}/start.sh'.f..(guest_dir))
        dckr.exec_start(i['Id'], detach_True, ?_True)
        config _ conf
        r_ ctn

    ___ wait_established neighbor):
        w__ T..:
            neigh _ json.loads(local('gobgp neighbor {0} -j'.f..(neighbor)).d..('utf-8'))
            __ neigh['state']['session-state'] __ 'established':
                r_
            t__.sleep(1)

    ___ stats queue):
        ___ stats
            cps _ config['monitor']['check-points'] __ 'check-points' __ config['monitor'] ____ []
            w__ T..:
                info _ json.loads(local('gobgp neighbor -j').d..('utf-8'))[0]
                info['who'] _ name
                state _ info['state']
                __ 'adj-table' __ state and 'accepted' __ state['adj-table'] and le.(cps) > 0 and int(cps[0]) __ int(state['adj-table']['accepted']):
                    cps.pop(0)
                    info['checked'] _ T..
                ____
                    info['checked'] _ F..
                queue.put(info)
                t__.sleep(1)

        t _ T..(target_stats)
        t.daemon _ T..
        t.s..
