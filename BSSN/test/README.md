## NRPy Unit Testing Globals: An In-Depth Guide

### Interactive Modules:

**trusted_values_dict:**<br /> 
This module does this

**Your_UnitTests:**<br />
This is what you do

### Functions:

**calc_error:**<br /> 
This function does this

**create_trusted_globals_dict:**<br /> 
This function does this

**list_to_value_list:**<br /> 
This function does this

**module_dict_to_list:**<br /> 
This function does this

**evaluate_globals:**<br /> 
This function does this

**first_time_print:**<br /> 
`first_time_print` takes in a module `mod` and a value dictionary `value_dict`, and prints the code that needs to be 
copied into trustedValuesDict assuming the entries in `value_dict` correspond to the module `mod`. <br />
Example Usage:
````
mod = 'myModule'
value_dict = {'x': mpf('0.122483331574515176153136610247876'), 'y': mpf('0.0'), 
'z': mpf('66.6570391079152319165851690987334')}

first_time_print(mod, value_dict)
````
Output:
````
Module: myModule
Please copy the following code between the ##### and paste it into your trusted_values_dict.py file:
#####

# Generated on: 2019-06-11 12:25:19.221572
trusted_values_dict['myModuleGlobals'] = {'x': mpf('0.122483331574515176153136610247876'), 
'y': mpf('0.0'), 'z': mpf('66.6570391079152319165851690987334')}`

#####
````
Note that `first_time_print` does not check if it _should_ be called at any given time based on the existence of 
`mod` in `trusted_values_dict`. It is up to the user to determine when the correct time to call the function is. 
If `run_test` is used without any modifications (as recommended), `first_time_print` will run as determined by the 
boolean result from `is_first_time`.
 

**functions_and_globals:**<br /> 
This function does this

**get_variable_dimension:**<br /> 
This function does this

**is_first_time:**<br /> 
This function does this

**run_test:**<br /> 
This function does this

### Example Usage:

Say you have a module `myModule` which has globals `x, y, z` and an initialization function `myModuleInit()`. How would
you go about testing these globals using the NRPy unit testing globals infrastructure? <br />
The first step is to create a unittest file. An example name is `NRPyUnitTests_Globals_Tests.py` <br />
Then it's important to import the necessary modules. Here we import unittest, which is Python's built-in testing platform, 
logging, which allows us to easily specify the level of desired output, and run_test and functions_and_globals,
as described above. <br />
````
import unittest`<br />
import logging`<br />
from run_test import run_test`<br />
from functions_and_globals import functions_and_globals`<br />
````

We then set the logging level according to the desired level of output. A good default level is INFO.
````
# ERROR -> Outputs minimal information -- only when there's an error
# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR
# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO
# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG

logging.basicConfig(level=logging.INFO)
````
Now that all the initialization is done, it's time to begin testing. The first step in testing is to create the unittest
class and a function for your specific test as follows. Note that the function MUST begin with the word 'test'.
````
class TestMyGlobals(unittest.TestCase):

    def test_my_module(self):
````

The next steps are to import the modules to be tested and any required pre-initialization for the modules, create a list
 of globals, and create a list of functions. We'll use `myModule` as described above.
 
````
import myModule as myMod
function_list = ['myModuleInit()']
global_list = ['x', 'y', 'z']
````

Note that the globals and functions are listed as strings! This is intentional and will cause an  error otherwise.

Next is to create our module dictionary `mod_dict`, which stores all information for our modules. This is where we use 
`functions_and_globals`, the function described above. We pass into it first our list of functions then our list of 
globals.

````
mod_dict = {'myMod': functions_and_globals(function_list, global_list)}
````

What this specifically does is create a dictionary with key `myMod` and value `functions_and_globals(function_list, 
global)list)`, which we know to be a dictionary as well from our functions tutorials.<br />
IMPORTANT NOTE: The key of our entry in `mod_dict` is `'myMod'`. It MUST be a string, and it MUST have the same name as the imported
module. Since we said `import myModule as myMod` above, its name must be `myMod`. If we had instead said
`import myModule as exampleMod` then in `ModDict` we would have to have the key as `'exampleMod'`. This is vital
for the way `runTest` functions.

The next step is to call `run_test` in order to calculate the globals for our modules. 

````
run_test(self, mod_dict, locals())
````

Finally, we must put the following if statement at the bottom of our file in order for everything to communicate 
properly.

````
if __name__ == '__main__':
unittest.main()
````

Our resulting file should look as such:

````
import unittest
import logging
from run_test import run_test
from functions_and_globals import functions_and_globals

logging.basicConfig(level=logging.INFO)

class TestMyGlobals(unittest.TestCase):

    def test_my_module(self):

        import myModule as myMod
        function_list = ['myModuleInit()']
        global_list = ['x', 'y', 'z']

        mod_dict = {'myMod': functions_and_globals(function_list, global_list)}

        run_test(self, mod_dict, locals())

if __name__ == '__main__':
    unittest.main()
````

Now that we have completed our test file, it's time to run it to calculate our trusted values for 
the first time. Run the test file, and you should see that text has been written to the console. Follow
the instructions given by copying the code in between the `#####` into your trustedValuesDict.py file.
Example output is as follows:

````
Module: myMod
Please copy the following code between the ##### and paste it into your trusted_values_dict.py file:
#####

# Generated on: 2019-06-11 12:25:19.221572
trusted_values_dict['myModGlobals'] = {'x': mpf('0.122483331574515176153136610247876'), 
'y': mpf('0.0'), 'z': mpf('66.6570391079152319165851690987334')}`

#####
````

After following the instructions, run the code again and you should see that the test passes with no errors.
