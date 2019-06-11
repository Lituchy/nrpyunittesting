# Takes in a tensor [tensor] and returns the rank of that tensor
# 0 -> rank 0 tensor -> scalar
# 1 -> rank 1 tensor -> vector
# ...
# Raises [IndexError] if the first argument of the tensor of any rank is the empty list.
# Assumes that the tensor being passed in is consistent in dimension, i.e. the 0'th index of the list has the same
# dimension as any other index of the list.

# Called by module_dict_to_list


def get_variable_dimension(tensor):
    
    dim = 0

    while isinstance(tensor, list):
        dim += 1
        tensor = tensor[0]

    return dim
