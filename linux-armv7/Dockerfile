FROM rawrtc/cross-build:base

# Apply dockcross/linux-armv7
COPY --from=dockcross/linux-armv7:latest / /

# Environment
ENV CROSS_TRIPLE armv7-unknown-linux-gnueabi
ENV CROSS_ROOT /usr/xcc/${CROSS_TRIPLE}
ENV CROSS_FILE_NAME linux-armv7
# Allow dynamically linked executables to run with qemu-arm
ENV QEMU_LD_PREFIX "${CROSS_ROOT}/${CROSS_TRIPLE}/sysroot"
ENV QEMU_SET_ENV "LD_LIBRARY_PATH=${CROSS_ROOT}/lib:${QEMU_LD_PREFIX}"

# Generate Meson cross-file
COPY generate-meson-cross-file.py .
RUN mkdir -p /usr/local/share/meson/cross \
 && python3 generate-meson-cross-file.py \
    > /usr/local/share/meson/cross/${CROSS_FILE_NAME} \
 && rm generate-meson-cross-file.py

