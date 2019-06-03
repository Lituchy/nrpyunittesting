from datetime import datetime


# Takes in a module and a module dictionary, and prints the code that needs to be copied
# into trustedValuesDict.

# Called by runTest

def firstTimePrint(mod,modDict):
    print('\nModule: ')
    print(mod)
    print('Please copy the following code between the ##### and paste it into your trustedValuesDict.py file:')
    print("#####\n\n# Generated on: " + str(datetime.now()) + "\ntrustedValuesDict['" + mod + "Globals'] = "
          + str(modDict) + "\n\n#####")
