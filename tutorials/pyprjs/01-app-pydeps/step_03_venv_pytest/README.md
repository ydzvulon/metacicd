# Applications Pydeps

## TD;DR

This sample application with show some information
about current virtual environment and loaded libraries

It will have cli inteface `./pydeps/pydeps.py --info`

## Environment Preparation

```bash
conda create -y -n pydeps36 python=3.6
conda activate pydeps36
# export PATH=$PATH:conda env list | grep pydeps36
conda info | grep 'active environment'
# active environment : pydeps36

# assert that you in venv:

conda install -y pytest
```

> Now we need run other actions within virtual environment
`conda activate pydeps36`

## Test

> In step_02_task_actions dir run

```bash
task test
```
> Output

    === test:test started ===
    Success found getpass in list of 76 modules
    === test:test passed ===

## Sample Run

> In step_02_task_actions dir run

```bash
task run
```

> Output

    ...
     'zope'}}
    Loaded Modules Count: 77
    Hello from pydeps ...
