#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': 'distccd-armv6h'}]
build_prefix = 'arch4edu-x86_64'
depends = ['x-tools-armv6-bin', 'x-tools-armv7-bin', 'x-tools-armv8-bin']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
