FROM archlinux/base:latest

# Update
RUN pacman -Syu --noconfirm

# CircleCI dependencies
RUN pacman -Sy --noconfirm --needed \
    ca-certificates \
    git \
    gzip \
    openssh \
    tar

# Build dependencies
RUN pacman -Sy --noconfirm --needed \
    base-devel \
    clang \
    cmake \
    gcc \
    meson \
    openssl
