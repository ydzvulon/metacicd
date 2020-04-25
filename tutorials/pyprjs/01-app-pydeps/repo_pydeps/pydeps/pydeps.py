import getpass


def analize():
    import sys
    return {'modules.loaded.list': set(sys.modules.keys())}


def main():
    print(f"Hello from pydeps to {getpass.getuser()}")
    print("Analizing Interpreter and Virtual Environment")
    import pprint
    res = analize()
    print(pprint.pformat(res))


if __name__ == "__main__":
    main()
