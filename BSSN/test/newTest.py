import unittest
import sympy as sp
from mpmath import *
import random
import sys


oldMods = dict(sys.modules)

from trustedValuesDict import trustedValuesDict
import modulesToImport as mti

newMods = dict(sys.modules)

oldSet = set(oldMods)
newSet = set(newMods)

print(newSet - oldSet)

