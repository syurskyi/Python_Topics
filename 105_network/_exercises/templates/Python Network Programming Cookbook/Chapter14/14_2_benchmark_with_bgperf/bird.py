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

c_ BIRD(Container):

    CONTAINER_NAME _ N..
    GUEST_DIR _ '/root/config'

    ___ -  host_dir, conf, image_'bgperf/bird'):
        super(BIRD, self).- (CONTAINER_NAME, image, host_dir, GUEST_DIR, conf)

    @classmethod
    ___ build_image(cls, force_False, tag_'bgperf/bird', checkout_'HEAD', nocache_False):
        cls.dockerfile _ '''
FROM ubuntu:latest
WORKDIR /root
RUN apt-get update && apt-get install -qy git autoconf libtool gawk make \
flex bison libncurses-dev libreadline6-dev
RUN apt-get install -qy flex
RUN git clone https://gitlab.labs.nic.cz/labs/bird.git bird
RUN cd bird && git checkout {0} && autoreconf -i && ./configure && make && make install
'''.f..(checkout)
        super(BIRD, cls).build_image(force, tag, nocache)


c_ BIRDTarget(BIRD, Target):

    CONTAINER_NAME _ 'bgperf_bird_target'
    CONFIG_FILE_NAME _ 'bird.conf'

    ___ write_config scenario_global_conf):
        config _ '''router id {0};
listen bgp port 179;
protocol device {{ }}
protocol direct {{ disabled; }}
protocol kernel {{ disabled; }}
table master{1};
'''.f..(conf['router-id'], ' sorted' __ conf['single-table'] ____ '')

        ___ gen_filter_assignment(n):
            __ 'filter' __ n:
                c _ []
                __ 'in' no. __ n['filter'] or le.(n['filter']['in']) __ 0:
                    c.ap..('import all;')
                ____
                    c.ap..('import where {0};'.f..( '&&'.j..(x + '()' ___ x __ n['filter']['in'])))

                __ 'out' no. __ n['filter'] or le.(n['filter']['out']) __ 0:
                    c.ap..('export all;')
                ____
                    c.ap..('export where {0};'.f..( '&&'.j..(x + '()' ___ x __ n['filter']['out'])))

                r_ '\n'.j..(c)
            r_ '''import all;
export all;
'''

        ___ gen_neighbor_config(n):
            r_ ('''table table_{0};
protocol pipe pipe_{0} {{
    table master;
    mode transparent;
    peer table table_{0};
{1}
}}'''.f..(n['as'], gen_filter_assignment(n)) __ no. conf['single-table'] ____ '') + '''protocol bgp bgp_{0} {{
    local as {1};
    neighbor {2} as {0};
    {3};
    import all;
    export all;
    rs client;
}}
'''.f..(n['as'], conf['as'], n['local-address'], 'secondary' __ conf['single-table'] ____ 'table table_{0}'.f..(n['as']))
            r_ n1 + n2

        ___ gen_prefix_filter(name, match):
            r_ '''function {0}()
prefix set prefixes;
{{
prefixes = [
{1}
];
if net ~ prefixes then return false;
return true;
}}
'''.f..(name, ',\n'.j..(match['value']))

        ___ gen_aspath_filter(name, match):
            c _ '''function {0}()
{{
'''.f..(name)
            c +_ '\n'.j..('if (bgp_path ~ [= * {0} * =]) then return false;'.f..(v) ___ v __ match['value'])
            c +_ '''
return true;
}
'''
            r_ c

        ___ gen_community_filter(name, match):
            c _ '''function {0}()
{{
'''.f..(name)
            c +_ '\n'.j..('if ({0}, {1}) ~ bgp_community then return false;'.f..(*v.s..(':')) ___ v __ match['value'])
            c +_ '''
return true;
}
'''
            r_ c

        ___ gen_ext_community_filter(name, match):
            c _ '''function {0}()
{{
'''.f..(name)
            c +_ '\n'.j..('if ({0}, {1}, {2}) ~ bgp_ext_community then return false;'.f..(*v.s..(':')) ___ v __ match['value'])
            c +_ '''
return true;
}
'''
            r_ c



        ___ gen_filter(name, match):
            c _ ['function {0}()'.f..(name), '{']
            ___ typ, name __ match:
                c.ap..(' if ! {0}() then return false;'.f..(name))
            c.ap..('return true;')
            c.ap..('}')
            r_ '\n'.j..(c) + '\n'

        with o..('{0}/{1}'.f..(host_dir, CONFIG_FILE_NAME), 'w') __ f:
            f.w..(config)

            __ 'policy' __ scenario_global_conf:
               ___ k, v __ list(scenario_global_conf['policy'].items()):
                    match_info _ []
                    ___ i, match __ enumerate(v['match']):
                        n _ '{0}_match_{1}'.f..(k, i)
                        __ match['type'] __ 'prefix':
                            f.w..(gen_prefix_filter(n, match))
                        ____ match['type'] __ 'as-path':
                            f.w..(gen_aspath_filter(n, match))
                        ____ match['type'] __ 'community':
                            f.w..(gen_community_filter(n, match))
                        ____ match['type'] __ 'ext-community':
                            f.w..(gen_ext_community_filter(n, match))
                        match_info.ap..((match['type'], n))
                    f.w..(gen_filter(k, match_info))

            ___ n __ sorted(list(flatten(list(t.get('neighbors', {}).values()) ___ t __ scenario_global_conf['testers'])) + [scenario_global_conf['monitor']], key_lambda n: n['as']):
                f.w..(gen_neighbor_config(n))
            f.f..

    ___ get_startup_cmd
        r_ '\n'.j..(
            ['#!/bin/bash',
             'ulimit -n 65536',
             'bird -c {guest_dir}/{config_file_name}']
        ).f..(
            guest_dir_self.guest_dir,
            config_file_name_self.CONFIG_FILE_NAME)
