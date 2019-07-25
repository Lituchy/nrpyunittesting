from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.ShiftedKerrSchild'

    module_name = 'ShiftedKerrSchild'

    global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

    function_list = ['ShiftedKerrSchild(ComputeADMGlobalsOnly = True)']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
