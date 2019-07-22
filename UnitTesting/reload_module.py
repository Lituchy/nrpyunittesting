import sys

# [reload_module] takes in a module [module] and calls the python reload function on the module, using the proper
# library based on the version of python being used. It then returns the reloaded module.


def reload_module(module):
    # Python 2
    if sys.version_info[0] == 2:
        reload(module)
    # Python 3.x, x <= 3
    elif sys.version_info[1] <= 3:
        import imp
        imp.reload(module)
    # Python 3.x, x >= 4
    else:
        import importlib
        importlib.reload(module)

    return module
