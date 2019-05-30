from mpmath import mpf,mp


# Dictionary of trusted values to be used throughout files
global trustedValuesDict

# Standard precision and seed values. Note that changing these may drastically change the calculated values.
trustedValuesDict = {
    "precision": 30,
    "seed": 1234
}

mp.dps = trustedValuesDict["precision"]

# Trusted Values:

# These values come from running the tests for the first time on a trusted verison of nrpy.
# Since the current version is known to be correct, these values should be consistent with any
# subsequent versions of the software. If the tests stop working, something was likely broken.

# Trusted values for BSSN Exact Globals with precision == 30 and seed == 1234

# Generated on: 2019-05-30 13:53:23.962443
trustedValuesDict['BrillLindquistGlobals'] = {'alphaCart': mpf('0.122483331574515176153136610247999'), 'betaCartU[0]': 0, 'betaCartU[1]': 0, 'betaCartU[2]': 0, 'BCartU[0]': 0, 'BCartU[1]': 0, 'BCartU[2]': 0, 'gammaCartDD[0][0]': mpf('66.6570391079152319165851690989984'), 'gammaCartDD[0][1]': 0, 'gammaCartDD[0][2]': 0, 'gammaCartDD[1][0]': 0, 'gammaCartDD[1][1]': mpf('66.6570391079152319165851690989984'), 'gammaCartDD[1][2]': 0, 'gammaCartDD[2][0]': 0, 'gammaCartDD[2][1]': 0, 'gammaCartDD[2][2]': mpf('66.6570391079152319165851690989984'), 'KCartDD[0][0]': 0, 'KCartDD[0][1]': 0, 'KCartDD[0][2]': 0, 'KCartDD[1][0]': 0, 'KCartDD[1][1]': 0, 'KCartDD[1][2]': 0, 'KCartDD[2][0]': 0, 'KCartDD[2][1]': 0, 'KCartDD[2][2]': 0}

# Generated on: 2019-05-30 13:53:24.267244
trustedValuesDict['ShiftedKerrSchildGlobals'] = {'alphaSph': mpf('0.611873766692798472488570416617989'), 'betaSphU[0]': mpf('0.625610493633166822638772330973041'), 'betaSphU[1]': 0, 'betaSphU[2]': 0, 'BSphU[0]': 0, 'BSphU[1]': 0, 'BSphU[2]': 0, 'gammaSphDD[0][0]': mpf('2.67101503379259532016438346708013'), 'gammaSphDD[0][1]': 0, 'gammaSphDD[0][2]': mpf('-1.20517572307269882101503709735004'), 'gammaSphDD[1][0]': 0, 'gammaSphDD[1][1]': mpf('1.22487699767344797967358950175995'), 'gammaSphDD[1][2]': 0, 'gammaSphDD[2][0]': mpf('-1.20517572307269882101503709735004'), 'gammaSphDD[2][1]': 0, 'gammaSphDD[2][2]': mpf('1.37627131033453091934058579009999'), 'KSphDD[0][0]': mpf('-1.38718835226831540718061902171006'), 'KSphDD[0][1]': mpf('0.171664018858514818215855728819989'), 'KSphDD[0][2]': mpf('0.455406940612776090115394191050997'), 'KSphDD[1][0]': mpf('0.171664018858514818215855728819989'), 'KSphDD[1][1]': mpf('1.06437469733833992932303275045991'), 'KSphDD[1][2]': mpf('-0.0774556883566536581224962371138946'), 'KSphDD[2][0]': mpf('0.455406940612776090115394191050997'), 'KSphDD[2][1]': mpf('-0.0774556883566536581224962371138946'), 'KSphDD[2][2]': mpf('0.594852484599533408232026058675987')}

# Generated on: 2019-05-30 13:53:24.292657
trustedValuesDict['StaticTrumpetGlobals'] = {'alphaSph': mpf('0.403092176323945252455401083265003'), 'betaSphU[0]': mpf('0.240608873710370682916226625465004'), 'betaSphU[1]': 0, 'betaSphU[2]': 0, 'BSphU[0]': 0, 'BSphU[1]': 0, 'BSphU[2]': 0, 'gammaSphDD[0][0]': mpf('6.15447854588632421730150623326011'), 'gammaSphDD[0][1]': 0, 'gammaSphDD[0][2]': 0, 'gammaSphDD[1][0]': 0, 'gammaSphDD[1][1]': mpf('2.71247932609742473472094943836995'), 'gammaSphDD[1][2]': 0, 'gammaSphDD[2][0]': 0, 'gammaSphDD[2][1]': 0, 'gammaSphDD[2][2]': mpf('0.0202697649478352484117814815031'), 'KSphDD[0][0]': mpf('-2.23056721663690142814440046331015'), 'KSphDD[0][1]': 0, 'KSphDD[0][2]': 0, 'KSphDD[1][0]': 0, 'KSphDD[1][1]': mpf('0.983083687023713543948423277992989'), 'KSphDD[1][2]': 0, 'KSphDD[2][0]': 0, 'KSphDD[2][1]': 0, 'KSphDD[2][2]': mpf('0.00734636945185188428754902788372999')}

# Generated on: 2019-05-30 13:53:24.646209
trustedValuesDict['UIUCBlackHoleGlobals'] = {'alphaSph': mpf('1.0'), 'betaSphU[0]': 0, 'betaSphU[1]': 0, 'betaSphU[2]': 0, 'BSphU[0]': 0, 'BSphU[1]': 0, 'BSphU[2]': 0, 'gammaSphDD[0][0]': mpf('1395.79778503827727330438811733996'), 'gammaSphDD[0][1]': 0, 'gammaSphDD[0][2]': 0, 'gammaSphDD[1][0]': 0, 'gammaSphDD[1][1]': mpf('9.61434498113641434805550645853074'), 'gammaSphDD[1][2]': 0, 'gammaSphDD[2][0]': 0, 'gammaSphDD[2][1]': 0, 'gammaSphDD[2][2]': mpf('6.70941611174433767041669495975963'), 'KSphDD[0][0]': 0, 'KSphDD[0][1]': 0, 'KSphDD[0][2]': mpf('4.81517781103762810906853631572986'), 'KSphDD[1][0]': 0, 'KSphDD[1][1]': 0, 'KSphDD[1][2]': mpf('0.00353154846117828932682951363208018'), 'KSphDD[2][0]': mpf('4.81517781103762810906853631572986'), 'KSphDD[2][1]': mpf('0.00353154846117828932682951363208018'), 'KSphDD[2][2]': 0}

# Trusted values for BSSN RHS Globals with precision == 30 and seed == 1234

# Generated on: 2019-05-30 14:45:17.150218
trustedValuesDict['RHSGlobals'] = {'cf_rhs': mpf('0.108793533420243400382437359023997'), 'trK_rhs': mpf('3.30282095875140881706270774125007'), 'lambda_rhsU[0]': mpf('14.4146532579619208332321232445997'), 'lambda_rhsU[1]': mpf('9.14040344940838866262852644671971'), 'lambda_rhsU[2]': mpf('26.9957568838818105455343954831985'), 'a_rhsDD[0][0]': mpf('2.26556473599099347828970276506987'), 'a_rhsDD[0][1]': mpf('6.40075102732740541648406894100033'), 'a_rhsDD[0][2]': mpf('6.96359374373942498303607889058989'), 'a_rhsDD[1][0]': mpf('6.4007510273274054164840689410098'), 'a_rhsDD[1][1]': mpf('7.00109695915127106153367716669004'), 'a_rhsDD[1][2]': mpf('5.47699085412767239495706268521978'), 'a_rhsDD[2][0]': mpf('6.96359374373942498303607889058989'), 'a_rhsDD[2][1]': mpf('5.47699085412767239495706268521978'), 'a_rhsDD[2][2]': mpf('3.13360411746722065209892752545988'), 'h_rhsDD[0][0]': mpf('-2.3534765754185598752394842153301'), 'h_rhsDD[0][1]': mpf('4.03858137169987222744923011743977'), 'h_rhsDD[0][2]': mpf('5.4886784474384333973268345805799'), 'h_rhsDD[1][0]': mpf('4.03858137169987222744923011743977'), 'h_rhsDD[1][1]': mpf('6.11377171283770447492683152001965'), 'h_rhsDD[1][2]': mpf('5.51757858482037307109713427494983'), 'h_rhsDD[2][0]': mpf('5.4886784474384333973268345805799'), 'h_rhsDD[2][1]': mpf('5.51757858482037307109713427494983'), 'h_rhsDD[2][2]': mpf('6.18063009469368111916088571625035')}

# Generated on: 2019-05-30 14:45:19.207119
trustedValuesDict['gaugeRHSGlobals'] = {'alpha_rhs': mpf('0.901044258771876282261546290678959'), 'bet_rhsU[0]': mpf('17.1997657603710396365205711173008'), 'bet_rhsU[1]': mpf('-27.2327651253429729949596610117012'), 'bet_rhsU[2]': mpf('58.0374456172848164603543757654023'), 'vet_rhsU[0]': mpf('3.21541454902200471606182815639986'), 'vet_rhsU[1]': mpf('2.41489682578349003033017259987988'), 'vet_rhsU[2]': mpf('5.81064334017651405863650589633999')}
