#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
build_prefix = 'extra-x86_64'
repo_depends = [('intel-parallel-studio-xe', 'intel-common-libs'), ('intel-parallel-studio-xe', 'intel-compiler-base'), ('intel-parallel-studio-xe', 'intel-fortran-compiler'), ('intel-parallel-studio-xe', 'intel-openmp')]
repo_depends += ['python-numpy-mkl']
makechrootpkg_args = ['-D', '/opt/intel/licenses']

def pre_build():
    aur_pre_build()

    for line in edit_file('PKGBUILD'):
        if line.startswith('makedepends=('):
            print(line.replace('numpy', 'numpy-mkl'))
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
