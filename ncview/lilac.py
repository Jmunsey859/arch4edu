#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'heavysink', 'email': 'Heavysink <winstonwu91@gmail.com>'}]
repo_depends = ['udunits']
build_prefix = 'extra-x86_64'
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
