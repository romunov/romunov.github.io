title: Pimping up the new install of Fedora
date: 2022-05-07
tags: fedora, linux
keywords: linux, fedora, fedora 35, system packages
category: HowTo
slug: pimping-up-the-new-install-of-fedora
author: Roman Luštrik
summary: A few details on how to get my Fedora 35 setup up and running.
lang: en
status: published

After a fresh install of a Fedora 35, I noticed that videos and gifs were a bit slow. After a bit of searching I found [this post](https://ask.fedoraproject.org/t/fedora-34-laggy-video-playback-in-firefox/13130) which gives instructions on how to install the ffmpeg system package.

```
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

sudo dnf install ffmpeg-libs
```

Another things I also noticed is that Rstudio would no longer work because of the

```
rstudio: error while loading shared libraries: libssl.so.10: cannot open shared object file: No such file or directory
```

I suspect this was because I installed the RHEL7 (CentOS) version of the package. The error went away when I installed the RHEL8 version from [here](https://dailies.rstudio.com/rstudio/spotted-wakerobin/electron/rhel8/).
