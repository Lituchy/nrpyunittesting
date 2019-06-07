import getVariableDimension as getVarDim

# moduleDictToList takes in a module dictionary [moduleDict] and returns a tuple
# of lists; the first list [varList] is a list of sympy expressions and the second 
# list [nameList] is the respective corresponding name for each expression in [varList].
# Example: varList[0] -> r/(M+r) 
#          nameList[0] -> 'alphaSph'
# Note: Not currently equipped to deal with any tensors of rank >= 5

# Called by runTest

def moduleDictToList(moduleDict):
    
    varList = []
    nameList = []
    
    for var, exprList in moduleDict.items():
        dim = getVarDim.getVariableDimension(exprList)
        if dim == 0:
            varList.append(exprList)
            nameList.append(var)
        elif dim == 1:
            num = 0
            for i in exprList:
                varList.append(i)
                nameList.append(var + '[' + str(num) + ']')
                num += 1
        elif dim == 2:
            num1 = 0
            for lst in exprList:
                num2 = 0
                for i in lst:
                    varList.append(i)
                    nameList.append(var + '[' + str(num1) + ']' + '[' + str(num2) + ']')
                    num2 += 1
                num1 += 1
        elif dim == 3:
            num1 = 0
            for lst1 in exprList:
                num2 = 0
                for lst0 in lst1:
                    num3 = 0
                    for i in lst0:
                        varList.append(i)
                        nameList.append(var + '[' + str(num1) + ']' + '[' + str(num2) + ']' + '[' + str(num3) + ']')
                        num3 += 1
                    num2 += 1
                num1 += 1
        elif dim == 4:
            num1 = 0
            for lst2 in exprList:
                num2 = 0
                for lst1 in lst2:
                    num3 = 0
                    for lst0 in lst1:
                        num4 = 0
                        for i in lst0:
                            varList.append(i)
                            nameList.append(var + '[' + str(num1) + ']' + '[' + str(num2) + ']' +
                                                  '[' + str(num3) + ']' + '[' + str(num4) + ']')
                            num4 += 1
                        num3 += 1
                    num2 += 1
                num1 += 1

    return varList, nameList
