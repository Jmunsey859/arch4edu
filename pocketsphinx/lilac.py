#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}]
build_prefix = 'arch4edu-x86_64'
depends = ['sphinxbase']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if 'python3.6' in line:
            print(line.replace('python3.6', 'python3.7'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
