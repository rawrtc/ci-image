FROM dockcross/base:latest

# Environment
ENV PY3_VERSION 3.7.1
ENV PY3_POSTFIX 3.7

# Install Python 3.x with pip
RUN apt-get update \
 && apt-get install -qqy --no-install-recommends \
    libffi-dev \
 && curl -O https://www.python.org/ftp/python/${PY3_VERSION}/Python-${PY3_VERSION}.tgz \
 && tar xf Python-${PY3_VERSION}.tgz \
 && cd Python-${PY3_VERSION} \
 && ./configure --with-ensurepip=install \
 && make -j 8 \
 && make altinstall \
 && cd .. \
 && rm -r Python-${PY3_VERSION} \
 && rm Python-${PY3_VERSION}.tgz

# Create python3 and pip3 symlink
RUN ln -s `which python${PY3_POSTFIX}` /usr/local/bin/python3 \
 && ln -s `which pip${PY3_POSTFIX}` /usr/local/bin/pip3

# Install Meson
RUN pip3 install meson==0.50.0
