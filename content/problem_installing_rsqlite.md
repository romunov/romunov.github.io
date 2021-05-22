title: Problem compiling RSQLite from source
date: 2021-05-22 08:53
tags: R, RSQLite
keywords: compiling, problem, R, RSQLite, reinstall, fedora, linux
category: HowTo
slug: problem-compiling-rsqlite-from-source
author: Roman Luštrik
summary: Compiling RSQLite from source on Fedora failed. Reinstalled Rcpp seemed to do the trick.
lang: en
status: published

When I tried to compile RSQLite from source on Fedora 34, I was awaited by this error message.

```bash
Error installing package 'RSQLite':
===================================
* installing to library ‘/.../renv/staging/1’
* installing *source* package ‘RSQLite’ ...
** package ‘RSQLite’ successfully unpacked and MD5 sums checked
** using staged installation
** libs
g++ -m64 -std=gnu++11 -I"/usr/include/R" -DNDEBUG -I. -Ivendor
-DRSQLITE_USE_BUNDLED_SQLITE -DSQLITE_ENABLE_RTREE
-DSQLITE_ENABLE_FTS3 -DSQLITE_ENABLE_FTS3_PARENTHESIS -DSQLITE_ENABLE_FTS5
-DSQLITE_ENABLE_JSON1 -DSQLITE_ENABLE_STAT4 -DSQLITE_SOUNDEX
-DRCPP_DEFAULT_INCLUDE_CALL=false -DRCPP_USING_UTF8_ERROR_STRING
-DBOOST_NO_AUTO_PTR -DSQLITE_MAX_LENGTH=2147483647 -DHAVE_USLEEP=1
-I'/../R/x86_64-redhat-linux-gnu-library/4.0/plogr/include'
-I'/.../renv/staging/1/Rcpp/include' -I/usr/local/include  
-fvisibility=hidden -fpic  -O2 -flto=auto -ffat-lto-objects -fexceptions
-g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,
-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS
-specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong
-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64  -mtune=generic
-fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection  
-c DbColumn.cpp -o DbColumn.o
In file included from pch.h:1,
                 from DbColumn.cpp:1:
RSQLite.h:9:10: fatal error: Rcpp.h: No such file or directory
    9 | #include <Rcpp.h>
      |          ^~~~~~~~
compilation terminated.
make: *** [/usr/lib64/R/etc/Makeconf:181: DbColumn.o] Error 1
ERROR: compilation failed for package ‘RSQLite’
```

To make it work, I think reinstalling `Rcpp` package made the difference. I have been upgrading my Fedora lately (bumping from F33 to F34), which leads me to believe that there may have been a change in compiler versions. What I would imagine is that something didn't play well together.
