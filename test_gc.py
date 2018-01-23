pytest_plugins = "pytester",


def test_switch(testdir):
    testdir.makepyfile("""
    import gc
    
    def test_switch():
        assert not gc.isenabled()
    """)
    testdir.runpytest().assert_outcomes(passed=1)