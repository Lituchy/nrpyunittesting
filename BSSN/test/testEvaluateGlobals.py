import makeFunctionAndGlobalDict as mfgd
import evaluateGlobals as eg

import BSSN.BrillLindquist as bl
import BSSN.ShiftedKerrSchild as sks
import BSSN.StaticTrumpet as st
import BSSN.UIUCBlackHole as ubh

SphGlobalList = ['alphaSph', 'betaSphU', 'BSphU','gammaSphDD', 'KSphDD']

ModDict = {
    'bl': mfgd.makeFunctionAndGlobalDict( ['BrillLindquist(ComputeADMGlobalsOnly = True)'] , ['alphaCart','betaCartU','BCartU', 'gammaCartDD','KCartDD'] ),
    
    'sks': mfgd.makeFunctionAndGlobalDict( ['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)'] , SphGlobalList ),
    
    'st': mfgd.makeFunctionAndGlobalDict( ['StaticTrumpet(ComputeADMGlobalsOnly = True)'] , SphGlobalList ),
    
    'ubh': mfgd.makeFunctionAndGlobalDict( ['UIUCBlackHole(ComputeADMGlobalsOnly = True)'] , SphGlobalList )
}

resultDict = eg.evaluateGlobals(ModDict,globals())

for key,valueDict in resultDict.items():
    print('\n#####' + key + '#####\n')
    for val,expr in valueDict.items():
        print(key + ' ' + val + ':')
        print(expr)
        print
    
