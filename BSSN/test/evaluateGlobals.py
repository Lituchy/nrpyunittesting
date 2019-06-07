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
# resultDict = eg.evaluateGlobals(ModDict,globals())
###
# Requires: Modules can't have the same name. Two globals for a given module can't have the same name.
#           Functions must be able to be called on their respective module. Globals must 
#           be defined in their respective modules.
# Returns: Returns [resultDict], which is a dictionary whose keys are the modules that were passed 
#          through modDict and the values are dictionaries containing the values for the specified globals
# Note: Must pass in globals() as second argument to insure that all imports that have been done are accessible
#       by the evaluateGlobals module

# Called by runTest

def evaluateGlobals(ModDict,oldGlobals):

    resultDict = dict()
    
    for mod,funcGlobDict in ModDict.items():

        # Initializing string of execution
        stringexec = ''

        # Calling all functions and assigning all globals
        for function in funcGlobDict['functionList']:
            stringexec += mod + '.' + function + '\n'
        for glob in funcGlobDict['globalList']:
            stringexec += glob + '=' + mod + '.' + glob + '\n'

        # Initializing location 
        loc = {}

        # Executing string of execution with current globals and storing resulting globals in loc
        exec(stringexec,oldGlobals,loc)
        
        # Storing the module-variable pair [mod],[loc] into the dictionary [resultDict]
        resultDict[mod] = loc
        
    return resultDict
