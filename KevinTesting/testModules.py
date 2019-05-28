import Module1 as M1
import Module2 as M2
import sympy as sp
import makeFunctionAndGlobalDict as mfgd


# def getGlobalsDict(oldGlobals,newGlobals):    
#     value = dict()

#     for key in newGlobals:
#         #if not (key in oldGlobals):
#         value[key] = newGlobals[key]
#     return value

# Named tuple dictionary: function list, 


ModDict = {
    'M1': mfgd.makeFunctionAndGlobalDict(['Module1(True)'],['x','y','z']),
    'M2': mfgd.makeFunctionAndGlobalDict(['Module2(200,40)'],['x2','y2'])
}


resultDict = dict()
 
for mod,funcGlobDict in ModDict.items():

    # Initializing string of execution
    stringexec = ''

    # Calling all functions and assigning all globals
    for function in funcGlobDict['functionList']:
        stringexec += mod + '.' + function + '\n'
    for glob in funcGlobDict['globalList']:
        stringexec += glob + '=' + mod + '.' + glob + '\n'

    # Assigning newGlobals
    stringexec += 'newGlobals = globals()'

    # Initializing location 
    loc = {}

    # Executing string of execution with current globals
    # and storing resulting globals in loc
    exec(stringexec,globals(),loc)

    # Deleting self-reference of newGlobals
    del loc['newGlobals']
        
    resultDict[mod] = loc
    
print(resultDict)

print(sp.factor(resultDict['M1']['x']+resultDict['M1']['y']+resultDict['M1']['z']))
        
    
    

# M1.Module1(True)
# x2=M1.x1
# y2=M1.y1
# glob = globals()



