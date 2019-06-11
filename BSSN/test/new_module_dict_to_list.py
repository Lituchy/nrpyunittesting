from get_variable_dimension import get_variable_dimension

# moduleDictToList takes in a variable dictionary [variable_dict] and returns a tuple
# of lists; the first list [var_list] is a list of sympy expressions and the second
# list [name_list] is the respective corresponding name for each expression in [var_list].
# Example: var_list[0] -> r/(M+r)
#          name_list[0] -> 'alphaSph'
# Note: Not currently equipped to deal with any tensors of rank >= 5

# Called by run_test


# iter_counter takes in a counter [counter] and a length [length] and returns the next number after counter
# in base [length].
# Example: iter_counter('00', 2) -> '01'
#          iter_counter('02', 3) -> '10'
#          iter_counter('01111', 2) -> '10000'
def iter_counter(counter, length):

    # Reverse counter, set return_string to empty string, set num to 1
    rev_counter = counter[::-1]
    return_string = ''
    num = 1

    # Loop through each character [char] in rev_counter
    for char in rev_counter:

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

    return return_string[::-1]


def new_module_dict_to_list(variable_dict):

    var_list = []
    name_list = []

    for var, expression_list in variable_dict.items():

        print('\nvar: ' + str(var))
        print('expression list: ' + str(expression_list))

        dim, length = get_variable_dimension(expression_list)

        print('dim: ' + str(dim))
        print('length: ' + str(length))

        if length == 0:
            total_number_vars = 0
        else:
            total_number_vars = length ** dim
        print('total number vars:' + str(total_number_vars))

        counter = '0' * dim
        print('counter: ' + counter)

        print(iter_counter(counter, length))

        # TODO: Finish implemtation with iter_counter


        if dim == 0:
            var_list.append(expression_list)
            name_list.append(var)
        elif dim == 1:
            num = 0
            for i in expression_list:
                var_list.append(i)
                name_list.append(var + '[' + str(num) + ']')
                num += 1
        elif dim == 2:
            num1 = 0
            for lst in expression_list:
                num2 = 0
                for i in lst:
                    var_list.append(i)
                    name_list.append(var + '[' + str(num1) + ']' + '[' + str(num2) + ']')
                    num2 += 1
                num1 += 1
        elif dim == 3:
            num1 = 0
            for lst1 in expression_list:
                num2 = 0
                for lst0 in lst1:
                    num3 = 0
                    for i in lst0:
                        var_list.append(i)
                        name_list.append(var + '[' + str(num1) + ']' + '[' + str(num2) + ']' + '[' + str(num3) + ']')
                        num3 += 1
                    num2 += 1
                num1 += 1
        elif dim == 4:
            num1 = 0
            for lst2 in expression_list:
                num2 = 0
                for lst1 in lst2:
                    num3 = 0
                    for lst0 in lst1:
                        num4 = 0
                        for i in lst0:
                            var_list.append(i)
                            name_list.append(var + '[' + str(num1) + ']' + '[' + str(num2) + ']' +
                                             '[' + str(num3) + ']' + '[' + str(num4) + ']')
                            num4 += 1
                        num3 += 1
                    num2 += 1
                num1 += 1

    return var_list, name_list
