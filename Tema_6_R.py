# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

class cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):  # constructor
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Culoarea cercului este {self.culoare} iar raza este {self.raza}')

    def aria(self):
        __pi = 3.14
        return __pi * self.raza * self.raza
        print(f'Aria cercului este {__pi * self.raza * self.raza}')

    def diametru(self):
        return (2 * self.raza)
        print(f'Diametrul cercului este {2 * self.raza}')

    def circumferinta(self):
        __pi = 3.14
        return 2 * (__pi * self.raza)
        print(f'Circumferinta cercului este {2 * (__pi * self.raza)}')


cercul_meu = cerc(int(input('Raza cerc=')), input('Culoare cerc='))
print(cercul_meu.descriere_cerc())
print(cercul_meu.aria())
print(cercul_meu.diametru())
print(cercul_meu.circumferinta())


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
#
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

class dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Lungimea este {self.lungime}\nLatimea este {self.latime}\nCuloarea este {self.culoare}')

    def arie(self):
        a = self.lungime * self.latime
        print(f'Aria este {a}')

    def perimetru(self):
        b = (2 * self.lungime) + (2 * self.latime)
        print(f'Perimetrul este {b}')

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


dreptunghiul_meu = dreptunghi(int(input('Lungimea este:')), int(input('Latimea este:')), input('Culoarea este:'))
print(dreptunghiul_meu.descrie())
print(dreptunghiul_meu.arie())
print(dreptunghiul_meu.perimetru())
print(dreptunghiul_meu.schimba_culoarea(input('Schimba culoarea in:')))
print(dreptunghiul_meu.descrie())


# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele este: {self.nume}, Prenumele este: {self.prenume}, Salariul este:{self.salariu}')

    def nume_complet(self):
        print(f'Numele complet este: {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este:{self.salariu}')

    def salariu_anual(self):
        print(f'Salariul anual este:{self.salariu * 12}')

    def marire_salariu(self, procent):
        print(f'Marirea de salariu este: {(self.salariu / 100) * procent}')


angajatul_meu = Angajat('petcu', 'cosmin', 1000)
print(angajatul_meu.descrie())
print(angajatul_meu.nume_complet())
print(angajatul_meu.salariu_lunar())
print(angajatul_meu.salariu_anual())
print(angajatul_meu.marire_salariu(int(input('introdu marirea de salariu:'))))


# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, suma):
        if suma < self.sold:
            self.sold = self.sold - suma
            print(f'Dupa debitare soldul este:{self.sold} lei')
        else:
            print(f'Suma depaseste soldul actual!')

    def creditare_cont(self, credit):
        self.sold = self.sold + credit
        print(f'Dupa creditare soldul este:{self.sold} lei')


contul_meu = cont(123456, 'Petcu Cosmin', 1000)
print(contul_meu.afisare_sold())
print(contul_meu.debitare_cont(int(input('Suma debitata:'))))
print(contul_meu.creditare_cont(int(input('Suma creditata:'))))
