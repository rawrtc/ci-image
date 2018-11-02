#!/usr/bin/env python3
import os
import pathlib

from make_standalone_toolchain import get_triple


cross_file_formatter = """\
[host_machine]
system = 'linux'
cpu_family = '{cpu_family}'
cpu = '{cpu}'
endian = 'little'

[properties]
root = '{root}/{triple}'

[binaries]
c = '{root}/bin/{triple}-clang'
cpp = '{root}/bin/{triple}-clang++'
ar = '{root}/bin/{triple}-ar'
as = '{root}/bin/{triple}-as'
ld = '{root}/bin/{triple}-ld'
strip = '{root}/bin/{triple}-strip'
# https://groups.google.com/forum/#!topic/mesonbuild/wTzIblOGs8w
# exe_wrapper = 'qemu-arm'
"""


def get_cpu_family(arch):
    if arch == 'arm64':
        return 'aarch64'
    return arch


def main():
    arch = os.environ['ANDROID_ARCH']
    cross_root = os.environ['CROSS_ROOT']
    cross_filename = os.environ['CROSS_FILE_NAME']
    path = pathlib.Path('/usr/local/share/meson/cross')
    path.mkdir(parents=True, exist_ok=True) 

    with open(str(path / cross_filename), 'w') as cross_file:
        cross_file.write(cross_file_formatter.format(
            cpu_family=get_cpu_family(arch),
            cpu=arch,  # not accurate
            root=cross_root,
            triple=get_triple(arch),
        ))
    
    print("cross-file available as '{}'".format(cross_filename))

if __name__ == '__main__':
    main()

