# Creating trusted_values_dict.py if it doesn't exist

import logging

# [setup_class] takes in a string representing a path [path], and creates the file [trusted_values_dict.py] in the
# directory of the file specified in [path]. If [trusted_values_dict.py] already exists within this directory,
# nothing happens.
def setup_class(path):

    # Try opening [trusted_values_dict.py] in [directory].
    try:
        fr = open(path + '/trusted_values_dict.py', 'r')
        fr.close()
    # If [trusted_values_dict.py] does not exist in [directory], create it with default contents.
    except IOError:
        logging.info('trusted_values_dict.py does not exist. Creating it...\n')
        fw = open(path + '/trusted_values_dict.py', 'w+')
        fw.write('from mpmath import mpf, mp, mpc\nfrom UnitTesting.standard_constants import precision\n\n'
                 'mp.dps = precision\ntrusted_values_dict = {}\n')
        fw.close()
    # Otherwise, do nothing -- no need to recreate file that already exists.


# # Sub-function that returns the full path to the directory that [path] is in.
# # Typical input for [path] is os.path.abspath(__file__)
# def find_path(path):
#     # Parse the string [path] in reverse
#     for idx, char in enumerate(reversed(path)):
#         # Look for first indicator that we're now at the directory, and return the rest of the string
#         if (char == '/' and platform.system() != 'Windows') or (char == '\\' and platform.system() == 'Windows'):
#             return path[0:(len(path) - idx)]
