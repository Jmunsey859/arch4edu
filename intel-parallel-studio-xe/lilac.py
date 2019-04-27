#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny'}]
update_on = [{'aur': 'intel-mkl'}]
build_prefix = 'extra-x86_64'

def pre_build():

    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        print(line.replace('.pkg.tar.lzo', '.pkg.tar.xz'))

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
