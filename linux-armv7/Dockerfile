FROM rawrtc/cross-build:base

# Apply dockcross/linux-armv7
COPY --from=dockcross/linux-armv7:latest / /

# Environment
ENV CROSS_TRIPLE=armv7-unknown-linux-gnueabi
ENV CROSS_ROOT=/usr/xcc/${CROSS_TRIPLE} \
    CROSS_FILE_NAME=linux-armv7 \
    OPENSSL_VERSION=1.1.1b
ENV CROSS_SYSROOT=${CROSS_ROOT}/${CROSS_TRIPLE}/sysroot
ENV PKG_CONFIG_LIBDIR=${CROSS_SYSROOT}/lib/pkgconfig:${CROSS_SYSROOT}/usr/lib/pkgconfig

# Allow dynamically linked executables to run with qemu-arm
ENV QEMU_LD_PREFIX="${CROSS_SYSROOT}"
ENV QEMU_SET_ENV="LD_LIBRARY_PATH=${CROSS_ROOT}/lib:${QEMU_LD_PREFIX}"

# Generate Meson cross-file
COPY generate-meson-cross-file.py /build/generate-meson-cross-file.py
RUN mkdir -p /usr/local/share/meson/cross \
 && python3 /build/generate-meson-cross-file.py \
    > /usr/local/share/meson/cross/${CROSS_FILE_NAME} \
&& rm -rf /build

# Build minimal OpenSSL
RUN mkdir /build \
 && cd /build \
 && curl -O https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \
 && tar -xzf openssl-${OPENSSL_VERSION}.tar.gz \
 && cd openssl-${OPENSSL_VERSION} \
 && ./Configure linux-armv4 \
    --prefix=${CROSS_SYSROOT}/usr --openssldir=${CROSS_SYSROOT}/usr \
    --cross-compile-prefix=${CROSS_ROOT}/bin/${CROSS_TRIPLE}- --api=1.0.0 \
    -ffunction-sections -fdata-sections -L-Wl,--gc-sections \
    no-capieng no-cms no-ct no-comp no-heartbeats no-hw-padlock no-nextprotoneg no-ocsp no-psk no-srp no-tests no-ts \
    no-ssl3 no-tls \
    no-aria no-bf no-blake2 no-camellia no-cast no-des no-dsa no-gost no-idea no-md2 no-md4 no-mdc2 no-ocb no-rc2 no-rc4 no-rc5 no-rmd160 no-scrypt no-seed no-siphash no-sm2 no-sm3 no-sm4 no-whirlpool \
 && make install_sw \
&& rm -rf /build

