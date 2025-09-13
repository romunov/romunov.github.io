Title: Insert changes into deep commits
Date: 2019-06-14
Category: HowTo
Tags: git, version control, rebase, fixup
Slug: insert-changes-into-deep-commits
Authors: Roman Luštrik
Summary: A quick guide on how to do a fixup, inserting changes into a "deep" commit

Have you ever committed a branch and review addressed issues from all commits? This post will address the issue of making changes at the top of the commit tree and then committing them deep to their respective commits.

A snapshot of the situation is illustrated in the below code chunk.

```
romunov@mucek:~/Documents/fixme$ git log
commit 1f78688a40598552262af08598fb4eb256421df8 (HEAD -> master)
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:47 2019 +0200

    Add file3

commit f7defe93b96436047988e9e5d943f22c9e136ad4
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:34 2019 +0200

    Add file2

commit 27a395f1f8878d83b8fc03629f1ef455f56db616
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:16 2019 +0200

    Add file1

commit 3fa086c62d4cf0041169a50946e0cc428fcc90d8
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:21:55 2019 +0200

    welcome

romunov@mucek:~/Documents/fixme$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   file1.txt
    modified:   file2.txt
    modified:   file3.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

I will show you how to iteratively make commits of files, hiding the rest of the uncommited changes, pushing those added files to the appropriate commit and then rinse and repeat until all the changes are done.

Starting from scratch, let's create a folder called `fixme` that will contain 4 files. Each file will reside in its own commit.

```
romunov@mucek:~/Documents$ mkdir fixme
romunov@mucek:~/Documents$ cd fixme/
romunov@mucek:~/Documents/fixme$ git init
Initialized empty Git repository in /home/romunov/Documents/fixme/.git/

romunov@mucek:~/Documents/fixme$ echo "welcome" > welcome.txt
romunov@mucek:~/Documents/fixme$ git add welcome.txt
romunov@mucek:~/Documents/fixme$ git commit -m "welcome"
[master (root-commit) 3fa086c] welcome
 1 file changed, 1 insertion(+)
 create mode 100644 welcome.txt

romunov@mucek:~/Documents/fixme$ echo "txt in file1" > file1.txt
romunov@mucek:~/Documents/fixme$ git add file1.txt
romunov@mucek:~/Documents/fixme$ git commit -m "Add file1"
[master 27a395f] Add file1
 1 file changed, 1 insertion(+)
 create mode 100644 file1.txt

romunov@mucek:~/Documents/fixme$ echo "txt in file2" > file2.txt
romunov@mucek:~/Documents/fixme$ git add file2.txt
romunov@mucek:~/Documents/fixme$ git commit -m "Add file2"
[master f7defe9] Add file2
 1 file changed, 1 insertion(+)
 create mode 100644 file2.txt

romunov@mucek:~/Documents/fixme$ echo "txt in file3" > file3.txt
romunov@mucek:~/Documents/fixme$ git add file3.txt
romunov@mucek:~/Documents/fixme$ git commit -m "Add file3"
[master 1f78688] Add file3
 1 file changed, 1 insertion(+)
 create mode 100644 file3.txt

romunov@mucek:~/Documents/fixme$ git status
On branch master
nothing to commit, working tree clean

romunov@mucek:~/Documents/fixme$ git log
commit 1f78688a40598552262af08598fb4eb256421df8 (HEAD -> master)
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:47 2019 +0200

    Add file3

commit f7defe93b96436047988e9e5d943f22c9e136ad4
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:34 2019 +0200

    Add file2

commit 27a395f1f8878d83b8fc03629f1ef455f56db616
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:16 2019 +0200

    Add file1

commit 3fa086c62d4cf0041169a50946e0cc428fcc90d8
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:21:55 2019 +0200

    welcome
```

Now let's create some changes to all files.

```
romunov@mucek:~/Documents/fixme$ echo "another txt in file 1" >> file1.txt
romunov@mucek:~/Documents/fixme$ echo "another txt in file 2" >> file2.txt
romunov@mucek:~/Documents/fixme$ echo "another txt in file 3" >> file3.txt
romunov@mucek:~/Documents/fixme$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   file1.txt
    modified:   file2.txt
    modified:   file3.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Let's push each change for `file1`, `file2` and `file3` to its corresponding commit.
The steps taken are
1. add specific file
2. push to specific commit using `--fixup`
3. hide uncommited changes using `git stash`
4. rebase
5. recall uncommited changes using `git stash apply` and go from 1.

Some comments about the code are inline.

```
romunov@mucek:~/Documents/fixme$ git add file1.txt
# To get hash of a commit, see above or use `git log`.
romunov@mucek:~/Documents/fixme$ git commit --fixup=27a395f1f8878d83b8fc03629f1ef455f56db616
[master f24f11b] fixup! Add file1
 1 file changed, 1 insertion(+)

 # Hide uncommited changes.
romunov@mucek:~/Documents/fixme$ git stash
Saved working directory and index state WIP on master: f24f11b fixup! Add file1

# Notice that the new fixedup commit is on top.
romunov@mucek:~/Documents/fixme$ git log
commit f24f11b7ca983be10b2cf3f477ebd649542d3ba2 (HEAD -> master)
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:24:14 2019 +0200

    fixup! Add file1

commit 1f78688a40598552262af08598fb4eb256421df8
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:47 2019 +0200

    Add file3

commit f7defe93b96436047988e9e5d943f22c9e136ad4
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:34 2019 +0200

    Add file2

commit 27a395f1f8878d83b8fc03629f1ef455f56db616
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:16 2019 +0200

    Add file1

commit 3fa086c62d4cf0041169a50946e0cc428fcc90d8
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:21:55 2019 +0200

    welcome

# Rebase. Make sure you go back in time (HEAD~X) so that you cover them
# actual commit message. Use autosquash so you don't have to manually
# squash it in the next window.    
romunov@mucek:~/Documents/fixme$ git rebase -i HEAD~4 --autosquash
```

<img src="{static}images/fixup_file1.jpg" width="500" class="center">

```
Successfully rebased and updated refs/heads/master.

# The top "fixup" commit has been squashed with commit titled
# "Add file1".
romunov@mucek:~/Documents/fixme$ git log
commit 95e48ac32aa93256aa248f8077c293bf16b8d911 (HEAD -> master)
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:47 2019 +0200

    Add file3

commit 7e881feb91bdf326a3af985697d7837283a2ba12
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:34 2019 +0200

    Add file2

commit 6d52f8818d587fded3910dd688f4fe6a762fd7dd
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:22:16 2019 +0200

    Add file1

commit 3fa086c62d4cf0041169a50946e0cc428fcc90d8
Author: Roman Luštrik <romunov@gmail.com>
Date:   Thu Jun 13 16:21:55 2019 +0200

    welcome
```

We now bring back uncommited changes...

```
romunov@mucek:~/Documents/fixme$ git stash apply
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   file2.txt
    modified:   file3.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

... and go through the same process again.

```
romunov@mucek:~/Documents/fixme$ git add file2.txt
romunov@mucek:~/Documents/fixme$ git commit --fixup=7e881feb91bdf326a3af985697d7837283a2ba12
[master d3f6227] fixup! Add file2
 1 file changed, 1 insertion(+)

romunov@mucek:~/Documents/fixme$ git stash
Saved working directory and index state WIP on master: d3f6227 fixup! Add file2
romunov@mucek:~/Documents/fixme$ git rebase -i HEAD~4 --autosquash
```

<img src="{static}images/fixup_file2.jpg" width="500" class="center">

```
Successfully rebased and updated refs/heads/master.
```

The final file should go into the top commit, so we can just use `git commit --amend`.

```
# Bring up uncommited changes.
romunov@mucek:~/Documents/fixme$ git stash apply
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   file3.txt

no changes added to commit (use "git add" and/or "git commit -a")
romunov@mucek:~/Documents/fixme$ git add file3.txt
romunov@mucek:~/Documents/fixme$ git commit --amend
[master c251243] Add file3
 Date: Thu Jun 13 16:22:47 2019 +0200
 1 file changed, 2 insertions(+)
 create mode 100644 file3.txt
```

You should now have a clean workspace with changes in their respective commits.

**CAVEAT**
Do this only on private branches, unless you are the only person working on `master` branch. If you force push these changes, your collaborators may throw you off of the nearest bridge.
