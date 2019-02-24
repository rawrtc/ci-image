FROM ubuntu:bionic

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
    cmake \
    gcc \
    libc-dev \
    libssl-dev \
    pkg-config \
    python3-pip \
    python3-setuptools \
    make \
    ninja-build

# Install Meson
RUN pip3 install meson==0.49.2
