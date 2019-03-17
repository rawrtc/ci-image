# Based on: https://github.com/dockcross/dockcross/blob/master/android-arm64/Dockerfile
FROM rawrtc/cross-build:android-base

# Environment
ENV CROSS_ROOT=${ANDROID_NDK_HOME}/toolchains/llvm/prebuilt/linux-x86_64 \
    CROSS_TRIPLE=aarch64-linux-android \
    CROSS_FILE_NAME=android-28-arm64 \
    ANDROID_ARCH=arm64 \
    ANDROID_API_LEVEL=28 \
    OPENSSL_VERSION=1.1.1b
ENV PKG_CONFIG_LIBDIR=${CROSS_ROOT}/sysroot/lib/pkgconfig:${CROSS_ROOT}/sysroot/usr/lib/${CROSS_TRIPLE}/${ANDROID_API_LEVEL}/pkgconfig


# Install emulator dependencies
RUN sed -i '/debian-security/d' /etc/apt/sources.list \
 && dpkg --add-architecture arm64 \ 
 && apt-get update

# Install emulator
RUN apt-get update \
 && apt-get install -qqy --no-install-recommends \
    qemu-user \
    qemu-user-static

# Generate Meson cross-file
COPY generate-android-meson-cross-file.py /build/generate-android-meson-cross-file.py
RUN python3 /build/generate-android-meson-cross-file.py \
 && rm -rf /build

# Build minimal OpenSSL
RUN mkdir /build \
 && cd /build \
 && export PATH=${CROSS_ROOT}/bin:$PATH \
 && curl -O https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \
 && tar -xzf openssl-${OPENSSL_VERSION}.tar.gz \
 && cd openssl-${OPENSSL_VERSION} \
 && ./Configure android-${ANDROID_ARCH} \
    --prefix=${CROSS_ROOT}/sysroot --openssldir=${CROSS_ROOT}/sysroot \
    --api=1.0.0 -D__ANDROID_API__=${ANDROID_API_LEVEL} \
    -ffunction-sections -fdata-sections -L-Wl,--gc-sections \
    no-capieng no-cms no-ct no-comp no-heartbeats no-hw-padlock no-nextprotoneg no-ocsp no-psk no-shared no-srp no-tests no-ts \
    no-ssl3 no-tls \
    no-aria no-bf no-blake2 no-camellia no-cast no-des no-dsa no-gost no-idea no-md2 no-md4 no-mdc2 no-ocb no-rc2 no-rc4 no-rc5 no-rmd160 no-scrypt no-seed no-siphash no-sm2 no-sm3 no-sm4 no-whirlpool \
 && make install_sw \
 && rm -rf /build
