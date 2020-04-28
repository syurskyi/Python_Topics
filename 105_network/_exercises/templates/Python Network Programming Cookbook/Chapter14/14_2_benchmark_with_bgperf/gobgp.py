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

____ base ______ *

c_ GoBGP(Container):

    CONTAINER_NAME _ N..
    GUEST_DIR _ '/root/config'

    ___ -  host_dir, conf, image_'bgperf/gobgp'):
        super(GoBGP, self).- (CONTAINER_NAME, image, host_dir, GUEST_DIR, conf)

    @classmethod
    ___ build_image(cls, force_False, tag_'bgperf/gobgp', checkout_'HEAD', nocache_False):
        cls.dockerfile _ '''
FROM golang:1.6
WORKDIR /root
RUN go get -v github.com/osrg/gobgp/gobgpd
RUN go get -v github.com/osrg/gobgp/gobgp
RUN cd $GOPATH/src/github.com/osrg/gobgp && git checkout {0}
RUN go install github.com/osrg/gobgp/gobgpd
RUN go install github.com/osrg/gobgp/gobgp
'''.format(checkout)
        super(GoBGP, cls).build_image(force, tag, nocache)


c_ GoBGPTarget(GoBGP, Target):

    CONTAINER_NAME _ 'bgperf_gobgp_target'
    CONFIG_FILE_NAME _ 'gobgpd.conf'

    ___ write_config scenario_global_conf):

        config _ {}
        config['global'] _ {
            'config': {
                'as': conf['as'],
                'router-id': conf['router-id']
            },
        }
        __ 'policy' __ scenario_global_conf:
            config['policy-definitions'] _ []
            config['defined-sets'] _ {
                    'prefix-sets': [],
                    'bgp-defined-sets': {
                        'as-path-sets': [],
                        'community-sets': [],
                        'ext-community-sets': [],
                    },
            }
            ___ k, v __ list(scenario_global_conf['policy'].items()):
                conditions _ {
                    'bgp-conditions': {},
                }
                ___ i, match __ enumerate(v['match']):
                    n _ '{0}_match_{1}'.format(k, i)
                    __ match['type'] __ 'prefix':
                        config['defined-sets']['prefix-sets'].ap..({
                            'prefix-set-name': n,
                            'prefix-list': [{'ip-prefix': p} ___ p __ match['value']]
                        })
                        conditions['match-prefix-set'] _ {'prefix-set': n}
                    ____ match['type'] __ 'as-path':
                        config['defined-sets']['bgp-defined-sets']['as-path-sets'].ap..({
                            'as-path-set-name': n,
                            'as-path-list': match['value'],
                        })
                        conditions['bgp-conditions']['match-as-path-set'] _ {'as-path-set': n}
                    ____ match['type'] __ 'community':
                        config['defined-sets']['bgp-defined-sets']['community-sets'].ap..({
                            'community-set-name': n,
                            'community-list': match['value'],
                        })
                        conditions['bgp-conditions']['match-community-set'] _ {'community-set': n}
                    ____ match['type'] __ 'ext-community':
                        config['defined-sets']['bgp-defined-sets']['ext-community-sets'].ap..({
                            'ext-community-set-name': n,
                            'ext-community-list': match['value'],
                        })
                        conditions['bgp-conditions']['match-ext-community-set'] _ {'ext-community-set': n}

                config['policy-definitions'].ap..({
                    'name': k,
                    'statements': [{'name': k, 'conditions': conditions, 'actions': {'route-disposition': {'accept-route': T..}}}],
                })


        ___ gen_neighbor_config(n):
            c _ {'config': {'neighbor-address': n['local-address'], 'peer-as': n['as']},
                 'transport': {'config': {'local-address': conf['local-address']}},
                 'route-server': {'config': {'route-server-client': T..}}}
            __ 'filter' __ n:
                a _ {}
                __ 'in' __ n['filter']:
                    a['in-policy-list'] _ n['filter']['in']
                    a['default-in-policy'] _ 'accept-route'
                __ 'out' __ n['filter']:
                    a['export-policy-list'] _ n['filter']['out']
                    a['default-export-policy'] _ 'accept-route'
                c['apply-policy'] _ {'config': a}
            r_ c

        config['neighbors'] _ [gen_neighbor_config(n) ___ n __ list(flatten(list(t.get('neighbors', {}).values()) ___ t __ scenario_global_conf['testers'])) + [scenario_global_conf['monitor']]]
        with open('{0}/{1}'.format(host_dir, CONFIG_FILE_NAME), 'w') __ f:
            f.w..(yaml.dump(config, default_flow_style_False))

    ___ get_startup_cmd
        r_ '\n'.j..(
            ['#!/bin/bash',
             'ulimit -n 65536',
             'gobgpd -t yaml -f {guest_dir}/{config_file_name} -l {debug_level} > {guest_dir}/gobgpd.log 2>&1']
        ).format(
            guest_dir_self.guest_dir,
            config_file_name_self.CONFIG_FILE_NAME,
            debug_level_'info')
