import getpass


def analize():
    import sys
    return {'modules.loaded.list': set(sys.modules.keys())}


def main():
    print("Analizing Interpreter and Virtual Environment")
    import pprint
    report = analize()
    print(pprint.pformat(report))
    print(f"Loaded Modules Count: {len(report['modules.loaded.list'])}")
    print(f"Hello from pydeps to {getpass.getuser()}")


def test():
    print("=== test:test started ===")
    report = analize()
    loaded = report['modules.loaded.list']
    assert 'getpass' in loaded, \
        f'Missing module getpass. Not found in list of {len(loaded)} modules'
    print(f"Success found getpass in list of {len(loaded)} modules")
    print("=== test:test passed ===")


if __name__ == "__main__":
    import sys
    if '--test' in sys.argv:
        test()
    else:
        main()
