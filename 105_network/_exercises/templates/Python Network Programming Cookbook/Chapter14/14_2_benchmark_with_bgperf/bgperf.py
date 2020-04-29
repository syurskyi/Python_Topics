#!/usr/bin/env python
#
# Copyright (C) 2015, 2016 Nippon Telegraph and Telephone Corporation.
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

______ __
______ ___
______ yaml
______ t__
______ shutil
______ netaddr
______ d_t_
____ ? ______ AP.., REMAINDER
____ itertools ______ chain, islice
____ ?.exceptions ______ ConnectionError
____ pyroute2 ______ IPRoute
____ ? ______ AF_INET
____ nsenter ______ Namespace
____ base ______ *
____ exabgp ______ ExaBGP, ExaBGP_MRTParse
____ gobgp ______ GoBGP, GoBGPTarget
____ bird ______ BIRD, BIRDTarget
____ quagga ______ Quagga, QuaggaTarget
____ tester ______ ExaBGPTester
____ mrt_tester ______ GoBGPMRTTester, ExaBGPMrtTester
____ monitor ______ Monitor
____ settings ______ dckr

____ queue ______ Queue
# Comment out the above line and uncomment the below for Python2.
#from Queue import Queue

____ mako.template ______ Template
____ packaging ______ version
____ docker.types ______ IPAMConfig, IPAMPool

___ gen_mako_macro
    r_ '''<
    import netaddr
    from itertools import islice

    it = netaddr.iter_iprange('100.0.0.0','160.0.0.0')

    def gen_paths(num):
        return list('{0}/32'.format(ip) for ip in islice(it, num))
>
'''

___ rm_line
    print ('\x1b[1A\x1b[2K\x1b[1D\x1b[1A')


___ gc_thresh3
    gc_thresh3 _ '/proc/sys/net/ipv4/neigh/default/gc_thresh3'
    w__ o..(gc_thresh3) __ f:
        r_ int(f.read().strip())


___ doctor(args):
    ver _ dckr.version()['Version']
    __ ver.endswith('-ce'):
        curr_version _ version.parse(ver.replace('-ce', ''))
    ____
        curr_version _ version.parse(ver)
    min_version _ version.parse('1.9.0')
    ok _ curr_version >_ min_version
    print ('docker version ... {1} ({0})'.f..(ver, 'ok' __ ok ____ 'update to {} at least'.f..(min_version)))

    print ('bgperf image',)
    __ img_exists('bgperf/exabgp'):
        print ('... ok')
    ____
        print ('... not found. run `bgperf prepare`')

    ___ name __ ['gobgp', 'bird', 'quagga']:
        print ('{0} image'.f..(name),)
        __ img_exists('bgperf/{0}'.f..(name)):
            print ('... ok')
        ____
            print ('... not found. if you want to bench {0}, run `bgperf prepare`'.f..(name))

    print ('/proc/sys/net/ipv4/neigh/default/gc_thresh3 ... {0}'.f..(gc_thresh3()))


___ prepare(args):
    ExaBGP.build_image(args.force, nocache_args.no_cache)
    ExaBGP_MRTParse.build_image(args.force, nocache_args.no_cache)
    GoBGP.build_image(args.force, nocache_args.no_cache)
    Quagga.build_image(args.force, checkout_'quagga-1.0.20160309', nocache_args.no_cache)
    BIRD.build_image(args.force, nocache_args.no_cache)


___ update(args):
    __ args.image __ 'all' or args.image __ 'exabgp':
        ExaBGP.build_image(T.., checkout_args.checkout, nocache_args.no_cache)
    __ args.image __ 'all' or args.image __ 'exabgp_mrtparse':
        ExaBGP_MRTParse.build_image(T.., checkout_args.checkout, nocache_args.no_cache)
    __ args.image __ 'all' or args.image __ 'gobgp':
        GoBGP.build_image(T.., checkout_args.checkout, nocache_args.no_cache)
    __ args.image __ 'all' or args.image __ 'quagga':
        Quagga.build_image(T.., checkout_args.checkout, nocache_args.no_cache)
    __ args.image __ 'all' or args.image __ 'bird':
        BIRD.build_image(T.., checkout_args.checkout, nocache_args.no_cache)


___ bench(args):
    config_dir _ '{0}/{1}'.f..(args.dir, args.bench_name)
    dckr_net_name _ args.docker_network_name or args.bench_name + '-br'

    ___ target_class __ [BIRDTarget, GoBGPTarget, QuaggaTarget]:
        __ ctn_exists(target_class.CONTAINER_NAME):
            print ('removing target container', target_class.CONTAINER_NAME)
            dckr.remove_container(target_class.CONTAINER_NAME, force_True)

    __ no. args.repeat:
        __ ctn_exists(Monitor.CONTAINER_NAME):
            print ('removing monitor container', Monitor.CONTAINER_NAME)
            dckr.remove_container(Monitor.CONTAINER_NAME, force_True)

        ___ ctn_name __ get_ctn_names
            __ ctn_name.startswith(ExaBGPTester.CONTAINER_NAME_PREFIX) or \
                ctn_name.startswith(ExaBGPMrtTester.CONTAINER_NAME_PREFIX) or \
                ctn_name.startswith(GoBGPMRTTester.CONTAINER_NAME_PREFIX):
                print ('removing tester container', ctn_name)
                dckr.remove_container(ctn_name, force_True)

        __ __.pa__.e..(config_dir):
            shutil.rmtree(config_dir)

    __ args.file:
        w__ o..(args.file) __ f:
            conf _ yaml.load(Template(f.read()).render())
    ____
        conf _ gen_conf(args)
        __ no. __.pa__.e..(config_dir):
            __.makedirs(config_dir)
        w__ o..('{0}/scenario.yaml'.f..(config_dir), 'w') __ f:
            f.w..(conf)
        conf _ yaml.load(Template(conf).render())

    bridge_found _ F..
    ___ network __ dckr.networks(names_[dckr_net_name]):
        __ network['Name'] __ dckr_net_name:
            print ('Docker network "{}" already exists'.f..(dckr_net_name))
            bridge_found _ T..
            b..
    __ no. bridge_found:
        subnet _ conf['local_prefix']
        print ('creating Docker network "{}" with subnet {}'.f..(dckr_net_name, subnet))
        ipam _ IPAMConfig(pool_configs_[IPAMPool(subnet_subnet)])
        network _ dckr.create_network(dckr_net_name, driver_'bridge', ipam_ipam)

    num_tester _ sum(le.(t.get('neighbors', [])) ___ t __ conf.get('testers', []))
    __ num_tester > gc_thresh3
        print ('gc_thresh3({0}) is lower than the number of peer({1})'.f..(gc_thresh3(), num_tester))
        print ('type next to increase the value')
        print ('$ echo 16384 | sudo tee /proc/sys/net/ipv4/neigh/default/gc_thresh3')

    print ('run monitor')
    m _ Monitor(config_dir+'/monitor', conf['monitor'])
    m.run(conf, dckr_net_name)

    is_remote _ T.. __ 'remote' __ conf['target'] and conf['target']['remote'] ____ F..

    __ is_remote:
        print ('target is remote ({})'.f..(conf['target']['local-address']))

        ip _ IPRoute()

        # r: route to the target
        r _ ip.get_routes(dst_conf['target']['local-address'], family_AF_INET)
        __ le.(r) __ 0:
            print ('no route to remote target {0}'.f..(conf['target']['local-address']))
            ___.e..(1)

        # intf: interface used to reach the target
        idx _ [t[1] ___ t __ r[0]['attrs'] __ t[0] __ 'RTA_OIF'][0]
        intf _ ip.get_links(idx)[0]
        intf_name _ intf.get_attr('IFLA_IFNAME')

        # raw_bridge_name: Linux bridge name of the Docker bridge
        # TODO: not sure if the linux bridge name is always given by
        #       "br-<first 12 characters of Docker network ID>".
        raw_bridge_name _ args.bridge_name or 'br-{}'.f..(network['Id'][0:12])

        # raw_bridges: list of Linux bridges that match raw_bridge_name
        raw_bridges _ ip.link_lookup(ifname_raw_bridge_name)
        __ le.(raw_bridges) __ 0:
            __ no. args.bridge_name:
                print('can\'t determine the Linux bridge interface name starting '
                      'from the Docker network {}'.f..(dckr_net_name))
            ____
                print('the Linux bridge name provided ({}) seems nonexistent'.f..(
                      raw_bridge_name))
            print('Since the target is remote, the host interface used to '
                    'reach the target ({}) must be part of the Linux bridge '
                    'used by the Docker network {}, but without the correct Linux '
                    'bridge name it\'s impossible to verify if that\'s true'.f..(
                        intf_name, dckr_net_name))
            __ no. args.bridge_name:
                print('Please supply the Linux bridge name corresponding to the '
                      'Docker network {} using the --bridge-name argument.'.f..(
                          dckr_net_name))
            ___.e..(1)

        # intf_bridge: bridge interface that intf is already member of
        intf_bridge _ intf.get_attr('IFLA_MASTER')

        # if intf is not member of the bridge, add it
        __ intf_bridge no. __ raw_bridges:
            __ intf_bridge is N..:
                print('Since the target is remote, the host interface used to '
                      'reach the target ({}) must be part of the Linux bridge '
                      'used by the Docker network {}'.f..(
                          intf_name, dckr_net_name))
                ___.s_o_.w..('Do you confirm to add the interface {} '
                                 'to the bridge {}? [yes/NO] '.f..(
                                     intf_name, raw_bridge_name
                                    ))
                ___
                    answer _ in..()
                ______:
                    print ('aborting')
                    ___.e..(1)
                answer _ answer.s..
                __ answer.lower() !_ 'yes':
                    print ('aborting')
                    ___.e..(1)

                print ('adding interface {} to the bridge {}'.f..(
                    intf_name, raw_bridge_name)
                )
                br _ raw_bridges[0]

                ___
                    ip.link('set', index_idx, master_br)
                ______ E.. __ e:
                    print('Something went wrong: {}'.f..(st..(e)))
                    print('Please consider running the following command to '
                          'add the {iface} interface to the {br} bridge:\n'
                          '   sudo brctl addif {br} {iface}'.f..(
                              iface_intf_name, br_raw_bridge_name))
                    print('\n\n\n')
                    r_
            ____
                curr_bridge_name _ ip.get_links(intf_bridge)[0].get_attr('IFLA_IFNAME')
                print('the interface used to reach the target ({}) '
                      'is already member of the bridge {}, which is not '
                      'the one used in this configuration'.f..(
                          intf_name, curr_bridge_name))
                print('Please consider running the following command to '
                        'remove the {iface} interface from the {br} bridge:\n'
                        '   sudo brctl addif {br} {iface}'.f..(
                            iface_intf_name, br_curr_bridge_name))
                ___.e..(1)
    ____
        __ args.target __ 'gobgp':
            target_class _ GoBGPTarget
        ____ args.target __ 'bird':
            target_class _ BIRDTarget
        ____ args.target __ 'quagga':
            target_class _ QuaggaTarget

        print ('run', args.target)
        __ args.image:
            target _ target_class('{0}/{1}'.f..(config_dir, args.target), conf['target'], image_args.image)
        ____
            target _ target_class('{0}/{1}'.f..(config_dir, args.target), conf['target'])
        target.run(conf, dckr_net_name)

    t__.s..(1)

    print ('waiting bgp connection between {0} and monitor'.f..(args.target))
    m.wait_established(conf['target']['local-address'])

    __ no. args.repeat:
        ___ idx, tester __ enumerate(conf['testers']):
            __ 'name' no. __ tester:
                name _ 'tester{0}'.f..(idx)
            ____
                name _ tester['name']
            __ 'type' no. __ tester:
                tester_type _ 'normal'
            ____
                tester_type _ tester['type']
            __ tester_type __ 'normal':
                tester_class _ ExaBGPTester
            ____ tester_type __ 'mrt':
                __ 'mrt_injector' no. __ tester:
                    mrt_injector _ 'gobgp'
                ____
                    mrt_injector _ tester['mrt_injector']
                __ mrt_injector __ 'gobgp':
                    tester_class _ GoBGPMRTTester
                ____ mrt_injector __ 'exabgp':
                    tester_class _ ExaBGPMrtTester
                ____
                    print ('invalid mrt_injector:', mrt_injector)
                    ___.e..(1)
            ____
                print ('invalid tester type:', tester_type)
                ___.e..(1)
            t _ tester_class(name, config_dir+'/'+name, tester)
            print ('run tester', name, 'type', tester_type)
            t.run(conf['target'], dckr_net_name)

    start _ d_t_.d_t_.now()

    q _ Queue()

    m.stats(q)
    __ no. is_remote:
        target.stats(q)

    ___ mem_human(v):
        __ v > 1000 * 1000 * 1000:
            r_ '{0:.2f}GB'.f..(float(v) / (1000 * 1000 * 1000))
        ____ v > 1000 * 1000:
            r_ '{0:.2f}MB'.f..(float(v) / (1000 * 1000))
        ____ v > 1000:
            r_ '{0:.2f}KB'.f..(float(v) / 1000)
        ____
            r_ '{0:.2f}B'.f..(float(v))

    f _ o..(args.output, 'w') __ args.output ____ N..
    cpu _ 0
    mem _ 0
    cooling _ -1
    w__ T..:
        info _ q.get()

        __ no. is_remote and info['who'] __ target.name:
            cpu _ info['cpu']
            mem _ info['mem']

        __ info['who'] __ m.name:
            now _ d_t_.d_t_.now()
            elapsed _ now - start
            recved _ info['state']['adj-table']['accepted'] __ 'accepted' __ info['state']['adj-table'] ____ 0
            __ elapsed.seconds > 0:
                rm_line()
            print ('elapsed: {0}sec, cpu: {1:>4.2f}, mem: {2}, recved: {3}'.f..(elapsed.seconds, cpu, mem_human(mem), recved))
            f.w..('{0}, {1}, {2}, {3}\n'.f..(elapsed.seconds, cpu, mem, recved)) __ f ____ N..
            f.f.. __ f ____ N..

            __ cooling __ args.cooling:
                f.c.. __ f ____ N..
                r_

            __ cooling >_ 0:
                cooling +_ 1

            __ info['checked']:
                cooling _ 0

___ gen_conf(args):
    neighbor_num _ args.neighbor_num
    prefix _ args.prefix_num
    as_path_list _ args.as_path_list_num
    prefix_list _ args.prefix_list_num
    community_list _ args.community_list_num
    ext_community_list _ args.ext_community_list_num

    local_address_prefix _ netaddr.IPNetwork(args.local_address_prefix)

    __ args.target_local_address:
        target_local_address _ netaddr.IPAddress(args.target_local_address)
    ____
        target_local_address _ local_address_prefix.broadcast - 1

    __ args.monitor_local_address:
        monitor_local_address _ netaddr.IPAddress(args.monitor_local_address)
    ____
        monitor_local_address _ local_address_prefix.ip + 2

    __ args.target_router_id:
        target_router_id _ netaddr.IPAddress(args.target_router_id)
    ____
        target_router_id _ target_local_address

    __ args.monitor_router_id:
        monitor_router_id _ netaddr.IPAddress(args.monitor_router_id)
    ____
        monitor_router_id _ monitor_local_address

    conf _ {}
    conf['local_prefix'] _ st..(local_address_prefix)
    conf['target'] _ {
        'as': 1000,
        'router-id': st..(target_router_id),
        'local-address': st..(target_local_address),
        'single-table': args.single_table,
    }

    __ args.target_config_file:
        conf['target']['config_path'] _ args.target_config_file

    conf['monitor'] _ {
        'as': 1001,
        'router-id': st..(monitor_router_id),
        'local-address': st..(monitor_local_address),
        'check-points': [prefix * neighbor_num],
    }

    offset _ 0

    it _ netaddr.iter_iprange('90.0.0.0', '100.0.0.0')

    conf['policy'] _ {}

    assignment _ []

    __ prefix_list > 0:
        name _ 'p1'
        conf['policy'][name] _ {
            'match': [{
                'type': 'prefix',
                'value': list('{0}/32'.f..(ip) ___ ip __ islice(it, prefix_list)),
            }],
        }
        assignment.ap..(name)

    __ as_path_list > 0:
        name _ 'p2'
        conf['policy'][name] _ {
            'match': [{
                'type': 'as-path',
                'value': list(ra..(10000, 10000 + as_path_list)),
            }],
        }
        assignment.ap..(name)

    __ community_list > 0:
        name _ 'p3'
        conf['policy'][name] _ {
            'match': [{
                'type': 'community',
                'value': list('{0}:{1}'.f..(i/(1<<16), i(1<<16)) ___ i __ ra..(community_list)),
            }],
        }
        assignment.ap..(name)

    __ ext_community_list > 0:
        name _ 'p4'
        conf['policy'][name] _ {
            'match': [{
                'type': 'ext-community',
                'value': list('rt:{0}:{1}'.f..(i/(1<<16), i(1<<16)) ___ i __ ra..(ext_community_list)),
            }],
        }
        assignment.ap..(name)

    neighbors _ {}
    configured_neighbors_cnt _ 0
    ___ i __ ra..(3, neighbor_num+3+2):
        __ configured_neighbors_cnt __ neighbor_num:
            b..
        curr_ip _ local_address_prefix.ip + i
        __ curr_ip __ [target_local_address, monitor_local_address]:
            print('skipping tester\'s neighbor with IP {} because it collides with target or monitor'.f..(curr_ip))
            c..
        router_id _ st..(local_address_prefix.ip + i)
        neighbors[router_id] _ {
            'as': 1000 + i,
            'router-id': router_id,
            'local-address': router_id,
            'paths': '${{gen_paths({0})}}'.f..(prefix),
            'filter': {
                args.filter_type: assignment,
            },
        }
        configured_neighbors_cnt +_ 1

    conf['testers'] _ [{
        'name': 'tester',
        'type': 'normal',
        'neighbors': neighbors,
    }]
    r_ gen_mako_macro() + yaml.dump(conf, d.._flow_style_False)


___ config(args):
    conf _ gen_conf(args)

    w__ o..(args.output, 'w') __ f:
        f.w..(conf)


__ _______ __ ______
    parser _ AP..(d.._'BGP performance measuring tool')
    ?.a_a..('-b', '--bench-name', d.._'bgperf')
    parser.a_a..('-d', '--dir', d.._'/tmp')
    s _ parser.add_subparsers()
    parser_doctor _ s.add_parser('doctor', help_'check env')
    parser_doctor.set_d..s(func_doctor)

    parser_prepare _ s.add_parser('prepare', help_'prepare env')
    parser_prepare.a_a..('-f', '--force', a.._'store_true', help_'build even if the container already exists')
    parser_prepare.a_a..('-n', '--no-cache', a.._'store_true')
    parser_prepare.set_d..s(func_prepare)

    parser_update _ s.add_parser('update', help_'rebuild bgp docker images')
    parser_update.a_a..('image', choices_['exabgp', 'exabgp_mrtparse', 'gobgp', 'bird', 'quagga', 'all'])
    parser_update.a_a..('-c', '--checkout', d.._'HEAD')
    parser_update.a_a..('-n', '--no-cache', a.._'store_true')
    parser_update.set_d..s(func_update)

    ___ add_gen_conf_args(parser):
        ?.a_a..('-n', '--neighbor-num', d.._100, ty.._in.)
        ?.a_a..('-p', '--prefix-num', d.._100, ty.._in.)
        ?.a_a..('-l', '--filter-type', choices_['in', 'out'], d.._'in')
        ?.a_a..('-a', '--as-path-list-num', d.._0, ty.._in.)
        ?.a_a..('-e', '--prefix-list-num', d.._0, ty.._in.)
        ?.a_a..('-c', '--community-list-num', d.._0, ty.._in.)
        ?.a_a..('-x', '--ext-community-list-num', d.._0, ty.._in.)
        ?.a_a..('-s', '--single-table', a.._'store_true')
        ?.a_a..('--target-config-file', type_str,
                            help_'target BGP daemon\'s configuration file')
        ?.a_a..('--local-address-prefix', type_str, d.._'10.10.0.0/16',
                            help_'IPv4 prefix used for local addresses; default: 10.10.0.0/16')
        ?.a_a..('--target-local-address', type_str,
                            help_'IPv4 address of the target; default: the last address of the '
                                 'local prefix given in --local-address-prefix')
        ?.a_a..('--target-router-id', type_str,
                            help_'target\' router ID; default: same as --target-local-address')
        ?.a_a..('--monitor-local-address', type_str,
                            help_'IPv4 address of the monitor; default: the second address of the '
                                 'local prefix given in --local-address-prefix')
        ?.a_a..('--monitor-router-id', type_str,
                            help_'monitor\' router ID; default: same as --monitor-local-address')

    parser_bench _ s.add_parser('bench', help_'run benchmarks')
    parser_bench.a_a..('-t', '--target', choices_['gobgp', 'bird', 'quagga'], d.._'gobgp')
    parser_bench.a_a..('-i', '--image', help_'specify custom docker image')
    parser_bench.a_a..('--docker-network-name', help_'Docker network name; this is the name given by \'docker network ls\'')
    parser_bench.a_a..('--bridge-name', help_'Linux bridge name of the '
                              'interface corresponding to the Docker network; '
                              'use this argument only if bgperf can\'t '
                              'determine the Linux bridge name starting from '
                              'the Docker network name in case of tests of '
                              'remote targets.')
    parser_bench.a_a..('-r', '--repeat', a.._'store_true', help_'use existing tester/monitor container')
    parser_bench.a_a..('-f', '--file', metavar_'CONFIG_FILE')
    parser_bench.a_a..('-g', '--cooling', d.._0, ty.._in.)
    parser_bench.a_a..('-o', '--output', metavar_'STAT_FILE')
    add_gen_conf_args(parser_bench)
    parser_bench.set_d..s(func_bench)

    parser_config _ s.add_parser('config', help_'generate config')
    parser_config.a_a..('-o', '--output', d.._'bgperf.yml', type_str)
    add_gen_conf_args(parser_config)
    parser_config.set_d..s(func_config)


    args _ ?.p_a..
    args.func(args)
