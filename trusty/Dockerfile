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
    python3-pip \
    make

# Install Meson
RUN pip3 install meson

# Build OpenSSL
RUN curl -O https://www.openssl.org/source/openssl-1.1.1a.tar.gz \
 && tar -zxf openssl-1.1.1a.tar.gz \
 && cd openssl-1.1.1a \
 && ./config shared \
 && make \
 && make install \
 && ldconfig
