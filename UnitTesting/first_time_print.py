from datetime import date
from setup_trusted_values_dict import find_path

# [first_time_print] takes in a module [mod], a value dictionary [value_dict], and a path [path], and prints to the
# console the properly formatted trusted_values_dict entry based on [mod] and [value_dict]. Additionally, it appends
# this output to the file [path]/trusted_values_dict.py

# Called by run_test


def first_time_print(mod, value_dict, path):
    print('\nModule: ' + mod + '\nPlease copy the following code between the ##### and paste it into your' +
          'trusted_values_dict.py file:\n' + "#####\n\n# Generated on: " + str(date.today()) +
          "\ntrusted_values_dict['" + mod + "Globals'] = " + str(value_dict) + "\n\n#####")

    fw = open(find_path(path) + 'trusted_values_dict.py', 'a')
    fw.write("\n# Generated on: " + str(date.today()) + "\ntrusted_values_dict['" + mod + "Globals'] = "
             + str(value_dict) + '\n')
    fw.close()
