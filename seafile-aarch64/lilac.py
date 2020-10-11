#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-aarch64'
repo_depends = [('libsearpc-aarch64', 'libsearpc'), ('ccnet-server-aarch64', 'ccnet-server')]

def pre_build():
    aur_pre_build('seafile')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
