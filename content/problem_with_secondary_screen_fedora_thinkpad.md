title: Problem when waking Fedora from sleep on a ThinkPad Carbon X1
date: 2022-07-14 11:03
tags: fedora, thinkpad, dual screen, secondary screen, sleep, wake-up
keywords: fedora, thinkpad, carbon, x1, secondary screen, sleep, wake-up
category: HowTo
slug: problem-with-secondary-screen-waking-fedora-thinkpad-carbon
author: Roman Luštrik
summary: It would appear I have solved a problem when waking up Fedora on a ThinkPad Carbon X1.
lang: en
status: published

If there's anything I really hate is booting up my system every day. Sorting windows to appropriate screens and virtual desktops is a hassle. Which is why I really love the sleep feature. The problem was, when I tried to wake the computer up, my secondary screen would not work anymore. Connection is via USB-C, the computer detects it, it's charging over it, but there is no picture. Even in settings, no secondary display was detected. This was solved by running

```bash
inxi -Fzx
```

and the picture appeared instantly. Don't ask me how this works, it's just something I tried when I ran diagnostics from [this page](https://ask.fedoraproject.org/t/dual-external-monitor-problem-with-fedora-35/19115/4).