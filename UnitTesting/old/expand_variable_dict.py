
# [expand_variable_dict] takes in a variable dictionary [variable_dict] and returns a dictionary that represents
# the expanded version of [variable_dict] according to the dimension of each variable in [variable_dict].
# Example: expand_variable_dict( { 'alpha': 0, 'betaU': [1, 3, 2] } ) --> { 'alpha': 0, 'betaU[0]': 1, 'betaU[1]': 3,
#                                                                           'betaU[2]': 2 }

# Called by cse_simplify_and_evaluate_sympy_expressions


def expand_variable_dict(variable_dict):

    # Initialize the result dictionary
    result_dict = dict()

    # Iterate through all elements of variable_dict
    for var, expression_list in variable_dict.items():

        # Getting the dimension and length of expression list
        dim, length = get_variable_dimension(expression_list)

        # If list is a scalar, easy computation with no necessary indexing
        if dim == 0:
            result_dict[var] = expression_list
        # Otherwise, need to do more work
        else:
            # Initialize our counter of the correct dimension
            counter = '0' * dim
            # Call flatten on our expression list to get a flattened list
            flattened_list = flatten(expression_list, [])

            # Append next element to var list and increment counter
            for elt in flattened_list:
                result_dict[form_string(var, counter)] = elt
                counter = increment_counter(counter, length)

    return result_dict

# Sub-functions:


# Takes in a tensor [tensor] and returns the rank of that tensor, along with the length of the tensor
# scalar -> rank 0 tensor with length 1 -> 0, 1
# vector with 5 elements -> rank 1 tensor with length 5 -> 1, 5
# tensor with NxN elements -> rank 2 tensor with length N -> 2, N
def get_variable_dimension(tensor):
    dim = 0
    length = 1

    while isinstance(tensor, list):
        if dim == 0:
            length = len(tensor)
        dim += 1
        tensor = tensor[0]

    return dim, length


# iter_counter takes in a counter [counter] and a length [length] and returns the next number after counter
# in base [length].
# Example: iter_counter('00', 2) -> '01'
#          iter_counter('02', 3) -> '10'
#          iter_counter('01111', 2) -> '10000'
def increment_counter(counter, length):

    # Set return_string to empty string, set num to 1
    return_string = ''
    num = 1

    # Loop backwards through each character [char] in [counter]
    for char in reversed(counter):

        # Add [num] to the integer representation of [char]
        digit = int(char) + num
        # If it's time to loop back around
        if digit == length:
            # Add a 0 to the return string, num = 1
            return_string += '0'
            num = 1
            # Add current digit to the return string, num = 0
        else:
            return_string += str(digit)
            num = 0

    # Return reversed return_string since we built it backwards
    return return_string[::-1]


# Used to form the proper string to be added to name list based on var and counter
def form_string(var, counter):
    return_string = var
    for char in counter:
        return_string += '[' + char + ']'

    return return_string


# Function used for removing nested lists in python.
# https://www.geeksforgeeks.org/python-convert-a-nested-list-into-a-flat-list/
def flatten(l, fl):
    for i in l:
        if type(i) == list:
            flatten(i, fl)
        else:
            fl.append(i)
    return fl



