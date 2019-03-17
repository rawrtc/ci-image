# Based on: https://github.com/dockcross/dockcross/blob/master/android-arm64/Dockerfile
FROM rawrtc/cross-build:base

# Environment
ENV ANDROID_NDK_REVISION=19c \
    ANDROID_NDK_HOME=/usr/android-ndk

# Install Android NDK dependencies
RUN apt-get update \
 && apt-get install -qqy --no-install-recommends \
    unzip

# Install Android NDK
RUN mkdir -p /build \
 && cd /build \
 && curl -O https://dl.google.com/android/repository/android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip \
 && unzip ./android-ndk-r${ANDROID_NDK_REVISION}-linux-x86_64.zip \
 && mv android-ndk-r${ANDROID_NDK_REVISION} ${ANDROID_NDK_HOME} \
 && find ${ANDROID_NDK_HOME}/toolchains -exec chmod a+r '{}' \; \
 && find ${ANDROID_NDK_HOME}/toolchains -executable -exec chmod a+x '{}' \; \
 && rm -rf /build

