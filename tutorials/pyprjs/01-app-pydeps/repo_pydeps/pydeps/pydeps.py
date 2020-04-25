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


if __name__ == "__main__":
    import sys
    if '--test' in sys.argv:
        print("--test depricated use pytest pydeps instead")
    else:
        main()
