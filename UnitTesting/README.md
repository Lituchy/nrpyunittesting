# NRPy Unit Testing: Functions In-Depth 

## create_test:
create_test is a function that takes the following user-supplied
information: a module to test `module`, the name of the module
`module_name`, and a dictionary whose keys are functions and whose
values are lists of globals `function_and_global_dict`. It uses this
information to generate a test file that is automatically run as a bash
script; this test file does all the heavy lifting in calling the
function, getting expressions for all the globals, evaluating the
expressions to numerical values, and storing the values in the proper
trusted_values_dict.

create_test additionally takes optional arguments `logging_level` and
`initialization_string_dict`, which respectively determine the desired
level of output (think verbosity) and run some python code prior calling
the specified function. Usage is as following:

```
module = 'BSSN.BrillLindquist'

module_name = 'BrillLindquist'

function_and_global_dict = {'BrillLindquist(ComputeADMGlobalsOnly = True)': ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']}

create_test(module, module_name, function_and_global_dict)
```

The way to think of this is that the module to be tested is
BSSN.BrillLindquist. The module_name is how you refer to this module --
it's a bit arbitrary, so whether you prefer BrillLindquist or bl, it
won't change the computation. The function_and_global_dict contains
entry 'BrillLindquist(ComputeADMGlobalsOnly = True)', which is the
function that gets called in the module. It's value in the dictionary is
a list of globals that get created when this function gets called.

Now let's add the optional arguments into the same example:

```
module = 'BSSN.BrillLindquist'

module_name = 'BrillLindquist'

function_and_global_dict = {'BrillLindquist(ComputeADMGlobalsOnly = True)': ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']}

logging_level = 'DEBUG'

initialization_string_dict = {'BrillLindquist(ComputeADMGlobalsOnly = True)': 'print("example")\nprint("Hello world!")'}

create_test(module, module_name, function_and_global_dict, logging_level=logging_level, initialization_string_dict=initialization_string_dict)
```

Now when create_test runs, the user will be given much more output due
to the logging_level; additionally, the user-specified print will occur
due to initialization_string_dict.

You may now be wondering why we use dictionaries to store this data
instead of simply having separate variables `function`, `global_list`,
and `initialization_string`. This is where some of the power of this
testing method lies: we can test multiple functions and their globals
with ease! In other words, function_and_global_dict can contain multiple
entries, each a specific function call with its own associated list of
globals. Since not every function being tested must have an associated
initialization_string, we make an entry for each function optional. An
example is as follows:

```
module = 'BSSN.BrillLindquist'

module_name = 'BrillLindquist'

function_and_global_dict = {'BrillLindquist(ComputeADMGlobalsOnly = True)': ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD'],
                            'BrillLindquist(ComputeADMGlobalsOnly = False)': ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']}

logging_level = 'DEBUG'

initialization_string_dict = {'BrillLindquist(ComputeADMGlobalsOnly = True)': 'print("example")\nprint("Hello world!")'}

create_test(module, module_name, function_and_global_dict, logging_level=logging_level, initialization_string_dict=initialization_string_dict)
```

Both instances will be called separately, with their own globals. The
print statements will only be called in the first function, since there
is no associated initialization_string for the second function as well.

An important note when using `create_test` is that all arguments are
**strings**. This includes the module, module_name, function, each
global in the list of globals, logging level, and initialization_string.
The reason for making these fields strings is that when setting
module_name, for example, there doesn't exist anything in Python with
the name BrillLindquist. So, we wrap it in a string. This is true of
every input. Be careful with the dicts and lists, however: their
arguments are strings, they aren't themselves strings.

## calc_error

## create_dict_string

## cse_simplify_and_evaluate_sympy_expressions

## evaluate_globals

## expand_variable_dict