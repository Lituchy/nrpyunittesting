# Creating trusted_values_dict.py if it doesn't exist

import logging
import platform


def setup_class(path):

    path = find_path(path)

    try:
        fr = open(path + 'trusted_values_dict.py', 'r')
        fr.close()
    except IOError:
        logging.info('trusted_values_dict.py does not exist. Creating it...\n')
        fw = open(path + 'trusted_values_dict.py', 'w+')
        fw.write('from mpmath import mpf, mp, mpc\nfrom UnitTesting.standard_constants import precision\n\n'
                 'mp.dps = precision\ntrusted_values_dict = dict()\n\n# Paste your trusted values here!\n')
        fw.close()


# Subfunction that returns the string we want
def find_path(path):
    for idx, char in enumerate(reversed(path)):
        if char == '/' and platform.system() != 'Windows':
            return path[0:(len(path) - idx)] + '/'
        elif char == '\\' and platform.system() == 'Windows':
            return path[0:(len(path) - idx)] + '\\'