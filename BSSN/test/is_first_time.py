from trusted_values_dict import trusted_values_dict

# isFirstTime takes in a module dictionary [mod_dict] and determines if it is the first time the code is being run
# based off the existence of trusted values for every module in [mod_dict].
# Requires: The name of the trusted values dictionary is the same as the convention set by create_trusted_globals_dict

# Called by run_test


def is_first_time(mod_dict):

    boolean_list = []
    mod_list = []

    for mod in mod_dict:

        mod_list.append(mod)
        # Boolean stating whether or not the module has an entry with the proper name in trustedValuesDict
        boolean_list.append((mod + 'Globals') not in trusted_values_dict)

    print(mod_list)
    print(boolean_list)

    return boolean_list
