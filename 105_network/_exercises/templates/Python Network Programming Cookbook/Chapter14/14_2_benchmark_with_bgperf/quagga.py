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

c_ Quagga(Container):

    CONTAINER_NAME _ N..
    GUEST_DIR _ '/root/config'

    ___ -  host_dir, conf, image_'bgperf/quagga'):
        super(Quagga, self).- (CONTAINER_NAME, image, host_dir, GUEST_DIR, conf)

    @classmethod
    ___ build_image(cls, force_False, tag_'bgperf/quagga', checkout_'HEAD', nocache_False):
        cls.dockerfile _ '''
FROM ubuntu:latest
WORKDIR /root
RUN useradd -M quagga
RUN mkdir /var/log/quagga && chown quagga:quagga /var/log/quagga
RUN mkdir /var/run/quagga && chown quagga:quagga /var/run/quagga
RUN apt-get update && apt-get install -qy git autoconf libtool gawk make telnet libreadline6-dev
RUN git clone git://git.sv.gnu.org/quagga.git quagga
RUN cd quagga && git checkout {0} && ./bootstrap.sh && \
./configure --disable-doc --localstatedir=/var/run/quagga && make && make install
RUN ldconfig
'''.f..(checkout)
        super(Quagga, cls).build_image(force, tag, nocache)


c_ QuaggaTarget(Quagga, Target):

    CONTAINER_NAME _ 'bgperf_quagga_target'
    CONFIG_FILE_NAME _ 'bgpd.conf'

    ___ write_config scenario_global_conf):

        config _ """hostname bgpd
password zebra
router bgp {0}
bgp router-id {1}
""".f..(conf['as'], conf['router-id'])

        ___ gen_neighbor_config(n):
            local_addr _ n['local-address']
            c _ """neighbor {0} remote-as {1}
neighbor {0} advertisement-interval 1
neighbor {0} route-server-client
neighbor {0} timers 30 90
""".f..(local_addr, n['as'])
            __ 'filter' __ n:
                ___ p __ (n['filter']['in'] __ 'in' __ n['filter'] ____ []):
                    c +_ 'neighbor {0} route-map {1} export\n'.f..(local_addr, p)
            r_ c

        w__ o..('{0}/{1}'.f..(host_dir, CONFIG_FILE_NAME), 'w') __ f:
            f.w..(config)
            ___ n __ list(flatten(list(t.get('neighbors', {}).values()) ___ t __ scenario_global_conf['testers'])) + [scenario_global_conf['monitor']]:
                f.w..(gen_neighbor_config(n))

            __ 'policy' __ scenario_global_conf:
                seq _ 10
                ___ k, v __ list(scenario_global_conf['policy'].items()):
                    match_info _ []
                    ___ i, match __ enumerate(v['match']):
                        n _ '{0}_match_{1}'.f..(k, i)
                        __ match['type'] __ 'prefix':
                            f.w..(''.j..('ip prefix-list {0} deny {1}\n'.f..(n, p) ___ p __ match['value']))
                            f.w..('ip prefix-list {0} permit any\n'.f..(n))
                        ____ match['type'] __ 'as-path':
                            f.w..(''.j..('ip as-path access-list {0} deny _{1}_\n'.f..(n, p) ___ p __ match['value']))
                            f.w..('ip as-path access-list {0} permit .*\n'.f..(n))
                        ____ match['type'] __ 'community':
                            f.w..(''.j..('ip community-list standard {0} permit {1}\n'.f..(n, p) ___ p __ match['value']))
                            f.w..('ip community-list standard {0} permit\n'.f..(n))
                        ____ match['type'] __ 'ext-community':
                            f.w..(''.j..('ip extcommunity-list standard {0} permit {1} {2}\n'.f..(n, *p.s..(':', 1)) ___ p __ match['value']))
                            f.w..('ip extcommunity-list standard {0} permit\n'.f..(n))

                        match_info.ap..((match['type'], n))

                    f.w..('route-map {0} permit {1}\n'.f..(k, seq))
                    ___ info __ match_info:
                        __ info[0] __ 'prefix':
                            f.w..('match ip address prefix-list {0}\n'.f..(info[1]))
                        ____ info[0] __ 'as-path':
                            f.w..('match as-path {0}\n'.f..(info[1]))
                        ____ info[0] __ 'community':
                            f.w..('match community {0}\n'.f..(info[1]))
                        ____ info[0] __ 'ext-community':
                            f.w..('match extcommunity {0}\n'.f..(info[1]))

                    seq +_ 10

    ___ get_startup_cmd
        r_ '\n'.j..(
            ['#!/bin/bash',
             'ulimit -n 65536',
             'bgpd -u root -f {guest_dir}/{config_file_name}']
        ).f..(
            guest_dir_self.guest_dir,
            config_file_name_self.CONFIG_FILE_NAME)
