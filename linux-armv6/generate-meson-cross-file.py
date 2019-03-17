#!/usr/bin/env python3
import os


cross_file_formatter = """\
[host_machine]
system = 'linux'
cpu_family = 'arm'
cpu = 'armv6l'
endian = 'little'

[properties]
root = '{CROSS_ROOT}'
sys_root = '{CROSS_SYSROOT}'
c_std = 'c99'
needs_exe_wrapper = true

[paths]
prefix = '{CROSS_SYSROOT}'

[binaries]
c = '/usr/bin/{CROSS_TRIPLE}-gcc'
cpp = '/usr/bin/{CROSS_TRIPLE}-cpp'
ar = '/usr/bin/{CROSS_TRIPLE}-ar'
as = '/usr/bin/{CROSS_TRIPLE}-as'
ld = '/usr/bin/{CROSS_TRIPLE}-ld'
strip = '/usr/bin/{CROSS_TRIPLE}-strip'
fortran = '/usr/bin/{CROSS_TRIPLE}-gfortran'
pkgconfig = '/usr/bin/{CROSS_TRIPLE}-pkg-config'
exe_wrapper = 'qemu-arm'
"""

if __name__ == '__main__':
    print(cross_file_formatter.format(**os.environ), end='')

