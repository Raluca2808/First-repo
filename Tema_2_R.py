# # #1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else
# #
# # #1.
# # #if else : dacă se îndeplinește conditia pusa de 'if' se executa codul,
# # # 'else' dacă nu se îndeplinește prima condiție se ruleaza urmatorul cod
# #
# # #2.Verifică și afișează dacă x este număr natural sau nu
#
# x = int(input('Scrie un nr:'))
# if x > 0:
#     print('nr e natural')
# else:
#     print('nu este nr natural')
# #
# # #3 Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
#
# x = float(input('Scrie un nr:'))
# if x > 0:
#     print('Nr e pozitiv')
# elif x < 0:
#     print('Nr e negativ')
# else:
#     print('Nr e neutru')
#
# # #4 Verifică și afișează dacă x este între -2 și 13.
#
# x = float(input('Scrie un nr:'))
# if (x > -2) and (x < 13):
#     print('Nr este între - 2 și 13')
# else:
#     print('Nr nu este în intervalul [-2:13]')
# #
# # # #5 Verifică și afișează dacă diferența dintre x și y este mai mică de 5
#
# x = float(input('Scrie un nr:'))
# y = float(input('Scrie al doilea nr:'))
# if (x - y) < 5:
#     print('Diferenta numerelor e mai mica decât 5')
# else:
#     print('Diferenta numerelor e mai mare decât 5')
#
# # #6.Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
#
# x = float(input('Scrie un nr:'))
# if not (x > 5 and x < 27):
#     print('Numarul nu este in intervalul [5:27]')
# else:
#     print('Numarul este in intervalul [5:27]')
#
# # # #7.x și y (int)
# # # Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# # # mare.
#
# x = float(input('Scrie un nr:'))
# y = float(input('Scrie al doilea nr:'))
# if x == y:
#     print('Numerele introduse sunt egale')
# elif (x > y):
#     print('x este mai mare ca y')
# else:
#     print('y este mai mare ca x')
# #
# # # 8.
# # # X, y, z - laturile unui triunghi.
# # # Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
#
# x = float(input('x='))
# y = float(input('y='))
# z = float(input('z='))
# if x == y == z:
#     print('Triunghiul este isoscel.')
# elif x == y != z:
#     print('Triunghiul este echilateral.')
# elif x == z != y:
#     print('Triunghiul este echilateral.')
# elif x != z == y:
#     print('Triunghiul este echilateral.')
# else:
#     print('Triunghiul este oarecare.')
# #
# # # 9. Citește o literă de la tastatură.
# # # Verifică și afișează dacă este vocală sau nu
#
# litera = str(input('Litera testata este: '))
# vocale = 'a' or 'e' or 'i' or 'o' or 'u'
# if litera == vocale:
#     print(f'{litera} este vocala.')
# else:
#     print(f'{litera} este consoana.')
#
# # # 10.Transformă și printează notele din sistem românesc în >
# # # Peste 9 => A
# # # Peste 8 => B
# # # Peste 7 => C
# # # Peste 6 => D
# # # Peste 4 => E
# # # 4 sau sub => F
#
# nota = float(input('Nota:'))
# if nota > 4:
#     print('E')
# elif nota > 6:
#     print('D')
# elif nota > 7:
#     print('C')
# elif nota > 8:
#     print('B')
# elif nota > 9:
#     print('A')
# else:
#     print('F')
#
# # TEMA OPTIONALA SEDINTA 2
#
# # 1.Verifică dacă x are minim 4 cifre (x e int).
# # (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
#
# x = int(input('Introdu un numar din 4 cifre:'))
# y = len(str(x))
# if y >= 4:
#     print('Numarul are minim 4 cifre')
# else:
#     print('Numarul NU are minim 4 cifre')
#
# # 2.Verifică dacă x are exact 6 cifre.
#
# x = int(input('Introdu un numar din 6 cifre:'))
# y = len(str(x))
# if y == 6:
#     print('Numarul are 6 cifre.')
# else:
#     print('Numarul NU are 6 cifre.')
#
# # 3.Verifică dacă x este număr par sau impar (x e int).
#
# x = int(input('Scrie te rog un numar :) = '))
# if (x % 2) == 0:
#     print('Numarul tau este par.')
# else:
#     print('Numarul tau este impar.')
#
# # 4. x, y, z (int)
# # Afișează care este cel mai mare dintre ele?
#
# x = int(input('Scrie primul nr: '))
# y = int(input('Scrie al doilea nr: '))
# z = int(input('Scrie al treilea nr: '))
# if x > y and x > z:
#     print(f'{x} este cel mai mare nr.')
# elif y > x and y > z:
#     print(f'{y} este cel mai mare nr.')
# elif z > x and z > y:
#     print(f'{z} este cel mai mare nr.')
# else:
#     print('Minim doua numere sunt egale')
#
# # 5.
# # X, y, z - reprezintă unghiurile unui triunghi
# # Verifică și afișează dacă triunghiul este valid sau nu.
#
# x = float(input('Primul unghi:'))
# y = float(input('Al doilea unghi:'))
# z = float(input('Al treilea unghi:'))
# if (0 < x < 180) and (0 < y < 180) and (0 < z < 180) and (x + y + z == 180):
#     print('Valid')
# else:
#     print('Invalid')
#
# # 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# # ● Citiți de la tastatură un int x
# # ● Afișează stringul fără ultimele x caractere
# # Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
#
# prop = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Scrie un nr:'))
# print(prop[0:len(prop) - x])
#
# # 7.Același string. Declară un string nou care să fie format din primele 5 caractere
# # + ultimele 5
#
# prop = 'Coral is either the stupidest animal or the smartest rock'
# nou = prop[0:5] + prop[len(prop) - 5:]
# print(prop)
# print(nou)
#
# # 8. Același string.
# # ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# # este o funcție care te ajuta sa faci asta)
# # ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# # cuvant
# # ● output: 'Coral is either the stupidest animal or the smartest '
#
# prop = 'Coral is either the stupidest animal or the smartest rock'
# x = 'rock'
# index = prop.find(x)
# print(prop[0:index])
#
# # 9. Citește de la tastatura un string
# # Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# # Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
#
# string = input('Introduceti un cuvant: ')
# assert string[0].lower() == string[len(string) - 1].lower(), 'Primul si ultimul caracter NU sunt la fel'
# print('Primul si ultimul caracter sunt la fel')
#
# # '''10. Avand stringul '0123456789'
# # ● Afișați doar numerele pare
# # ● Afișați doar numerele impare
# # (hint: folositi slicing, controlați din pas)'''
# #
# string = '0123456789'
# print('Pare: ' + string[0:len(string):2])
# print('Impare: ' + string[1:len(string):2])
#
# # Exerciții Bonus (may need google) .
#
# # '''11. Joc ghicit zarul
# # Caută pe net și vezi cum se generează un număr random
# # Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# # Luați un numărul ghicit de la utilizator
# # Verificați și afișați dacă utilizatorul a ghicit
# # Veți avea 3 opțiuni
# # ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# # ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# # ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y'''
#
# import random
#
# random = random.randint(1, 6)
# dice_roll = int(input('Introduceti un numar de la 1 la 6: '))
#
# if random > dice_roll and 6 >= dice_roll >= 1:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {dice_roll} dar a fost {random}')
# elif random < dice_roll and 6 >= dice_roll >= 1:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {dice_roll} dar a fost {random}')
# elif random == dice_roll and 6 >= dice_roll >= 1:
#     print(f'Ai ghicit. Felicitari! Ai ales {dice_roll} si zarul a fost {random}')
# else:
#     print('Numar invalid')
