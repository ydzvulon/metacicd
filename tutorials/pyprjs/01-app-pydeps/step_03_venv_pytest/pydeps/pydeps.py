import sys
import getpass
import subprocess


def analize():
    report = {}
    report.update(analize_loaded())
    report.update(analize_pip_list())
    report.update(analize_pip_freeze())
    return report


def analize_loaded():
    loaded = set(it for it in sys.modules.keys() if not it.startswith('_'))
    return {'modules.loaded.list': loaded}


def analize_pip_list():
    out = subprocess.check_output(
        f'{sys.executable} -m pip list', 
        shell=True).decode()
    return {'modules.pip-list.list': out}


def analize_pip_freeze():
    out = subprocess.check_output(
        f'{sys.executable} -m pip freeze', 
        shell=True).decode()
    return {'modules.pip-freeze.list': out}


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
