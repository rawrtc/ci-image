#!/usr/bin/env python3
import os


cross_file_formatter = """\
[host_machine]
system = 'linux'
cpu_family = 'arm'
cpu = 'armv7l'
endian = 'little'

[properties]
root = '{CROSS_ROOT}'
sys_root = '{CROSS_SYSROOT}'
c_std = 'c99'
needs_exe_wrapper = true

[paths]
prefix = '{CROSS_SYSROOT}/usr'

[binaries]
c = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-gcc'
cpp = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-cpp'
ar = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-ar'
as = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-as'
ld = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-ld'
strip = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-strip'
fortran = '{CROSS_ROOT}/bin/{CROSS_TRIPLE}-gfortran'
pkgconfig = '/usr/bin/pkg-config'
# https://github.com/dockcross/dockcross/issues/274
# exe_wrapper = 'qemu-arm'
"""

if __name__ == '__main__':
    print(cross_file_formatter.format(**os.environ), end='')

