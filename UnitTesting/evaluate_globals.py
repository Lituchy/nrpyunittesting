# [evaluate_globals] takes in a module [module], a module name [module_name], a list of globals [global_list], and a
# list of functions [function_list]. It uses executes code that imports [module] as [module_name], calls all the
# functions in [function_list] on [module_name], gets the expressions for each global in [global_list], and stores the
# globals in a dictionary [var_dict].

# Called by run_test

from UnitTesting.reload_module import reload_module

def evaluate_globals(module, module_name, global_list, function_list):

    # Initializing string of execution
    string_exec = ''

    # Calling all functions and assigning all globals
    for function in function_list:
        string_exec += module_name + '.' + function + '\n'
    for glob in global_list:
        string_exec += glob + '=' + module_name + '.' + glob + '\n'

    # Initializing location
    var_dict = {}

    # Executing string of execution with current globals and storing resulting globals in loc
    exec(string_exec, {module_name: module}, var_dict)

    # for mod in dir():
    #     reload_module(locals()[mod])

    return var_dict
