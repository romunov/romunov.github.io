title: Lintering using tox ignores Python version
date: 2023-11-10 09:52
tags: python, tox, lintering, fedora, venv
keywords: python, tox, lintering, fedora, venv
category: HowTo
author: Roman Luštrik
summary: How I figured out how tox is assuming the wrong virtual environment
lang: en
status: published

When trying to run linters using `tox`, it would keep use Python 3.11 to run. But this isn't what's defined in my project configuration that says it should be Python versions between and including 3.8 and 3.10 nor the version used in my virtual environment.

```python
➜ tox -e linters
...
Processing ./.tox/.tmp/....tar.gz
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done

ERROR: Package 'mypackage' requires a different Python: 3.11.6 not in '<3.11,>=3.8'
```

The specific configuration (`tox.ini`, `setup.cfg` and `pyproject.toml`) worked for others and testing server, but not for me, so I started poking around my system. The first clue was when I checked `tox --version` which said 4.11, BUT, it was from folder `.../python3.11/site-packages`. When I tried to remove the global version using `pip uninstall tox`, pip complained that this isn't possible because the package might have been installed using the system's package manager. Sure enough, after `sudo dnf remove tox` and installation of `tox` in the local environment, lintering now goes through.