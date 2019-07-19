from UnitTesting.reload_module import reload_module
import reference_metric as rfm

try:
    print(rfm.GammahatUDDdD)
except AttributeError:
    print('GammahatUDDdD does not exist.')

rfm.reference_metric()
print(rfm.GammahatUDDdD)

rfm = reload_module(rfm)
print(rfm.GammahatUDDdD)

reload_module(rfm)
print(rfm.GammahatUDDdD)

import reference_metric as rfm
print(rfm.GammahatUDDdD)

import reference_metric as rfm
print(rfm.GammahatUDDdD)

del globals()['rfm']

import reference_metric as rfm
print(rfm.GammahatUDDdD)

import importlib
rfm = importlib.reload(rfm)
print(rfm.GammahatUDDdD)

print(dir(rfm))

reload_module(rfm)

print('\n' + str(dir(rfm)))

for attr in dir(rfm):
    if attr[0:2] != '__':
        delattr(rfm, attr)

print(dir(rfm))

reload_module(rfm)

print(dir(rfm))

try:
    print(rfm.GammahatUDDdD)
except AttributeError:
    print('GammahatUDDdD does not exist.')

rfm.reference_metric()

print(rfm.GammahatUDDdD)

