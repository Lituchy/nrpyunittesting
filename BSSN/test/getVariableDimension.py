# Takes in a tensor [tensor] and returns the rank of that tensor
# 0 -> rank 0 tensor -> scalar
# 1 -> rank 1 tensor -> vector
# ...

# Called by moduleDictToList

def getVariableDimension(tensor):
    
    dim = 0

    while isinstance(tensor, list):
        dim += 1
        tensor = tensor[0]

    return dim
