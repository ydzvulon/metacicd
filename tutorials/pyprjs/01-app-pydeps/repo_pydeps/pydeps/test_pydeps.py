import pydeps


def assert_getpass_is_loaded(report):
    loaded = report['modules.loaded.list']
    assert ('getpass', '') in loaded, \
        f'Missing module getpass. Not found in list of {len(loaded)} modules'
    print(f"Success found getpass in list of {len(loaded)} modules")


def assert_pip_report(report):
    assert 'requests' in report['pip_freeze_loaded']


def test__pydeps__analize():
    report = pydeps.analize()
    assert_getpass_is_loaded(report)
    assert_pip_report(report)

