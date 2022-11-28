# exercitii obligatorii
#
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

for masina in masini:
    print(f'Masina mea preferata este {masina}')

i = 0
while i < len(masini):
    print(f'masina mea preferata este {masini[i]}')
    i += 1

# 2. Aceeași listă:
# Folosește un for else
# În for
#
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
    print(masini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for marca in masini:
    if marca == 'Mercedes':
        print(f'Am găsit masina dorita')
        break
    else:
        print(f'Am găsit masina {masina}. Mai cautam.')

# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for marca in masini:
    if marca == 'Trabant' or marca == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}. ')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
#
# ● Printează Modele vechi: x.
# ● Modele noi: x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for marca in masini:
    if marca == 'Trabant' or marca == 'Lastun':
        masini_vechi.append(marca)
        masini.remove(marca)
        masini.append('Tesla')
print(f'Vechi: {masini_vechi} ')
print(f'Noi:{masini}')

# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Va putem oferi:{masina}')

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
for trei in numere:
    if trei == 3:
        i = i + 1
print(f'Numarul 3 apare de {i} ori')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for i in numere:
    suma = suma + i
print(f'Suma nr = {suma}')

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_mare = numere[0]
for nr in numere:
    if nr > nr_mare:
        nr_mare = nr
print(f'Cel mai mare nr este {nr_mare}')

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
negativ = []
for i in numere:
    if i > 0:
        i = i - i * 2
    negativ.append(i)
print(negativ)

#################exercitii optionale


# 1.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if i % 2 == 0:  # se verifica valorile pt listele par/impar
        numere_pare.append(i)
    elif i % 2 != 0:
        numere_impare.append(i)
    if i > 0:  # se verifica valorile pt listele negativ/pozitiv
        numere_pozitive.append(i)
    elif i < 0:
        numere_negative.append(i)
# printare liste de la capat
print(
    f'Lista numere pare:{numere_pare}\nLista numere impare:{numere_impare}\nLista numere pozitive:{numere_pozitive}\nLista numere negative:{numere_negative}')

# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4

list = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
i = 0
for i in range(len(list) - 1):
    for j in range(len(list) - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)

# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
#
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!

import random

numar_secret = random.randrange(1, 30)
numar_ghicit = None
# print(f'Nr secret:{numar_secret}')
numar_ghicit = int(input('Introdu un numar intre 1 si 30:'))
while numar_ghicit < numar_secret:
    print('Nr secret e mai mare')
    break
else:
    if numar_ghicit > numar_secret:
        print('Nr secret e mai mic')
    else:
        print('Felicitari! Ai ghicit!')

# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

nr = int(input('Numar:'))
i = 0
for i in range(1, nr + 1):
    print(str(i) * i)

# 5.
# tastatura_telefon = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este:{tastatura_telefon[i][j]}')
