from datetime import date
from UnitTesting.create_dict_string import create_dict_string

# [first_time_print] takes in a module [mod], a value dictionary [value_dict], a path [path], and a boolean [write].
# It prints to the console the properly formatted trusted_values_dict entry based on [mod] and [value_dict].
# Additionally, if [write] is [True], it appends this output to the file [path]/trusted_values_dict.py

# Called by run_test


def first_time_print(mod, value_dict, path, write=True):
    print('\nModule: ' + mod + '\nPlease copy the following code between the ##### and paste it into your ' +
          'trusted_values_dict.py file:\n' + "#####\n\n# Generated on: " + str(date.today()) +
          "\ntrusted_values_dict['" + mod + "Globals'] = " + create_dict_string(value_dict) + "\n\n#####")

    if write:
        fw = open(path + '/trusted_values_dict.py', 'a')
        fw.write("\n# Generated on: " + str(date.today()) + "\ntrusted_values_dict['" + mod + "Globals'] = "
                 + str(value_dict) + '\n')
        fw.close()
