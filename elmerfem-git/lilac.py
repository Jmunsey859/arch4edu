#!/usr/bin/env python3
from lilaclib import *

from pyalpm import Handle
arch = 'x86_64'
package = 'glfw-wayland'
dbpath = '/var/lib/archbuild/extra-x86_64/root/var/lib/pacman/'
gpgpath = '/var/lib/archbuild/extra-x86_64/root/etc/pacman.d/gnupg'
mirror = 'https://mirrors.tuna.tsinghua.edu.cn/archlinux'
handle = Handle('/', dbpath)
for i in ['core', 'extra', 'community']:
    repo = handle.register_syncdb(i, 0)
for repo in handle.get_syncdbs():
    result = repo.get_pkg(package)
    if result:
        url = f'{mirror}/{repo.name}/os/{arch}/{result.filename}'
        break

repo_depends = ['mumps-par' ,'oce' ,'hypre' ,'mmg' ,'libnn-git' ,'libcsa-git' ,'scalapack']
build_prefix = 'extra-x86_64'
time_limit_hours = 8
makechrootpkg_args = ['-I', 'tmp/'+result.filename]

def pre_build():
    vcs_update()

    run_cmd(['wget', '-nc', url, url+'.sig'])
    run_cmd(['gpg', '--homedir', gpgpath, '--verify', result.filename+'.sig', result.filename])
    run_cmd(['mkdir', '-p', 'tmp'])
    run_cmd(['mv', result.filename, result.filename+'.sig', 'tmp'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
