#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
pre_build = aur_pre_build

def post_build():
    run_cmd('git add -f plantuml.run'.split(' '))
    aur_post_build()

if __name__ == '__main__':
  single_main(build_prefix)
