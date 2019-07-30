
# create_trusted_globals_dict takes in a module name [module_name], a trusted values dictionary [trusted_values_dict],
# and a boolean [first_time].

# Called by run_test


def create_trusted_globals_dict(self):

    # If module is being run for the first time, a trusted_values_dict entry doesn't exist; return an empty dictionary.
    if self.first_time:
        return {}
    # Otherwise, return the trusted_values_dict entry for the string [module_name] with the word 'Globals' concatenated
    # onto its end -- this is the standard naming scheme for NRPy unit tests.
    else:
        return self.trusted_values_dict[self.trusted_values_dict_name]
