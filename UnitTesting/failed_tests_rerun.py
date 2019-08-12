

def failed_tests_rerun():
    import os
    from importlib import import_module
    import ast

    with open(os.path.join('UnitTesting', 'failed_tests.txt'), 'r') as file:
        file_text_list = file.readlines()

    for line in file_text_list[2:]:
        path, function_list = line.split(': ', 1)
        print(path, function_list)

        module_string = path.replace('/', '.')[:-3]
        print(module_string)

        module = import_module(module_string)
        print(module)

        for function_string in ast.literal_eval(function_list):
            print(function_string)

            function = getattr(module, function_string)
            print(function)
            #function()



        #imp.load_source('mod', module)
        #print(mod)


if __name__ == '__main__':
    failed_tests_rerun()
