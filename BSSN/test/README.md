## NRPy Unit Testing Globals: An In-Depth Guide

### Interactive Modules

**trustedValuesDict:**<br /> 
This module does this

**Your_UnitTests:**<br />
This is what you do

### Functions:

**calcError:**<br /> 
This function does this

**createTrustedGlobalsDict:**<br /> 
This function does this

**listToValueList:**<br /> 
This function does this

**moduleDictToList:**<br /> 
This function does this

**evaluateGlobals:**<br /> 
This function does this

**firstTimePrint:**<br /> 
This function does this

**functionsAndGlobals:**<br /> 
This function does this

**getVariableDimension:**<br /> 
This function does this

**isFirstTime:**<br /> 
This function does this

**runTest:**<br /> 
This function does this

### Example Usage:

Say you have a module [myModule] which has globals [x, y, z], and an initialization function [myModuleInit()]. How would
you go about testing these globals using the NRPy unit testing globals infrastructure? <br />
The first step is to create a unittest file. An example name is NRPyUnitTests_Globals_Tests.py <br />
Then it's important to import the necessary modules. Here we import unittest, which is Python's built-in testing platform, 
logging, which allows us to easily specify the level of desired output, and runTest and functionsAndGlobals,
as described above. <br />

`import unittest`<br />
`import logging`<br />
`from runTest import runTest`<br />
`from functionsAndGlobals import functionsAndGlobals`<br />

We then set the logging level according to the desired level of output. A good default level is INFO.

`# ERROR -> Outputs minimal information -- only when there's an error`<br />
`# INFO -> Outputs when starting and finishing a module, as well as everything in ERROR`<br />
`# DEBUG -> Displays all pairs of values being compared, as well as everything in INFO`<br />
`# NOTSET -> Displays symbolic dictionary for all modules, as well as everything in DEBUG`

`logging.basicConfig(level=logging.INFO)`<br />

Now that all the initialization is done, it's time to begin testing. The first step in testing is to create the unittest
class and a function for your specific test as follows. Note that the function MUST begin with the word 'test'.

`class TestMyGlobals(unittest.TestCase):`<br />

&nbsp;&nbsp;&nbsp;`def testMyModule(self):`<br />

The next steps are to import the modules to be tested and any required pre-initialization for the modules, create a list
 of globals, and create a list of functions. We'll use [myModule] as described above.

`import myModule as myMod`<br />
`functionList = ['myModuleInit()']`<br />
`globalList = ['x', 'y', 'z']`


Note that the globals and functions are listed as strings! This is intentional and will cause an  error otherwise.

Next is to create our module dictionary [ModDict], which stores all information for our modules. This is where we use 
functionsAndGlobals, the function described above. We pass into it first our list of functions then our list of globals.

`ModDict = {'myMod': functionsAndGlobals(functionList, globalList)}`

What this specifically does is create a dictionary with key `myMod` and value `functionsAndGlobals(functionList, 
globalList)`, which we know to be a dictionary as well from our functions tutorials.<br />
IMPORTANT NOTE: The key of `ModDict` is `'myMod'`. It MUST be a string, and it MUST have the same name as the imported
module. Since we said `import myModule as myMod` above, its name must be `myMod`. If we had instead said
`import myModule as exampleMod` then in `ModDict` we would have to have the key as `'exampleMod'`. This is vital
for the way `runTest` functions.

The next step is to call `runTest` in order to calculate the globals for our modules. 

`runTest(self, ModDict, locals())`

Finally, we must put the following if statement at the bottom of our file in order for everything to communicate 
properly.

`if __name__ == '__main__':`<br />
&nbsp;&nbsp;&nbsp;`unittest.main()`

Our resulting file should look as such:

`import unittest`<br />
`import logging`<br />
`from runTest import runTest`<br />
`from functionsAndGlobals import functionsAndGlobals`<br />

`logging.basicConfig(level=logging.INFO)`<br />

`class TestMyGlobals(unittest.TestCase):`<br />

&nbsp;&nbsp;&nbsp;`def testMyModule(self):`<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`import myModule as myMod`<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`functionList = ['myModuleInit()']`<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`globalList = ['x', 'y', 'z']`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ModDict = {'myMod': functionsAndGlobals(functionList, globalList)}`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`runTest(self, ModDict, locals())`

`if __name__ == '__main__':`<br />
&nbsp;&nbsp;&nbsp;`unittest.main()`


Now that we have completed our test file, it's time to run it to calculate our trusted values for 
the first time. Run the test file, and you should see that text has been written to the console. Follow
the instructions given by copying the code in between the `#####` into your trustedValuesDict.py file.
Example output is as follows:

`Please copy the following code between the ##### and paste it into your trustedValuesDict.py file:` <br />
`#####`

`# Generated on: 2019-06-11 12:25:19.221572` <br />
`trustedValuesDict['myModuleGlobals'] = {'x': mpf('0.122483331574515176153136610247876'), 'y': mpf('0.0'), 
'z': mpf('66.6570391079152319165851690987334')}`

`#####`

After following the instructions, run the code again and you should see that the test passes with no errors.
