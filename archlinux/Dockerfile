FROM archlinux/base:latest

# Workaround for "systemd-libs and libsystemd are in conflict"
RUN yes | pacman -Sy --needed systemd-libs

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
