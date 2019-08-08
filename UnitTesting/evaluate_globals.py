import logging
from importlib import import_module

# [evaluate_globals] takes in a module [module], a module name [module_name], a list of globals [global_list], and a
# list of functions [function_list]. It uses executes code that imports [module] as [module_name], calls all the
# functions in [function_list] on [module_name], gets the expressions for each global in [global_list], and stores the
# globals in a dictionary [var_dict].

# Called by run_test


def evaluate_globals(self):

    logging.debug(' Importing ' + self.module + '...')

    try:
        imported_module = import_module(self.module)
    # If user supplied an incorrect module, error
    except ImportError:
        logging.error(" Attribute 'module' for " + self.module_name + " does not exist as a module. This attribute "
                      "should be what you would type if you were importing 'module' in your own file.\n")
        self.assertTrue(False)
    except ValueError:
        logging.error(" Attribute 'module' for " + self.module_name + " is empty -- it must have a value.")
        self.assertTrue(False)

    logging.debug(' ...Success: Imported module.')

    logging.debug(' Executing initialization_string...')

    logging.debug('initialization_string: ' + self.initialization_string)

    exec(self.initialization_string)

    logging.debug(' ...Successfully executed.')

    string_exec = self.module_name + '.' + self.function + '\n'

    for glob in self.global_list:
        string_exec += glob + '=' + self.module_name + '.' + glob + '\n'

    # Initializing location
    var_dict = {}

    logging.debug(' Executing function call and global assignment...')

    # Executing string of execution with current globals and storing resulting globals in loc
    exec(string_exec, {self.module_name: imported_module}, var_dict)

    logging.debug(' ...Successfully executed.')

    return var_dict
