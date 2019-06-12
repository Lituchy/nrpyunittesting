from get_variable_dimension import get_variable_dimension


# moduleDictToList takes in a module dictionary [module_dict] and returns a tuple
# of lists; the first list [var_list] is a list of sympy expressions and the second
# list [name_list] is the respective corresponding name for each expression in [var_list].
# Example: var_list[0] -> r/(M+r)
#          name_list[0] -> 'alphaSph'
# Note: Not currently equipped to deal with any tensors of rank >= 5

# Called by run_test


def module_dict_to_list(module_dict):
    var_list = []
    name_list = []

    for var, expression_list in module_dict.items():
        dim, length = get_variable_dimension(expression_list)
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
