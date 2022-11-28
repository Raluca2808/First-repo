# 1.Funcție care să calculeze și să returneze suma a două numere

x, y = float(input('Nr 1:')), float(input('Nr 2:'))


def suma(a, b):
    z = a + b  # calcul suma
    return z


print(suma(x, y))

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

x = int(input('Numar:'))


def par_impar(a):
    if a % 2 == 0:  # conditie
        return 'TRUE'
    else:
        return 'FALSE'


print(par_impar(x))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

nume = input('Nume=')
prenume = input('Prenume=')
nume_mijlociu = input('Nume_mijlociu=')


def caractere(x, y, z):
    nr = len(x) + len(y) + len(z)  # calcul nr caractere totale
    return nr


print('Numarul total de caractere este ', caractere(nume, prenume, nume_mijlociu))

# 4. Funcție care returnează aria dreptunghiului

lungime = float(input('Lungimea:'))
latime = float(input('Latimea:'))


def aria(x, y):
    if x > 0 and y > 0:
        rezultat = x * y
        return rezultat
    else:
        print('Introdu date valide')


print(aria(lungime, latime))

# 5. Funcție care returnează aria cercului

pi = 3.14
raza = float(input('Introdu raza cercului:'))


def arie_cerc(x):
    if x > 0:
        rezultat = pi * (x ** 2)  # ridicare la puterea:  **2
        return rezultat
    else:
        print('Introdu date valide')


print(arie_cerc(raza))

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

string = input('String:')
c = input('Introdu un caracter:')


def caracter(i, car):
    for i in string:
        if i == car:  # se verifica daca caracterul cerut se regaseste in string
            print('True')
            return i
    else:
        print('False')


caracter(string, c)


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def lower_upper(string):
    char_upper = 0
    char_lower = 0
    for char in string:
        if char.isupper():
            char_upper = char_upper + 1
        elif char.islower():
            char_lower = char_lower + 1
    print(f'Numarul de caractere mari este: {char_upper}')
    print(f'Numarul de caractere mici este: {char_lower}')


lower_upper('abc1ABCD!')

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

list1 = []
list2 = []


def fct(l1, l2):
    n = int(input('Cate numere doresti in lista?'))
    for i in range(0, n):
        element = int(input())
        l1.append(element)  # lista initiala
    for j in l1:
        if j > 0:  # verificare daca nr e pozitiv si apoi adaugare in lista de nr pozitive
            l2.append(j)
            j += 1
    return l2


print('Numerele pozitive:', fct(list1, list2))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

x, y = int(input('Scrie primul nr:')), int(input('Scrie al doilea nr:'))


def mare(a, b):
    if a > b:
        print(f'Primul numar({a}) este mai mare ca al doilea({b}).')
    elif b > a:
        print(f'Al doilea numar({b}) este mai mare decat primul({a}).')
    else:  # daca numerele sunt egale
        print(f'Numerele introduse sunt egale')


mare(x, y)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

numere = set({})  # setul initial
a = int(input('Cate numere doriti in set?(numere unice)'))  # nr de pozitii ale setului

for i in range(0, a):
    element = int(input('Introdu numar:'))
    numere.add(element)
print(f'Setul este:{numere}')

x = int(input('Scrie un nr:'))  # numarul verificat


def functie(j, nr):
    if j in nr:  # se verifica daca j este in set deja
        print('Nu am adaugat numarul in set.Acesta exista deja')
        return 'False'
    else:
        numere.add(j)  # se adauga j in set
        print(f'Am adaugat numarul nou in setul de numere {nr}.')
        return 'True'


print(functie(x, numere))
