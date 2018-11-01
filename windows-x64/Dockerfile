FROM rawrtc/cross-build:base

# Apply dockcross/windows-x64
COPY --from=dockcross/windows-x64:latest / /

# Environment
ENV CROSS_ROOT /usr/src/mxe/usr
ENV CROSS_TRIPLE x86_64-w64-mingw32.static
ENV CROSS_FILE_NAME windows-x64
ENV WINEARCH win64

# Generate Meson cross-file
COPY generate-meson-cross-file.py .
RUN mkdir -p /usr/local/share/meson/cross \
 && python3 generate-meson-cross-file.py \
    > /usr/local/share/meson/cross/${CROSS_FILE_NAME} \
 && rm generate-meson-cross-file.py

