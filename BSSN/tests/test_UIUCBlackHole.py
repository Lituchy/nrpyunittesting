from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.UIUCBlackHole'

    module_name = 'UIUCBlackHole'

    global_list = ['alphaSph', 'betaSphU', 'BSphU', 'gammaSphDD', 'KSphDD']

    function_list = ['UIUCBlackHole(ComputeADMGlobalsOnly = True)']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
