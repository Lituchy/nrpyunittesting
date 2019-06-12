## NRPy Unit Testing Globals: An In-Depth Guide

### Motivation:

What is the purpose of unit testing, and why should you do it? To begin thinking about that, consider what subtleties 
can occur with your code that are almost unnoticeable to the eye, but wind up giving you a very incorrect result. You
could make a small optimization, and observe that nothing changes about your result. However, maybe the optimization 
you made only works on Python 3 and not Python 2, or it changes a value by some tiny amount -- too small to be obviously
noticeable, but enough to make a difference.

This is where unit testing comes in. By initially calculating values for the globals of your modules in a **trusted**
version of your code and storing those values in a dictionary, you can then easily check if something stopped working
by comparing your newly calculated values to the ones you've stored. On the frontend, there are four modules 
essential to get your unit tests up and running: `trusted_values_dict`, `functions_and_globals`, `run_test`, and your 
testing module (which we'll simply reference as `Your_Tests`). The usage of each of these modules is outlined in the 
**Interactive Modules** section. There are many functions at play in the backend as well, all of which will 
be described in detail below in the **Functions** section. Understanding of them may not be essential to get your tests 
up-and-running, but some basic understanding of these modules with undoubtedly streamline the testing process and how 
to potentially create your own, different types of tests.

An important caveat is that the unit testing does not test the **correctness** of your code or your variables. The 
unit tests function as a protective measure to ensure that nothing was broken. It gets its values by running your code, 
so if something starts out incorrect, it will be stored as incorrect in the system. There are measures against this, 
but it relies on the user's knowledge of what versions of their code are correct.

### Interactive Modules:

**trusted_values_dict:**<br /> 
`trusted_values_dict` acts as the storage hub for NRPy unit tests. It is a module that stores trusted values of the 
globals that you calculate in an easily accessible dictionary. It also stores the precision `precision` that is used in 
comparing your trusted values and calculated values, as well as a seed `seed` that is used by some functions below. A 
good default value for `precision` is `30`, and a standard `seed` is `1234`. 


**functions_and_globals:**<br /> 
This function does this

**run_test:**<br /> 
`run_test` is the culmination of all the functions outlined below. It does all the heavy lifting in calculating values,
comparing them to trusted values, throwing errors if necessary, printing the desired output, etc. `run_test` takes in 
`self`, which simply allows it to use the assert functions of `unittest`, `mod_dict`, which is the user-created module 
dictionary containing the modules they're testing, the necessary functions to run for each module, and the globals to 
evaluate and compare for each module, and `locs` (almost always a simple call to the built-in function 
`locals`), which allows the current local variables to be passed into `run_test`.  

**Your_Tests:**<br />
This is what you do

### Functions:

**calc_error:**<br /> 
This function does this

**create_trusted_globals_dict:**<br /> 
This function does this

**list_to_value_list:**<br /> 
This function does this

**evaluate_globals:**<br /> 
This function does this

**first_time_print:**<br /> 
`first_time_print` takes in a module `mod` and a value dictionary `value_dict`, and prints the code that needs to be 
copied into `trusted_values_dict` assuming the entries in `value_dict` correspond to the module `mod`. <br />
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

**get_variable_dimension:**<br /> 
`get_variable_dimension` takes in a tensor `tensor` and returns a tuple containing the rank of the tensor `dim` and the 
length of the tensor `length`. `dim` is defined as the number of dimensions of `tensor`. For example, `dim` of a scalar
is `0`, `dim` of a vector is `1`, etc. `length` is defined as the number of variables in each `dim` of `tensor`. For 
example, `length` of `[1,2,3]` is `3`. It is assumed that any tensor being passed into the function is 'square'. This
means that a `d`-dimensional tensor being passed in is made up of `n` tensors of dimension `d-1`, then each `d-1` 
dimensional tensors must also be made up of `n` tensors of dimension `d-2`, etc. `get_variable_dimension` of an empty 
list `[]` throws an `IndexError`. Example usage is shown below:

````
scalar = 2
get_variable_dimension(scalar) -> 0, 1

vector = [1, 2, 3]
get_variable_dimension(vector) -> 1, 3

long_vector = [2, 1, 3, 3, 4, 10, 12]
get_variable_dimension(long_vector) -> 1, 7

basic_tensor = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
get_variable_dimension(basic_tensor) -> 2, 3

high_dim_tensor = [[[[1]]]]
get_variable_dimension(high_dim_tensor) -> 4

empty_list = []
get_variable_dimension(empty_list) -> Raises IndexError
````

**variable_dict_to_list:**<br /> 
`variable_dict_to_list` takes in a variable dictionary `variable_dict` and returns a tuple containing a list of variables
`var_list` and its corresponding list of names `name_list`. These lists are created such that each tensor in 
`variable_dict` is broken down into each of its scalars, the scalar is stored in `var_list`, and the name of the scalar
according to Python list syntax is stored in the same respective index in `name_list`. Example usage is shown below:

````
variable_dict = {'alpha' : r / (M + r), 'betaDD': [[r * cos(theta), r * sin(theta)], 
[r * tan(theta), 0]], 'gammaU': [r, r**2, r**3, r**4]}

variable_dict_to_list(variable_dict) -> 
[r / (M + r), r * cos(theta), r * sin(theta), r * tan(theta), 0, r, r**2, r**3, r**4] , 
['alpha', 'betaDD[0][0]', 'betaDD[0][1]','betaDD[1][0]', 'betaDD[1][1]',
'gammaU[0]', 'gammaU[1]', 'gammaU[2]', 'gammaU[3]']
````

**is_first_time:**<br /> 
`is_first_time` takes in a module dictionary `mod_dict` and returns a list containing corresponding booleans for each
module in `mod_dict`. The boolean for each module `mod` is `True` if `trusted_values_dict` contains a dictionary entry
for `mod` according to the naming convention defined in `create_trusted_globals_dict`, `False` otherwise. Say we have 
`trusted_values_dict` with the following keys (and corresponding values which aren't listed):

````
trusted_values_dict = {'Module1Globals', 'module1Globals', 'mod1globals', 'Mod2Globals', 'Module3Globs'}
````

Then we'd get the following results with the following module dictionaries (without their corresponding values):

````
mod_dict_1 = {'Module1', 'Module2', 'Module3'}
is_first_time(mod_dict_1) -> [True, False, False]

mod_dict_2 = {'Mod1', 'Mod2', 'Mod3'}
is_first_time(mod_dict_2) -> [False, True, False]

mod_dict_3 = {'module1', 'Module3', 'Mod2', 'mod1'}
is_first_time(mod_dict_3) -> [True, False, True, False]
````

An important note is that the order of keys in the module dictionary is the same order that `is_first_time` generates
its boolean list. This ensures that the resulting boolean list properly corresponds with the input module dictionary.

### Example Usage:

Say you have a module `myModule` which has globals `x, y, z` and an initialization function `myModuleInit()`. How would
you go about testing these globals using the NRPy unit testing globals infrastructure? <br />
The first step is to create a unittest file. An example name is `NRPyUnitTests_Globals_Tests.py` <br />
Then it's important to import the necessary modules. Here we import unittest, which is Python's built-in testing platform, 
logging, which allows us to easily specify the level of desired output, and run_test and functions_and_globals,
as described above. <br />
````
import unittest
import logging
from run_test import run_test
from functions_and_globals import functions_and_globals
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

Now let's say you have another module that's similar to `myModule` -- say `myModule2`, with initialization function 
`myMod2Init()` and globals `x2 y2`-- and you want to test it as well
without having to add an entirely new test file, copying all the code, etc. With some simile variable renaming, we can
add `myModule2` to our `test_my_module` function to easily test it as well. One possible way of doing this is to 
adjust our test file as follows:

````
import unittest
import logging
from run_test import run_test
from functions_and_globals import functions_and_globals

logging.basicConfig(level=logging.INFO)

class TestMyGlobals(unittest.TestCase):

    def test_my_modules(self):

        import myModule as myMod
        function_list_1 = ['myModuleInit()']
        global_list_1 = ['x', 'y', 'z']
        
        import myModule2 as myMod2
        function_list_2 = ['myMod2Init()']
        global_list_2 = ['x2', 'y2']


        mod_dict = {'myMod':  functions_and_globals(function_list_1, global_list_1),
                    'myMod2': functions_and_globals(function_list_2, global_list_2)}

        run_test(self, mod_dict, locals())

if __name__ == '__main__':
    unittest.main()
````

It's as simple as that! All we did was change the function name from `test_my_module` to `test_my_modules` (note that
this isn't necessary, but just makes things more understandable), we renamed `function_list` and `global_list` by
adding `_1` onto the end, and we imported and created our new modules, function list, and global list. Then 
by simply adding `myMod2` to the dictionary with the proper function and global list, we are now easily testing 
`myMod2` as well as the original `myMod`. Of course, after running the code for the first time you'll have to copy
the calculated values for `trusted_values_dict` into place, but you _don't_ have to redo anything to do with `myMod`.
Its tests are unaffected by the introduction of `myModule2`, and as such nothing about them will change.

