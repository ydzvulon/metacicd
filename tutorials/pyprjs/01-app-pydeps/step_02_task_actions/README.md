# Applications Pydeps

## TD;DR

This sample application with show some information
about current virtual environment and loaded libraries

It will have cli inteface `./pydes --info`

## Run

> In repo_pydeps dir run

```bash
python pydeps/pydeps.py --info
```
> Output

    ...
     'zope'}}
    Loaded Modules Count: 77
    Hello from pydeps ...

## Test

> In repo_pydeps dir run

```bash
python pydeps/pydeps.py --test
```

> Output

    === test:test started ===
    Success found getpass in list of 76 modules
    === test:test passed ===
