# Evaluates the supplied globals for each module in ModDict after calling each supplied function.
# Example usage is as follows:
###
# import Module1 as Module1
# import Module2 as Module2
# import makeFunctionAndGlobalDict as mfgd
# import evaluateGlobals as eg
# ModDict = {
#     'Module1': mfgd.makeFunctionAndGlobalDict( ['mod1Function1','mod1Function2'] , ['mod1global1','mod1global2','mod1global3'] )
#     'Module2': mfgd.makeFunctionAndGlobalDict( ['mod2Function1'] , ['mod2global1','mod2global2','mod2global3','mod2global4'] )
# }
# resultDict = eg.evaluateGlobals(ModDict,locals())
###
# Requires: Modules can't have the same name. Two globals for a given module can't have the same name.
#           Functions must be able to be called on their respective module. Globals must
#           be defined in their respective modules.
# Returns: Returns [resultDict], which is a dictionary whose keys are the modules that were passed
#          through modDict and the values are dictionaries containing the values for the specified globals
# Note: Must pass in globals() as second argument to insure that all imports that have been done are accessible
#       by the evaluateGlobals module

# Called by runTest

def testEvaluateGlobals(ModDict, oldLocs):
    resultDict = dict()

    for mod, funcGlobDict in ModDict.items():

        # print('Mod: ' + mod)
        # print('Func Glob Dict: ' + str(funcGlobDict))
        # print('Globals: ' + str(globals()))
        # print('Old Locs: ' +  str(oldLocs))
        # print(oldLocs[mod])
        newMod = oldLocs[mod]

        tempDict = dict()
        for function in funcGlobDict['functionList']:
            newStrLst = function.split('(', 1)
            s = newStrLst[1][0:-1]
            if len(s) == 0:
                getattr(newMod, newStrLst[0])()
            else:
                getattr(newMod, newStrLst[0])(s)
        for glob in funcGlobDict['globalList']:
            tempDict[glob] = getattr(newMod,glob)

        resultDict[mod] = tempDict

        # print(tempDict)

        # # Initializing string of execution
        # stringexec = ''
        #
        # # Calling all functions and assigning all globals
        # for function in funcGlobDict['functionList']:
        #     stringexec += mod + '.' + function + '\n'
        # for glob in funcGlobDict['globalList']:
        #     stringexec += glob + '=' + mod + '.' + glob + '\n'
        #
        # # Initializing location
        # loc = {}
        #
        # # Executing string of execution with current globals and storing resulting globals in loc
        # exec(stringexec, oldLocs, loc)
        #
        # # Storing the module-variable pair [mod],[loc] into the dictionary [resultDict]
        # resultDict[mod] = loc

    return resultDict


def __main__():
    from functionsAndGlobals import functionsAndGlobals
    # TODO: Import modules to be tested
    # Note: Even though it says the modules are unused, these imports are vital for runTest to work properly.
    # Their information gets passed into runTest through locals()
    import BSSN.BrillLindquist as BrillLindquist
    import BSSN.ShiftedKerrSchild as ShiftedKerrSchild
    import BSSN.StaticTrumpet as StaticTrumpet
    import BSSN.UIUCBlackHole as UIUCBlackHole

    # TODO: Modules that need to be imported to pre-initialize module and their function calls
    # None

    # TODO: Create lists of globals to calculate
    CartGlobalList = ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']
    SphGlobalList = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

    # TODO: Create Module dictionary based on imported modules, functions to initialize the modules, and globals
    # IMPORTANT: The name of the modules in ModDicT MUST have the same name as the imported module.
    # Example: If you say 'import MyModules.Module1 as M1', then ModDict should have the entry 'M1',not 'Module1'.
    ModDict = {
        'BrillLindquist': functionsAndGlobals(['BrillLindquist(ComputeADMGlobalsOnly = True)'], CartGlobalList),

        'ShiftedKerrSchild': functionsAndGlobals(['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)'],
                                                 SphGlobalList),

        'StaticTrumpet': functionsAndGlobals(['StaticTrumpet(ComputeADMGlobalsOnly = True)'], SphGlobalList),

        'UIUCBlackHole': functionsAndGlobals(['UIUCBlackHole(ComputeADMGlobalsOnly = True)'], SphGlobalList)
    }

    resultDict = testEvaluateGlobals(ModDict, locals())
    print("Original Result Dict: \n\t{'BSSN_T4UUmunu_vars': {'rho': rho, 'S': S, 'sD': [sD0, sD1, sD2], 'sDD': [[sDD00, sDD01, sDD02], [sDD01, sDD11, sDD12], [sDD02, sDD12, sDD22]]}}")
    print('Result Dict: \n\t' + str(resultDict))


if __name__ == '__main__':
    __main__()
