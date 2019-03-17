#!/usr/bin/env python3
import os
import pathlib

cross_file_formatter = """\
[host_machine]
system = 'linux'
cpu_family = '{cpu_family}'
cpu = '{cpu}'
endian = 'little'

[properties]
root = '{root}'
needs_exe_wrapper = true

[paths]
prefix = '{root}/sysroot'

[binaries]
c = '{root}/bin/{clang_prefix}-clang'
cpp = '{root}/bin/{clang_prefix}-clang++'
ar = '{root}/bin/{triple}-ar'
as = '{root}/bin/{triple}-as'
ld = '{root}/bin/ld.lld'
strip = '{root}/bin/{triple}-strip'
pkgconfig = '/usr/bin/pkg-config'
# https://groups.google.com/forum/#!topic/mesonbuild/wTzIblOGs8w
# exe_wrapper = 'qemu-arm'
"""


def get_cpu_family(arch):
    if arch == 'arm64':
        return 'aarch64'
    return arch


def get_clang_prefix(arch, triple, api_level):
    if arch == 'arm':
        triple = triple.replace('arm', 'armv7a', 1)
    return '{}{}'.format(triple, api_level)


def main():
    root = os.environ['CROSS_ROOT']
    triple = os.environ['CROSS_TRIPLE']
    cross_filename = os.environ['CROSS_FILE_NAME']
    arch = os.environ['ANDROID_ARCH']
    api_level = os.environ['ANDROID_API_LEVEL']
    path = pathlib.Path('/usr/local/share/meson/cross')
    path.mkdir(parents=True, exist_ok=True) 

    with open(str(path / cross_filename), 'w') as cross_file:
        cross_file.write(cross_file_formatter.format(
            cpu_family=get_cpu_family(arch),
            cpu=arch,  # not accurate
            root=root,
            triple=triple,
            clang_prefix=get_clang_prefix(arch, triple, api_level),
        ))
    
    print("cross-file available as '{}'".format(cross_filename))

if __name__ == '__main__':
    main()

