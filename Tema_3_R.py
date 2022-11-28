# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
#
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f'Notele muzicale:{note_muzicale}')
note_muzicale = note_muzicale[::-1]
print(f'Notele inversate sunt:{note_muzicale}')
note_muzicale.reverse()
print(f'Notele inversate:{note_muzicale}')

# 2. De câte ori apare ‘do’?
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.

x = [3, 1, 0, 2]
y = [6, 5, 4]
print(x + y)
x.extend(y)
print(x)

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.

x = [3, 1, 0, 2]
y = [6, 5, 4]
z = x + y
z.sort()
print(z)
z.pop(0)
print(z)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.

list = [3, 1, 0, 2, 6, 5, 4]
if len(list) > 0:
    print('nu e goala')
else:
    print('goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.

list = [3, 1, 0, 2, 6, 5, 4]
list.clear()
print(list)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.

if len(list) > 0:
    print('nu e goala')
else:
    print('goala')  # lista e goala

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
a = dict1.keys()
print(a)

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
nota_ana = dict1.get('Ana')
nota_gigel = dict1.get('Gigel')
nota_dorel = dict1.get('Dorel')
print('Ana a lua nota', nota_ana, 'Gigel a luat nota', nota_gigel, 'Dorel a luat nota', nota_dorel)

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
dict1['Dorel'] = 6
nota = dict1.get('Dorel')
print(f'Nota actualizata:{nota},{dict1}')

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1.pop('Dorel')
dict1.update({'Ionica': '9'})  # sau dict1['Ionica']= 9
print(dict1)

# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)  # elementul exista deja in set si nu il mai poate adauga

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

x = zile_sapt.isdisjoint(weekend)  # daca nu se intersecteaza returneaza True
if x == False:
    print('Weekend este un subset al zilelor săptămânii.')
else:
    print('Weekend nu este un subset al zilelor săptămânii.')

# 14. Afișează diferențele dintre aceste 2 seturi.

diferente = zile_sapt.difference(weekend)
print(f'Diferentele dintre cele 2 seturi sunt:{diferente}')

# 15. Afișază intersecția elementelor din aceste 2 seturi.

intersectie = zile_sapt.intersection(weekend)
print(f'Intersectia celor 2 seturi este:{intersectie}')
