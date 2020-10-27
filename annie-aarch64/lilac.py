#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'action-extra-aarch64'

def pre_build():
    aur_pre_build('annie')
    add_arch(['aarch64'])

post_build = aur_post_build

if __name__ == '__main__':
    from action_tools import action_main
    action_main(build_prefix)
