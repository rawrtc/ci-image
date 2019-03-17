#!/usr/bin/env python3
import pathlib
import shutil
import sys

from jinja2 import Template


def get_triple(arch):
    return {
        'arm': 'arm-linux-androideabi',
        'arm64': 'aarch64-linux-android',
        'x86': 'i686-linux-android',
        'x86_64': 'x86_64-linux-android',
    }[arch]


def main():
    # Android API levels
    try:
        api_levels = sys.argv[1]
    except IndexError:
        api_levels = [
            '16',  # Android 4.1/4.1.1
            '28',  # Android 9.0
        ]
    else:
        api_levels = [api_level.strip() for api_level in api_levels.split(',')]
    print('Android API levels:', api_levels)

    # Architectures
    try:
        architectures = sys.argv[2]
    except IndexError:
        architectures = [
            'arm',
            'arm64',
            'x86',
            'x86_64',
        ]
    else:
        architectures = [arch.strip() for arch in architectures.split(',')]
    print('Architectures:', architectures)

    # OpenSSL Version
    try:
        openssl_version = sys.argv[3]
    except IndexError:
        openssl_version = '1.1.1b'
    print('OpenSSL Version:', openssl_version)

    # Load templates
    with open('Dockerfile.in', 'r') as dockerfile_template_file:
        dockerfile_template = Template(dockerfile_template_file.read())
    with open('.circleci/config.yml.in', 'r') as circleci_config_template_file:
        circleci_config_template = Template(circleci_config_template_file.read())
    with open('Readme.md.in', 'r') as readme_template_file:
        readme_template = Template(readme_template_file.read())

    # Create Dockerfiles and Meson cross file generators
    targets = []
    for api_level in api_levels:
        for architecture in architectures:
            if architecture in ('arm64', 'x86_64') and int(api_level) < 21:
                continue
            name = 'android-{}-{}'.format(api_level, architecture)
            target = {
                'name': name,
                'api_level': api_level,
                'architecture': architecture,
                'triple': get_triple(architecture),
            }
            targets.append(target)
            
            # Prepare directory
            directory_path = pathlib.Path(name)
            dockerfile_path = directory_path / 'Dockerfile'
            directory_path.mkdir(exist_ok=True)

            # Generate Dockerfile    
            print('Generating', dockerfile_path)
            with open(str(dockerfile_path), 'w') as dockerfile:
                dockerfile.write(dockerfile_template.render(
                    openssl_version=openssl_version,
                    **target,
                ))

            # Copy Meson cross file generator
            meson_cross_path = pathlib.Path(
                'generate-android-meson-cross-file.py')
            shutil.copyfile(
                str(meson_cross_path),
                str(directory_path / meson_cross_path))

    # Create CircleCI config
    with open('.circleci/config.yml', 'w') as circleci_config_file:
        circleci_config_file.write(circleci_config_template.render(
            targets=[target['name'] for target in targets],
        ))

    # Create readme
    with open('Readme.md', 'w') as readme_file:
        readme_file.write(readme_template.render(
            openssl_version=openssl_version,
            targets=targets,
        ))

if __name__ == '__main__':
    main()

