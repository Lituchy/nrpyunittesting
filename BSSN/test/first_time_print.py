from datetime import datetime


# Takes in a module [mod] and a module dictionary [mod_dict], and prints the code that needs to be copied
# into trustedValuesDict.

# Called by run_test

def first_time_print(mod, mod_dict):
    print('\nModule: ')
    print(mod)
    print('Please copy the following code between the ##### and paste it into your trusted_values_dict.py file:')
    print("#####\n\n# Generated on: " + str(datetime.now()) + "\ntrusted_values_dict['" + mod + "Globals'] = "
          + str(mod_dict) + "\n\n#####")
