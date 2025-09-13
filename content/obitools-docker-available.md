Title: Docker image for OBITools (1.2.13) available
Date: 2019-06-15
Category: OpenSource
Tags: python, bioinformatics, docker, obitools, dockerhub
Slug: docker-image-of-obitools-available
Authors: Roman Luštrik
Summary: Docker image for OBITools available

In order to aid in making bioinformatics pipelines more reproducible, I have put together a [docker image which houses OBITools](https://hub.docker.com/r/romunov/obitools). OBITools is a software bundle which helps you analyze NGS data. See [their website](https://git.metabarcoding.org/obitools/obitools/wikis/home) for more information.

Having obitools housed in a docker image enables us to easily migrate or communicate our workflow. Here is a short representation of how one can call functions from the bundle using Python's `docker` package.

First, prepare some boilerplate stuff to have the container ready as a Python variable.

```
import docker
from docker.errors import NotFound

client = docker.from_env()

# Create or start docker container named 'obitools'.
try:
    obt = client.containers.get('obitools')
    if obt.status == 'exited':
        print('Starting container obitools.')
        obt.start()
    else:
        print('Container obitools ready.')
except NotFound:
    print('Creating container obitools.')
    obt = client.containers.run(
        image='romunov/obitools:1.2.13',
        name='obitools',
        # This maps my local wolfdata to /data in container
        volumes={'/home/romunov/wolfdata': {'bind': '/data', 'mode': 'rw'}},
        tty=True, detach=True
        )
```

And then run the command

```
score_min = 40
reads_r = "wolf_R.fastq"
reads_f = "wolf_F.fastq"
output = "wolf.fastq"
wolf = obt.exec_run(tty=True, workdir='/data', cmd=f'illuminapairedend --score-min={score_min} -r {reads_r} {reads_f} > {output}')
```

Command `illuminapairedend --score-min=40 -r wolf_R.fastq wolf_F.fastq > wolf.fastq` would be sent to the docker container and output would be located in `/home/romunov/wolfdata` (see the first code chunk, specifically study the argument `volumes`).
