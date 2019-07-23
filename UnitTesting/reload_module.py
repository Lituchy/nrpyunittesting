import sys

# reload_module takes in a module [mod]. It deletes the attributes of [mod] and then reloads [mod] to ensure that
# a fresh module instance has been created.


def reload_module(mod):

    # Loop through all attributes of [mod], deleting those who don't begin with '__'
    for attr in dir(mod):
        if attr[0:2] != '__':
            delattr(mod, attr)

    # Python 2.x
    if sys.version_info[0] == 2:
        reload(mod)
    # Python 3.x, x <= 3
    elif sys.version_info[1] <= 3:
        import imp
        imp.reload(mod)
    # Python 3.x, x >= 4
    else:
        import importlib
        importlib.reload(mod)