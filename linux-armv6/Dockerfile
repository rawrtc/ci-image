FROM rawrtc/cross-build:base

# Apply dockcross/linux-armv6
COPY --from=dockcross/linux-armv6:latest / /

# Environment
ENV CROSS_TRIPLE arm-linux-gnueabihf
ENV CROSS_ROOT /usr/${CROSS_TRIPLE}
ENV CROSS_FILE_NAME linux-armv6
# Allow dynamically linked executables to run with qemu-arm
ENV QEMU_LD_PREFIX ${CROSS_ROOT}/libc
ENV QEMU_SET_ENV "LD_LIBRARY_PATH=${CROSS_ROOT}/lib:${CROSS_ROOT}/libc/lib/${CROSS_TRIPLE}/"

# Generate Meson cross-file
COPY generate-meson-cross-file.py .
RUN mkdir -p /usr/local/share/meson/cross \
 && python3 generate-meson-cross-file.py \
    > /usr/local/share/meson/cross/${CROSS_FILE_NAME} \
 && rm generate-meson-cross-file.py
