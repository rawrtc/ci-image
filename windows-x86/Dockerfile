FROM rawrtc/cross-build:base

# Apply dockcross/windows-x86
COPY --from=dockcross/windows-x86:latest / /

# Environment
ENV CROSS_ROOT /usr/src/mxe/usr
ENV CROSS_TRIPLE i686-w64-mingw32.static
ENV CROSS_FILE_NAME windows-x86
ENV WINEARCH win32

# Generate Meson cross-file
COPY generate-meson-cross-file.py .
RUN mkdir -p /usr/local/share/meson/cross \
 && python3 generate-meson-cross-file.py \
    > /usr/local/share/meson/cross/${CROSS_FILE_NAME} \
 && rm generate-meson-cross-file.py

