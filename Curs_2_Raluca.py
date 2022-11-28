# # optiune = int(input('alege optiunea'))
# # if optiune == 0:
# #     print('meniul anterior')
# # elif optiune == 1:
# #     print('ati ales ro')
# # elif optiune == 2:
# #     print('ati ale eng')
# # else:
# #     print('mai incearca')
# # pentru un bancomat verificam user si parola.userul are doar 2 incercari atat pt username cat si pt parola
# #userul doreste sa scoata o anumita suma acesta avand un sold curent .suma dorita trebuie sa fie mai mica sau egala cu soldul
# #daca se introduce o suma prea mare poate sa aleaga daca doreste sa reicerce sau nu
# expected_user = 'ion'
# expected_pass = '1234'
# sold = 40000.50
# username = input('introduceti user:')
# if username == expected_user:
#     print('user corect')
# else:
#     print('username incorect. incercati din nou')
#     username = input('introduceti user:')
#     assert username==expected_user, 'user incorect. o zi buna'
#     print('user corect')
# parola= input('introdu parola')
# if parola==expected_pass:
#     print ('parola corecta')
# else:
#     print('parola incorecta')
#     parola = input('introdu parola')
#     assert parola== expected_pass, 'parola incorecta.o zi buna'
#     print('parola corecta')
# suma= float(input('suma dorita:'))
# if suma<=sold:
#     print('ridicati banii')
# else:
#     print('fonduri insuficiente')
#     reincercare = input('doriti sa continuati? da sau nu?')
#     if reincercare == 'da':
#         suma=float(input('introdu suma dorita'))
#         assert suma<=sold,'suma introdusa e prea mare'
#         print('ridicati banii')
#     elif reincercare=='nu':
#         print('la revedere')
#     else:
#         assert False, 'eroare'
#

import random
zar = [1,2,3,4,5,6]
dice_roll= random.choice(zar)

numar= int(input('un nr:'))

if numar < dice_roll:
    print(f'nu e corect,nr este {dice_roll} iar tu ai ales{numar}')
elif numar > dice_roll:
    print(f'nu e corect,nr este {dice_roll} iar tu ai ales {numar}')
else:
    print('numar corect')