# Based on: https://github.com/dockcross/dockcross/blob/master/android-arm64/Dockerfile
FROM rawrtc/cross-build:base

# Environment
ENV CROSS_ROOT /usr/android-27-arm64
ENV CROSS_FILE_NAME android-27-arm64
ENV ANDROID_NDK_REVISION 18b
ENV ANDROID_NDK_API 27
ENV ANDROID_ARCH arm64


# Install emulator dependencies
RUN sed -i '/debian-security/d' /etc/apt/sources.list \
 && dpkg --add-architecture arm64 \
 && apt-get update

# Install emulator
RUN apt-get install -qqy --no-install-recommends \
    qemu-user \
    qemu-user-static \
    unzip

# Install standalone toolchain
RUN mkdir -p /build \
 && cd /build \
 && curl -O https://dl.google.com/android/repository/android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip \
 && unzip ./android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip \
 && cd android-ndk-r${ANDROID_NDK_REVISION}/build/tools \
 && ./make_standalone_toolchain.py \
      --arch ${ANDROID_ARCH} \
      --api ${ANDROID_NDK_API} \
      --install-dir=${CROSS_ROOT}

# Generate Meson cross-file
COPY generate-android-meson-cross-file.py /build/android-ndk-r${ANDROID_NDK_REVISION}/build/tools
RUN cd /build/android-ndk-r${ANDROID_NDK_REVISION}/build/tools \
 && python3 generate-android-meson-cross-file.py

# Cleanup
RUN cd / \
 && rm -rf /build \
 && find ${CROSS_ROOT} -exec chmod a+r '{}' \; \
 && find ${CROSS_ROOT} -executable -exec chmod a+x '{}' \;
