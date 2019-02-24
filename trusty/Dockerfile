FROM ubuntu:trusty

RUN apt-get update -qqy

# CircleCI dependencies
RUN apt-get install -qqy --no-install-recommends \
    ca-certificates \
    git \
    gzip \
    openssh-client \
    tar

# Build dependencies
RUN apt-get install -qqy --no-install-recommends \
    autoconf \
    clang \
    cmake3 \
    curl \
    gcc \
    libc-dev \
    pkg-config \
    python3.5 \
    unzip \
    make

# Download and install ninja >= 1.5
RUN curl -L -O https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip \
 && unzip ninja-linux.zip -d /usr/local/bin \
 && chmod a+x /usr/local/bin/ninja

# Download and install pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py \
 && python3.5 get-pip.py \
 && rm get-pip.py

# Install Meson
RUN pip install meson==0.49.2

# Build OpenSSL
RUN curl -O https://www.openssl.org/source/openssl-1.1.1a.tar.gz \
 && tar -zxf openssl-1.1.1a.tar.gz \
 && cd openssl-1.1.1a \
 && ./config shared \
 && make \
 && make install \
 && ldconfig \
 && cd .. \
 && rm -rf openssl-1.1.1a openssl-1.1.1a.tar.gz
