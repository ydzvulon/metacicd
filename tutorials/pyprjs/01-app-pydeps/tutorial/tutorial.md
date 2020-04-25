# Python Sample App Tutorial

## Introduction

- [step_00_poc](../step_00_poc/README.md)
Initial Idea and one python file implemtation
prints list of loaded modules

- [step_01_dirty_test_readme](../step_01_dirty_test_readme/README.md)
Basic test from cli added on first step
Readme with instructions, --test command

- [step_02_task_actions](../step_02_task_actions/README.md)
Added task repo actions, now we can interact with repo using `task test`

## Python Version And Modules Management

> [step_03_venv_pytest](../step_03_venv_pytest/README.md)
**Python Versions And Environment Management Dev Environment Testion**

After basic implementation and basic test, to move forward to python test
package pytest we need to setup virtual environment or venv.
There are couple of tools that can assist with the subject,
most of them are `module: venv` based or pypi or setuptools.

For simple and robus usage we choose 
conda+pip approach under task-actions cover, 
- cross os compatibilty,
- python version management
- virtual environment (transient and persistent) management
- precompiled binaries
- setup tools compatible

We will: 
- create manually venv using conda [README](../step_03_venv_pytest/README.md)
- install pytest package in this venv, add to requirements-dev.txt
- move test to test file according to pytest convention
- update `task test` entrypoint to use `pytest pydeps/test_pydeps.py -s`


So lets create our venv, don't rush to command line,
let's open Taskfile.yml, and add venv-install command
Now run
`task venv-install`


