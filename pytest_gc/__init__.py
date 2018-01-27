import os


class PluginLoader:
    @staticmethod
    def pytest_addoption(parser):
        parser.addoption('--gc-disable', action='store_true',
                         help='Disable automatic garbage collection')
        parser.addoption('--gc-threshold', nargs='+', type=int,
                         help='Set the garbage collection thresholds')
        parser.addoption('--gc-scope', help='Set the scope for gc fixtures')

    @staticmethod
    def pytest_configure(config):
        if any(map(config.getoption, ['gc_disable', 'gc_threshold'])):
            scope = config.getoption('gc_scope')
            if scope:
                os.environ['gc_scope'] = scope
            from pytest_gc import plugin
            config.pluginmanager.register(plugin)
