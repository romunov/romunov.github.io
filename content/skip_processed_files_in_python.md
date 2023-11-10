title: Remember processed entities in Python
date: 2021-09-04 10:38
modified: 2021-09-04 10:38
tags: persistent storage, shelf, shelve, Python
keywords: persistent storage, shelf, shelve, Python, processing data, skip processed entity
category: HowTo
slug: remember-processed-entities-in-python
author: Roman Luštrik
summary: An off-the-shelf way to remember which entities have been processed which enables you to flow your workflow in a more intelligent manner.
lang: en
status: published

There exist not-so-edge cases when you're processing data but your code fails for some reason or another. There are many solutions around this. Complexity increases fault tolerance but also the cost of setting things up. For instance, you could create a Celery task queue or a Redis database for persistent storage to process tasks, but this can be somewhat involved. It can also not be feasible if you're working in a contained environment where installing a new package or piece of software would take a Jira ticket and days of waiting. Also, if you're doing a one-off thing, anything other than simple may be an overkill.

To remember which entities have been already processed, my initial solution included writing this information into a pickle file. Before processing an entity, I would reread the pickle file and check if the entity has been processed previously. This seems very Flintstony, so I thought I'd use the collective hive mind and asked this question on a local developer community slack channel. A bunch of solutions rushed in, including Redis and Celery, but the one that got my attention the most was the [`shelve` object](https://docs.python.org/3/library/shelve.html) used for persistent storage.

It's very easy and intuitive to work with. It's just a matter of setting up a shelf as it were and putting things on it. It's nice to tear the shelf down once you're done using it. It's even prepackaed with Python, so no additional installation of packages is needed.

Here's a small script that demonstrates the functionality. A function `run_process` processes all the files in folder. First, I add three files and process them. Then I add two more files and process the whole set of files again. Notice that the files that have already been processed are now skipped. This is the result of the script:

```
['In file1']
['In file2']
['In file3']
Skipping ./file1
Skipping ./file2
Skipping ./file3
['In file4']
['In file5']
```

The script in its entirety or see [this gist](https://gist.github.com/romunov/b79d63caa8874618e734329eaa3d6950):

```python
"""
Off the shelf way to skip already processed entities

This scripts processes files, remembers which files have been already
processed and skips them on the next run.
"""
import glob
import os
import shelve


def create_files(file_list):
    """Creates specified files on disk with boring contents."""
    for obj in file_list:
        with open(obj, mode="wt") as to_disk:
            to_disk.write(f"In {os.path.basename(obj)}")
    return None


def process_file(x):
    """Reads file and prints its contents."""
    with open(file=x, mode="rt") as in_file:
        content = in_file.readlines()
        print(content)


def list_files(path):
    """List all files in a specified path."""
    files = glob.glob(os.path.join(path, "file*"))

    return sorted(files)


# noinspection PyBroadException
def run_process(files):
    """
    Iterate through specified files and process them if not already
    done in the previous run.
    """
    for obj in files:
        try:
            key = os.path.basename(obj)
            if key not in shelf:
                process_file(x=obj)
                shelf[key] = "OK"
            else:
                print(f"Skipping {obj}")
        except Exception as e:
            print(f"Failed ({e})")

    return f"Processed {len(files)} files."


# This is a file where memories of processed files go.
CACHE_FILE = "processed.cache"

shelf = shelve.open(filename=CACHE_FILE)

create_files(file_list=["file1", "file2", "file3"])

available_files = list_files(path=".")

run_process(files=available_files)

create_files(file_list=["file4", "file5"])

available_files = list_files(path=".")

run_process(files=available_files)

# Close the shelf
shelf.close()

# Remove any files that may have been created during the execution of
# this script.
for file in available_files:
    os.unlink(file)

os.unlink(CACHE_FILE)
```
