#!/usr/bin/env python3
import os


cross_file_formatter = """\
[host_machine]
system = 'windows'
cpu_family = 'x86_64'
cpu = 'x86_64'
endian = 'little'

[properties]
root = '{CROSS_ROOT}'
sys_root = '{CROSS_ROOT}/{CROSS_TRIPLE}'

[binaries]
c = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-gcc'
cpp = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-cpp'
ar = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-ar'
as = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-as'
ld = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-ld'
strip = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-strip'
pkgconfig = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-pkg-config'
windres = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-windres'
fortran = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-gfortran'
exe_wrapper = 'wine'
"""

if __name__ == '__main__':
    print(cross_file_formatter.format(**os.environ), end='')

