Docker images for Continuous Integration builds of RAWRTC.

## Targets

Docker files for specific target platforms reside in the following branches:

- Common **Linux x64** distributions are located in the
  [host/linux-x64][host/linux-x64] branch.
- The **Linux ARMv6** target is located in the
  [cross/linux-armv6][cross/linux-armv6] branch. Builds for this target should
  run on the popular Raspberry Pi 1 and Zero devices.
- The **Linux ARMv7** target is located in the
  [cross/linux-armv7][cross/linux-armv7] branch. Builds for this target should
  run on the similarly popular Raspberry Pi 2 and 3 devices.
- The **Windows x86** target resides in the
  [cross/windows-x86][cross/windows-x86] branch.
- The **Windows x64** target resides in the
  [cross/windows-x64][cross/windows-x64] branch.
- **Android** targets for various API levels and architectures reside in the
  [cross/android][cross/android] branch.

## Other Branches

A couple of further branches exist that do not contain Docker files for target
platforms:

- [master][master] only contains this readme.
- [cross/base][cross/base] contains a dependency Docker file for
  cross-compilation targets.
- [test-project][test-project] contains a simple test project that is being
  used by CircleCI to verify that a newly built image is working as intended.

## Docker Hub

The images of this repository are built automatically by CircleCI and pushed
to the following two Docker Hub repositories:

- [rawrtc/ci-image][dockerhub-ci-image] contains images of host targets.
- [rawrtc/cross-build][dockerhub-cross-build] contains images of
  cross-compilation targets.



[host/linux-x64]: ../../tree/host/linux-x64
[cross/linux-armv6]: ../../tree/cross/linux-armv6
[cross/linux-armv7]: ../../tree/cross/linux-armv7
[cross/windows-x86]: ../../tree/cross/windows-x86
[cross/windows-x64]: ../../tree/cross/windows-x64
[cross/android]: ../../tree/cross/android
[master]: ../../tree/master
[cross/base]: ../../tree/cross/base
[test-project]: ../../tree/test-project
[dockerhub-ci-image]: https://hub.docker.com/r/rawrtc/ci-image/tags
[dockerhub-cross-build]: https://hub.docker.com/r/rawrtc/cross-build/tags

