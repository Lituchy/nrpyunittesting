# Takes in a variable in string form (i.e. 'gammaCartDD') and returns the 
# dimension of that variable according to nrpy convention.
# 0 -> scalar
# 1 -> vector
# 2 -> tensor
def getVariableDimension(strVar):
    
    length = len(strVar)
    chars = strVar[length-2:length]
    
    if chars == 'DD'or chars == 'UU':
        return 2
    elif chars[1] == 'D' or chars[1] == 'U':
        return 1
    else:
        return 0