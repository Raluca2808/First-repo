# ______EXERCITII
# OBLIGATORII__________
# 1.
# variabila este o zona din memorie care retine informatii
# 2.
# declarare si initializare variabile


elev = 'Ana'
nota = 7
jumatate_nota = 3.5
raspuns = True
# printare variabile cu virgula
print(elev, ',', nota, ',', jumatate_nota, ',', raspuns)

# 3.
# afisare tip variabila
print(type(elev))
print(type(nota))
print(type(jumatate_nota))
print(type(raspuns))

# 4.
# suprascriere zecimala
jumatate_nota = round(jumatate_nota)
print(jumatate_nota)
print(type(jumatate_nota))

# 5.
# printare propozitii cu variabile
print('Primul elev este', elev)
print('Nota primita este', nota)
print('Nota lui Ion este', jumatate_nota)
print('Raspunsul calculatorului a fost', raspuns)

# 6.
# afisare numar caractere
nume = str(input('Numele este='))
prenume = str(input('Prenumele este='))
print('Numele complet are', len(nume + prenume), 'caractere')

# 7.
# afisare arie dreptunghi

lungime = int(input('lungimea='))
latime = int(input('latime='))
a = lungime * latime
print(f'Aria dreptungiului este {a}.')

# 8.
# numar aparitii 'the'

propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.count('the'))

# 9.
# 'the' trece in 'THE'
propozitie = 'Coral is either the stupidest animal or the smartest rock'
x = 'the'
print(propozitie.replace('the', x.upper()))

# 10.
# verificare continut (litere sau numere)
propozitie = 'Coral is either the stupidest animal or the smartest rock'
assert propozitie == str(propozitie)
print('String care contine litere')
assert propozitie == int(propozitie)
print('String care contine cifre')

# _______EXERCITII OPTIONALE______
# OPTIONALE SEDINTA 1

# ex 1 mijloc cuvant impar
cuvant = str(input('Scrie un cuvant impar='))
print(len(cuvant))
y = round(len(cuvant) // 2)
print(y)
print(cuvant[y])

# ex 2 string este palindrom
pal = str(input('Scrie un cuvant:'))
assert pal == pal[::-1]
print('este palindrom')

# #ex 3 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

x, y = (str(input('Introduceti o propozitie din 2 cuvinte: '))).split()
print(f' x = {x} \n y = {y}')

# #ex 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

prop = str(input('Inserati o propozitie: '))
first = prop[0]
x = prop[1:(len(prop) - 1)]
print(first, x.replace(first, first.upper()), prop[(len(prop) - 1)])

# ex 5
# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input('User=')
parola = input('Parola=')
nr = len(parola)
print('Parola pt userul ' + user + ' este ' + parola.replace(parola, '*') * len(parola) + ' si are ' + str(
    nr) + ' caractere')
