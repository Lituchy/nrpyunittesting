from datetime import date
from setup_trusted_values_dict import find_path

# Takes in a module [mod] and a module dictionary [mod_dict], and prints the code that needs to be copied
# into trustedValuesDict.
# Called by run_test


def first_time_print(mod, value_dict, path):
    print('\nModule: ' + mod)
    print('Please copy the following code between the ##### and paste it into your trusted_values_dict.py file:')
    print("#####\n\n# Generated on: " + str(date.today()) + "\ntrusted_values_dict['" + mod + "Globals'] = "
          + str(value_dict) + "\n\n#####")

    fw = open(find_path(path) + 'trusted_values_dict.py', 'a')
    fw.write("\n# Generated on: " + str(date.today()) + "\ntrusted_values_dict['" + mod + "Globals'] = "
             + str(value_dict) + '\n')
    fw.close()
