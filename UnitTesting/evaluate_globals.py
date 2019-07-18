# [evaluate_globals] takes in a module dictionary [mod_dict] and locals [old_locals] and returns a dictionary
# [result_dict] containing the symbolic expressions for each global specified in mod_dict

# Requires: Modules can't have the same name. Two globals for a given module can't have the same name.
#           Functions must be able to be called on their respective module. Globals must 
#           be defined in their respective modules.
# Returns: Returns [resultDict], which is a dictionary whose keys are the modules that were passed 
#          through modDict and the values are dictionaries containing the values for the specified globals
# Note: Must pass in locals() as second argument to insure that all imports that have been done are accessible
#       by the evaluateGlobals module

# Called by run_test


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

    return var_dict
