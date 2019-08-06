from UnitTesting.create_test import create_test


def test_MaxwellCartesian_Evol_System_I():

    module = 'Maxwell.MaxwellCartesian_Evol'

    module_name = 'MaxwellCartesian_Evol_System_I'

    function_and_global_dict = {'MaxwellCartesian_Evol()': ['ArhsD', 'ErhsD', 'psi_rhs', 'Cviola']}

    initialization_string_dict = {'MaxwellCartesian_Evol()': 'import NRPy_param_funcs as par\npar.set_parval_from_str("System_to_use","System_I")'}

    create_test(module, module_name, function_and_global_dict, initialization_string_dict=initialization_string_dict)

def test_MaxwellCartesian_Evol_System_II():

    module = 'Maxwell.MaxwellCartesian_Evol'

    module_name = 'MaxwellCartesian_Evol_System_II'

    function_and_global_dict = {'MaxwellCartesian_Evol()': ['ArhsD', 'ErhsD', 'psi_rhs', 'Gamma_rhs', 'Cviola']}

    create_test(module, module_name, function_and_global_dict)


def test_MaxwellCartesian_ID_System_I():

    module = 'Maxwell.MaxwellCartesian_ID'

    module_name = 'MaxwellCartesian_ID_System_I'

    function_and_global_dict = {'MaxwellCartesian_ID()': ['AidD', 'EidD', 'psi_ID']}

    initialization_string_dict = {'MaxwellCartesian_ID()': 'import NRPy_param_funcs as par\npar.initialize_param(par.glb_param("char", __name__, "System_to_use", "System_I"))'}

    create_test(module, module_name, function_and_global_dict, initialization_string_dict=initialization_string_dict)

def test_MaxwellCartesian_ID_System_II():

    module = 'Maxwell.MaxwellCartesian_ID'

    module_name = 'MaxwellCartesian_ID_System_II'

    function_and_global_dict = {'MaxwellCartesian_ID()': ['AidD', 'EidD', 'psi_ID']}

    initialization_string_dict = {'MaxwellCartesian_ID()': 'import NRPy_param_funcs as par\npar.initialize_param(par.glb_param("char", __name__, "System_to_use", "System_II"))'}

    create_test(module, module_name, function_and_global_dict, initialization_string_dict=initialization_string_dict)


if __name__ == '__main__':
    failed = set()
    for fun in dir():
        if fun[0:5] == 'test_':
            print('\nTesting function ' + str(fun) + '...\n')
            try:
                exec(fun + '()')
            except SystemExit:
                failed.add(True)
            else:
                failed.add(False)

    if failed == set() or True in failed:
        exit(1)