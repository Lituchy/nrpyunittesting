import logging


# [setup_trusted_values_dict] takes in a path [path], and creates the file [trusted_values_dict.py] in the
# directory specified in [path]. If [trusted_values_dict.py] already exists within this directory,
# nothing happens.

# Called by NRPyUnitTests_(Anything)_Globals

def setup_trusted_values_dict(path):

    # Try opening [trusted_values_dict.py] in [directory].
    try:
        fr = open(path + '/trusted_values_dict.py', 'r')
        fr.close()
    # If [trusted_values_dict.py] does not exist in [directory], create it with default content.
    except IOError:
        logging.info('trusted_values_dict.py does not exist. Creating it...\n')
        fw = open(path + '/trusted_values_dict.py', 'w+')
        fw.write('from mpmath import mpf, mp, mpc\nfrom UnitTesting.standard_constants import precision\n\n'
                 'mp.dps = precision\ntrusted_values_dict = {}\n')
        fw.close()
