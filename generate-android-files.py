#!/usr/bin/env python3
import pathlib
import shutil
import sys

from jinja2 import Template


def main():
    # NDK Revision
    try:
        ndk_revision = sys.argv[1]
    except IndexError:
        ndk_revision = '18b'
    print('NDK Revision:', ndk_revision)

    # NDK APIs
    try:
        ndk_apis = sys.argv[2]
    except IndexError:
        ndk_apis = [
            '21',  # Android 5.0/5.1
            '27',  # Android 8.1
        ]
    else:
        ndk_apis = [api.strip() for api in ndk_apis.split(',')]
    print('NDK APIs:', ndk_apis)

    # Architectures
    try:
        architectures = sys.argv[2]
    except IndexError:
        architectures = [
            'arm',
            'arm64',
            #'x86',
            #'x86_64',
        ]
    else:
        architectures = [arch.strip() for arch in architectures.split(',')]
    print('Architectures:', architectures)

    # Load templates
    with open('Dockerfile.in', 'r') as dockerfile_template_file:
        dockerfile_template = Template(dockerfile_template_file.read())
    with open('.circleci/config.yml.in', 'r') as circleci_config_template_file:
        circleci_config_template = Template(circleci_config_template_file.read())
    with open('Readme.md.in', 'r') as readme_template_file:
        readme_template = Template(readme_template_file.read())

    # Create Dockerfiles and Meson cross file generators
    targets = []
    for ndk_api in ndk_apis:
        for architecture in architectures:
            name = 'android-{}-{}'.format(ndk_api, architecture)
            target = {
                'name': name,
                'ndk_api': ndk_api,
                'architecture': architecture,
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
                    ndk_revision=ndk_revision,
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
            ndk_revision=ndk_revision,
            targets=targets,
        ))

if __name__ == '__main__':
    main()

