from UnitTesting.kevin_test import kevin_test


def test():

    module = 'BSSN.BrillLindquist'

    module_name = 'BrillLindquist'

    global_list = ['alphaCart', 'betaCartU', 'BCartU', 'gammaCartDD', 'KCartDD']

    function_list = ['BrillLindquist(ComputeADMGlobalsOnly = True)']

    kevin_test(module, module_name, global_list, function_list)


if __name__ == '__main__':
    test()
