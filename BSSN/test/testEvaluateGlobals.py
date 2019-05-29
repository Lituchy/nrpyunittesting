import makeFunctionAndGlobalDict as mfgd
import evaluateGlobals as eg
import getVariableDimension as getVarDim
import moduleDictToList as modDictToLst
import listToValueList as lstToValLst

import BSSN.BrillLindquist as BrillLindquist
import BSSN.ShiftedKerrSchild as ShiftedKerrSchild
import BSSN.StaticTrumpet as StaticTrumpet
import BSSN.UIUCBlackHole as UIUCBlackHole

import sympy as sp

import trustedValuesDict as trustedDict


CartGlobalList = ['alphaCart','betaCartU','BCartU', 'gammaCartDD','KCartDD']
SphGlobalList = ['alphaSph', 'betaSphU', 'BSphU','gammaSphDD', 'KSphDD']

ModDict = {
    'BrillLindquist': mfgd.makeFunctionAndGlobalDict( ['BrillLindquist(ComputeADMGlobalsOnly = True)'] , CartGlobalList ),
    
    'ShiftedKerrSchild': mfgd.makeFunctionAndGlobalDict( ['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)'] , SphGlobalList ),
    
    'StaticTrumpet': mfgd.makeFunctionAndGlobalDict( ['StaticTrumpet(ComputeADMGlobalsOnly = True)'] , SphGlobalList ),
    
    'UIUCBlackHole': mfgd.makeFunctionAndGlobalDict( ['UIUCBlackHole(ComputeADMGlobalsOnly = True)'] , SphGlobalList )
}




resultDict = eg.evaluateGlobals(ModDict,globals())

tvDict = dict()

for mod in resultDict:

    (varList,nameList) = modDictToLst.moduleDictToList(resultDict[mod])
    numList = lstToValLst.listToValueList(mod,varList,True)
    modDict = dict()
    for num, name in zip(numList,nameList):
        modDict[name] = num
    tvDict[mod] = modDict
    
for mod, vals in tvDict.items():
    print(mod + ':\n' + str(vals) + '\n')

print('Result:\n' + str(tvDict['UIUCBlackHole']) + '\n')
print('Trusted:\n' + str(trustedDict.tvDict['UIUCBlackHole']))

    
print(cmp(tvDict['UIUCBlackHole'],trustedDict.tvDict['UIUCBlackHole']))

print(set(tvDict))
    

#     valueList = lstToValLst.listToValueList(mod,lst,True)
#     print(mod + ': ')
#     print(str(valueList) + '\n')

# print(resultDict['BrillLindquist']['KCartDD'])






