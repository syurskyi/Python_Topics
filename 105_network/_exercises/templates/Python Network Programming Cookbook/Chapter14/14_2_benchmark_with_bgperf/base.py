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

____ settings ______ dckr
______ io
______ __
______ yaml
____ itertools ______ chain
____ th.. ______ T..
______ netaddr
______ ___

flatten _ lambda l: chain.from_iterable(l)

___ get_ctn_names
    names _ list(flatten(n['Names'] ___ n __ dckr.containers(all_True)))
    r_ [n[1:] __ n[0] __ '/' ____ n ___ n __ names]


___ ctn_exists(name):
    r_ name __ get_ctn_names()


___ img_exists(name):
    r_ name __ [ctn['RepoTags'][0].s..(':')[0] ___ ctn __ dckr.images() __ ctn['RepoTags'] !_ None]


___ rm_line
    print ('\x1b[1A\x1b[2K\x1b[1D\x1b[1A')


c_ Container(o..):
    ___ -  name, image, host_dir, guest_dir, conf):
        name _ name
        image _ image
        host_dir _ host_dir
        guest_dir _ guest_dir
        conf _ conf
        config_name _ None
        __ no. __.pa__.e..(host_dir):
            __.makedirs(host_dir)
            __.chmod(host_dir, 0o777)

    @classmethod
    ___ build_image(cls, force, tag, nocache_False):
        ___ insert_after_from(dockerfile, line):
            lines _ dockerfile.s..('\n')
            i _ -1
            ___ idx, l __ enumerate(lines):
                elems _ [e.s.. ___ e __ l.s..()]
                __ le.(elems) > 0 and elems[0] __ 'FROM':
                    i _ idx
            __ i < 0:
                r_ E..('no FROM statement')
            lines.insert(i+1, line)
            r_ '\n'.j..(lines)

        ___ env __ ['http_proxy', 'https_proxy']:
            __ env __ __.environ:
                cls.dockerfile _ insert_after_from(cls.dockerfile, 'ENV {0} {1}'.format(env, __.environ[env]))

        f _ io.BytesIO(cls.dockerfile.e..('utf-8'))
        __ force or no. img_exists(tag):
            print ('build {0}...'.format(tag))
            ___ line __ dckr.build(fileobj_f, rm_True, tag_tag, decode_True, nocache_nocache):
                __ 'stream' __ line:
                    print (line['stream'].strip())

    ___ get_ipv4_addresses
        __ 'local-address' __ conf:
            local_addr _ conf['local-address']
            r_ [local_addr]
        r_ NotImplementedError()

    ___ run dckr_net_name_'', rm_True):

        __ rm and ctn_exists(name):
            print ('remove container:', name)
            dckr.remove_container(name, force_True)

        host_config _ dckr.create_host_config(
            binds_['{0}:{1}'.format(__.pa__.abspath(host_dir), guest_dir)],
            privileged_True,
            network_mode_'bridge',
            cap_add_['NET_ADMIN']
        )

        ctn _ dckr.create_container(image_self.image, entrypoint_'bash', detach_True, name_self.name,
                                    stdin_open_True, volumes_[guest_dir], host_config_host_config)
        ctn_id _ ctn['Id']

        ipv4_addresses _ get_ipv4_addresses()

        net_id _ None
        ___ network __ dckr.networks(names_[dckr_net_name]):
            __ network['Name'] !_ dckr_net_name:
                c..

            net_id _ network['Id']
            __ no. 'IPAM' __ network:
                print('can\'t verify if container\'s IP addresses '
                      'are valid for Docker network {}: missing IPAM'.format(dckr_net_name))
                b..
            ipam _ network['IPAM']

            __ no. 'Config' __ ipam:
                print('can\'t verify if container\'s IP addresses '
                      'are valid for Docker network {}: missing IPAM.Config'.format(dckr_net_name))
                b..

            ip_ok _ F..
            network_subnets _ [item['Subnet'] ___ item __ ipam['Config'] __ 'Subnet' __ item]
            ___ ip __ ipv4_addresses:
                ___ subnet __ network_subnets:
                    ip_ok _ netaddr.IPAddress(ip) __ netaddr.IPNetwork(subnet)

                __ no. ip_ok:
                    print('the container\'s IP address {} is not valid for Docker network {} '
                          'since it\'s not part of any of its subnets ({})'.format(
                              ip, dckr_net_name, ', '.j..(network_subnets)))
                    print('Please consider removing the Docket network {net} '
                          'to allow bgperf to create it again using the '
                          'expected subnet:\n'
                          '  docker network rm {net}'.format(net_dckr_net_name))
                    ___.e..(1)
            b..

        __ net_id is None:
            print ('Docker network "{}" not found!'.format(dckr_net_name))
            r_

        dckr.connect_container_to_network(ctn_id, net_id, ipv4_address_ipv4_addresses[0])
        dckr.start(container_self.name)

        __ le.(ipv4_addresses) > 1:

            # get the interface used by the first IP address already added by Docker
            dev _ None
            res _ local('ip addr')
            ___ line __ res.s..(b'\n'):
                __ ipv4_addresses[0].e..('utf-8') __ line:
                    dev _ line.s..(b' ')[-1].s..
            __ no. dev:
                dev _ "eth0"

            ___ ip __ ipv4_addresses[1:]:
                local('ip addr add {} dev {}'.format(ip, dev))

        r_ ctn

    ___ stats queue):
        ___ stats
            ___ stat __ dckr.stats(ctn_id, decode_True):
                cpu_percentage _ 0.0
                prev_cpu _ stat['precpu_stats']['cpu_usage']['total_usage']
                __ 'system_cpu_usage' __ stat['precpu_stats']:
                    prev_system _ stat['precpu_stats']['system_cpu_usage']
                ____
                    prev_system _ 0
                cpu _ stat['cpu_stats']['cpu_usage']['total_usage']
                system _ stat['cpu_stats']['system_cpu_usage']
                cpu_num _ le.(stat['cpu_stats']['cpu_usage']['percpu_usage'])
                cpu_delta _ float(cpu) - float(prev_cpu)
                system_delta _ float(system) - float(prev_system)
                __ system_delta > 0.0 and cpu_delta > 0.0:
                    cpu_percentage _ (cpu_delta / system_delta) * float(cpu_num) * 100.0
                mem_usage _ stat['memory_stats'].get('usage', 0)
                queue.put({'who': name, 'cpu': cpu_percentage, 'mem': mem_usage})

        t _ T..(target_stats)
        t.daemon _ T..
        t.s..

    ___ local cmd, stream_False, detach_False):
        i _ dckr.exec_create(container_self.name, cmd_cmd)
        r_ dckr.exec_start(i['Id'], stream_stream, detach_detach)

    ___ get_startup_cmd
        r_ NotImplementedError()

    ___ exec_startup_cmd stream_False, detach_False):
        startup_content _ get_startup_cmd()

        __ no. startup_content:
            r_

        filename _ '{0}/start.sh'.format(host_dir)
        with open(filename, 'w') __ f:
            f.write(startup_content)
        __.chmod(filename, 0o777)

        r_ local('{0}/start.sh'.format(guest_dir),
                          detach_detach,
                          stream_stream)


c_ Target(Container):

    CONFIG_FILE_NAME _ None

    ___ write_config scenario_global_conf):
        r_ NotImplementedError()

    ___ use_existing_config
        __ 'config_path' __ conf:
            with open('{0}/{1}'.format(host_dir, CONFIG_FILE_NAME), 'w') __ f:
                with open(conf['config_path'], 'r') __ orig:
                    f.write(orig.read())
            r_ T..
        r_ F..

    ___ run scenario_global_conf, dckr_net_name_''):
        ctn _ super(Target, self).run(dckr_net_name)

        __ no. use_existing_config
            write_config(scenario_global_conf)

        exec_startup_cmd(detach_True)

        r_ ctn


c_ Tester(Container):

    CONTAINER_NAME_PREFIX _ None

    ___ -  name, host_dir, conf, image):
        Container.-  CONTAINER_NAME_PREFIX + name, image, host_dir, GUEST_DIR, conf)

    ___ get_ipv4_addresses
        res _ []
        peers _ list(conf.get('neighbors', {}).values())
        ___ p __ peers:
            res.ap..(p['local-address'])
        r_ res

    ___ configure_neighbors target_conf):
        r_ NotImplementedError()

    ___ run target_conf, dckr_net_name):
        ctn _ super(Tester, self).run(dckr_net_name)

        configure_neighbors(target_conf)

        output _ exec_startup_cmd(stream_True, detach_False)

        cnt _ 0
        prev_pid _ 0
        ___ lines __ output:
            ___ line __ lines.s...s..(b'\n'):
                pid _ int((line.s..(b'|')[1]).d..("utf-8"))
                __ pid !_ prev_pid:
                    prev_pid _ pid
                    cnt +_ 1
                    __ cnt > 1:
                        rm_line()
                    print('tester booting.. ({0}/{1})'.format(cnt, le.(list(conf.get('neighbors', {}).values()))))

        r_ ctn
