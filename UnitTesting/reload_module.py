import sys


def reload_module(module):
    if sys.version_info[0] == 2:
        reload(module)
    elif sys.version_info[1] <= 3:
        import imp
        imp.reload(module)
    else:
        import importlib
        importlib.reload(module)