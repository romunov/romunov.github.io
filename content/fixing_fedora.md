title: Fixing Fedora the old fashion way
date: 2022-05-02 13:18
modified: 2022-05-02 13:18
tags: fedora, linux
keywords: upgrading, crash, reinstall
category: HowTo
slug: fixing-fedora-the-old-fashion-way
author: Roman Luštrik
summary: Brief description of content for index pages
lang: en
status: published

My regular maintenance of my Fedora instance includes doing incessant upgrading using

```bash
sudo dnf upgrade
```

which updates any possible packages and the kernel. This has worked fine until recently,
when two of my computers started freezing during the upgrading process. Usually,
I would wait about 10 minutes before hard shutting down the computer and powering back up
without any obvious detremental effects.

But a few days ago, I cycled the computer after a freeze after about a minute. When trying
to powering back up, I was welcomed by the emergency mode saying

```bash
Cannot open access to console, the root account is locked.
See sulogin(8) man page for more details.

Press Enter to continue.
```

Needless to say, anything I tried to do at this stage would not bear any fruit, resulting
in a lot of `FAILED` messages, from failure to mount `/boot/efi` to `Failed to start Load Kernel Module`.

The problem was resolved by booting into a live USB Fedora and installing a fresh install.
The only thing to watch for is to not reformat the `/home` folder. After the system was up and running,
I was welcommd by having all my setting being retained, i.e. all Firefox windows were as I left them before
the crash. When I installed Slack, all channels were loaded without going through the tedious
logging in using two-factor authentication. PyCharm also kept all the sweet settings I set.

The key to fixing the computer is just pouring copious quantities of your favorite wine. And having
a backup computer also helps.