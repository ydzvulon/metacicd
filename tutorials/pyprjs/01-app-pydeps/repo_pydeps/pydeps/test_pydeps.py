import pydeps

def test__pydeps__analize():
    print("=== test:test started ===")
    report = pydeps.analize()
    loaded = report['modules.loaded.list']
    assert 'getpass' in loaded, \
        f'Missing module getpass. Not found in list of {len(loaded)} modules'
    print(f"Success found getpass in list of {len(loaded)} modules")
    print("=== test:test passed ===")
