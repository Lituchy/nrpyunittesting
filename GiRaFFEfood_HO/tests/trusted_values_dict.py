from mpmath import mpf, mp, mpc
from UnitTesting.standard_constants import precision

# Dictionary of trusted values to be used throughout files.
# Standard precision and seed values are precision: 30, seed: 1234.
# Note that changing these may drastically change the calculated values.

mp.dps = precision

trusted_values_dict = dict()

# # Generated on: 2019-06-20
# trusted_values_dict['GiRaFFEfood_HOGlobals'] = {'AD[0]': mpf('-0.94115744530567775184433060969805'), 'AD[1]': mpf('1.69321905451215397667294884427835'), 'AD[2]': mpf('0.0'), 'ValenciavU[0]': mpf('0.294521454719030203077048644263695'), 'ValenciavU[1]': mpf('0.163706555966521359089651866391384'), 'ValenciavU[2]': mpf('-0.975070156720603120338029391237849')}
#
# # Generated on: 2019-06-28
# trusted_values_dict['GiRaFFEfood_HO_Aligned_RotatorGlobals'] = {'AD[1]': mpf('0.0000801849028614445840261036910018663'), 'AD[2]': mpf('0.0'), 'AD[0]': mpf('-0.0000814205707660507544992115618536768'), 'ValenciavU[2]': mpf('0.0'), 'ValenciavU[1]': mpf('0.633637754333239655611670762070977'), 'ValenciavU[0]': mpf('-0.64340225872540982046101426632778')}
#
# # Generated on: 2019-06-28
# trusted_values_dict['GiRaFFEfood_HO_1D_testsGlobals'] = {'ValenciavleftU[2]': mpf('-0.177163047879428556096999973264083'), 'ValenciavcenterU[0]': mpf('0.960565202527069021634940572819423'), 'ArightD[1]': mpf('4.69702474888921975092157202378567'), 'ArightD[0]': mpf('0.0'), 'ValenciavrightU[0]': mpf('0.963623291737759499614278388867548'), 'ValenciavcenterU[1]': mpf('0.181077139394546010673339180581874'), 'AcenterD[2]': mpf('0.0252378284171808196728573673392487'), 'AleftD[2]': mpf('0.0252378284171808196728573673392487'), 'ValenciavrightU[2]': mpf('-0.138124790730574777928762802038226'), 'AleftD[1]': mpf('3.60963442222247660778615524728305'), 'AcenterD[0]': mpf('0.0'), 'AcenterD[1]': mpf('4.15948634638592125992534403685407'), 'ValenciavrightU[1]': mpf('0.181359583480349125594396153707543'), 'ValenciavleftU[1]': mpf('0.180159993445189792091149436683383'), 'ArightD[2]': mpf('0.0252378284171808196728573673392487'), 'AleftD[0]': mpf('0.0'), 'ValenciavleftU[0]': mpf('0.950635045468266851031502199941728'), 'ValenciavcenterU[2]': mpf('-0.148347823665109776191580527495614')}

# Generated on: 2019-06-28
trusted_values_dict['GiRaFFEfood_HO_1D_testsGlobals'] = {'AleftD[0]': mpf('0.0'), 'AleftD[1]': mpf('3.60963442222247660778615524728305'), 'AleftD[2]': mpf('0.0252378284171808196728573673392487'), 'AcenterD[0]': mpf('0.0'), 'AcenterD[1]': mpf('4.15948634638592125992534403685407'), 'AcenterD[2]': mpf('0.0252378284171808196728573673392487'), 'ArightD[0]': mpf('0.0'), 'ArightD[1]': mpf('4.69702474888921975092157202378567'), 'ArightD[2]': mpf('0.0252378284171808196728573673392487'), 'ValenciavleftU[0]': mpf('0.950635045468266851031502199941728'), 'ValenciavleftU[1]': mpf('0.180159993445189792091149436683383'), 'ValenciavleftU[2]': mpf('-0.177163047879428556096999973264083'), 'ValenciavcenterU[0]': mpf('0.960565202527069021634940572819423'), 'ValenciavcenterU[1]': mpf('0.18107713939454601067333918058185'), 'ValenciavcenterU[2]': mpf('-0.148347823665109776191580527495614'), 'ValenciavrightU[0]': mpf('0.963623291737759499614278388867548'), 'ValenciavrightU[1]': mpf('0.181359583480349125594396153707543'), 'ValenciavrightU[2]': mpf('-0.138124790730574777928762802038226')}

# Generated on: 2019-06-28
trusted_values_dict['GiRaFFEfood_HOGlobals'] = {'AD[0]': mpf('-0.94115744530567775184433060969805'), 'AD[1]': mpf('1.69321905451215397667294884427835'), 'AD[2]': mpf('0.0'), 'ValenciavU[0]': mpf('0.294521454719030203077048644263695'), 'ValenciavU[1]': mpf('0.163706555966521359089651866391384'), 'ValenciavU[2]': mpf('-0.975070156720603120338029391237849')}

# Generated on: 2019-06-28
trusted_values_dict['GiRaFFEfood_HO_Aligned_RotatorGlobals'] = {'AD[0]': mpf('-0.0000814205707660507544992115618536768'), 'AD[1]': mpf('0.0000801849028614445840261036910018663'), 'AD[2]': mpf('0.0'), 'ValenciavU[0]': mpf('-0.64340225872540982046101426632778'), 'ValenciavU[1]': mpf('0.633637754333239655611670762070977'), 'ValenciavU[2]': mpf('0.0')}
