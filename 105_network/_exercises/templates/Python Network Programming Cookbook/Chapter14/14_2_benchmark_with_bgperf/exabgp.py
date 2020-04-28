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

c_ ExaBGP(Container):

    GUEST_DIR _ '/root/config'

    ___ -  name, host_dir, conf, image_'bgperf/exabgp'):
        super(ExaBGP, self).- ('bgperf_exabgp_' + name, image, host_dir, GUEST_DIR, conf)

    @classmethod
    ___ build_image(cls, force_False, tag_'bgperf/exabgp', checkout_'HEAD', nocache_False):
        cls.dockerfile _ '''
FROM ubuntu:latest
WORKDIR /root
RUN apt-get update && apt-get install -qy git python python-setuptools gcc python-dev
RUN easy_install pip
RUN git clone https://github.com/Exa-Networks/exabgp && \
(cd exabgp && git checkout {0} && pip install six && pip install -r requirements.txt && python setup.py install)
RUN ln -s /root/exabgp /exabgp
'''.f..(checkout)
        super(ExaBGP, cls).build_image(force, tag, nocache)


c_ ExaBGP_MRTParse(Container):

    GUEST_DIR _ '/root/config'

    ___ -  name, host_dir, conf, image_'bgperf/exabgp_mrtparse'):
        super(ExaBGP_MRTParse, self).- ('bgperf_exabgp_mrtparse_' + name, image, host_dir, GUEST_DIR, conf)

    @classmethod
    ___ build_image(cls, force_False, tag_'bgperf/exabgp_mrtparse', checkout_'HEAD', nocache_False):
        cls.dockerfile _ '''
FROM ubuntu:latest
WORKDIR /root
RUN apt-get update && apt-get install -qy git python python-setuptools gcc python-dev
RUN easy_install pip
RUN git clone https://github.com/Exa-Networks/exabgp && \
(cd exabgp && git checkout {0} && pip install six && pip install -r requirements.txt && python setup.py install)
RUN ln -s /root/exabgp /exabgp
RUN git clone https://github.com/t2mune/mrtparse.git && \
(cd mrtparse && python setup.py install)
'''.f..(checkout)
        super(ExaBGP_MRTParse, cls).build_image(force, tag, nocache)
