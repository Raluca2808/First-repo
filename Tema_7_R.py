from abc import abstractmethod

# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

class FormaGeometrica():
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')
# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Am sters latura')
        self.__latura = None

    def aria(self):
        print(f'Aria este: {self.__latura * self.__latura}')

# Creează un obiect de tip Patrat și joacă-te cu metodele lui

patrat = Patrat(2)
patrat.latura
patrat.aria()
patrat.latura = 3
patrat.latura
# del patrat.latura
# patrat.latura
patrat.aria()
patrat.descrie()

# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din
# clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Noua raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Am sters raza')
        self.__raza = None

    def aria(self):
        print(f'Aria este: {self.__raza * self.__raza * FormaGeometrica.PI}')

    # POLYMORPHISM
    # Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
    def descrie(self):
        print('Eu nu am colturi')

# Creează un obiect de tip Cerc și joacă-te cu metodele lui

cerc = Cerc(4)
cerc.raza
cerc.aria()
cerc.raza = 2
cerc.raza
cerc.aria()
del cerc.raza
cerc.raza
cerc.descrie()







