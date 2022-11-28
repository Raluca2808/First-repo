################ Exceptii
# try:
#     list=[1,2,3]
#     list[6]
#
# except IndexError as e:
#     print(e)
# print('am ajuns aici')
#
# raise IndexError('eroare fortata')

# ________________________________________________________________________________
# MOSTENIRE
# class chef:
#     def make_salad(self):
#         print('chef: salad')
#     def make_fries(self):
#         print('fries')
# class jap(chef):
#     def make_sushi(self):
#         print('sushi')
#     def make_salad(self):
#         print('jap chef:salad')
# class ita(chef):
#     def make_pizza(self):
#         print('pizza')
#
# chef=chef()
# japchef=jap()
# itachef=ita()
# chef.make_fries()
# japchef.make_sushi()
# itachef.make_pizza()
# japchef.make_salad()


# _---------------------------------------------------------------------------
# polimorfism


# print(len('abc'))
# print(len([1,2,3,4]))

# def add(x,y,z=0):
#     return x+y+z
#
# print(add(2,3))
# print(add(2,3,5))

# class Adunare():
#
#     def add(self,x,y,z=0):
#         return x+y+z
#
# adunare=Adunare()
# print(adunare.add(5,6))

# ==================================================================
# ABSTRACTIZARE
# --------------------------------------

# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def sleep(self):
#         raise NotImplementedError
#
#     def pri(self):
#         print('animal')
#
# class Dog(Animal):
#     def sound(self):
#         print('ham ham')
#
#     def sleep(self):
#         print('lalalal')
#
#
# class Cat(Animal):
#     def sound(self):
#         print('miau miau')
#
#     def sleep(self):
#         print('prrrrrrr')
#
#
# dog = Dog()
# cat = Cat()
# dog.sleep()
# cat.sleep()
# dog.pri()
# cat.pri()

# ______________________________________________________________________________________________
######### INCAPSULARE
#
# class car:
#     __color='gri'
#     model='ema'
#     def get_color(self):
#         return self.__color
#     def set_color(self,culoare_dorita):
#         self.__color= culoare_dorita
#         self.__mesaj(f'culoarea a fost schimbata in {culoare_dorita}')
#     def __mesaj(self,mesaj):
#         print(mesaj)
#
# masina=car()
# masina.set_color('rosu')

# EXERCITIU


# class Triunghi():
#     baza=0
#     inaltime=0
#     __arie=0
#     def __init__(self,baza,inaltime):
#         self.baza=baza
#         self.inaltime=inaltime
#     def getArie(self):
#         self.__calcArie()
#         return self.__arie
#
#     def __calcArie(self):
#         self.__arie=(self.baza * self.inaltime)/2
# triunghi=Triunghi(2,4)
# print(triunghi.getArie())


#__________________________________________________________________________________
# INCAPSULARE OPTIONAL

# class CarPy:
#
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.getter
#     def color(self):
#         print(f'Getter: culoarea este {self.__color}')
#         return self.__color
#
#     @color.setter
#     def color(self, color):
#         print(f'Setter: cul este {color}')
#         self.__color = color
#
#     @color.deleter
#     def color(self):
#         print(f'Deleter:Am sters cul')
#         self.__color = None
#
#
# car = CarPy('rosu')
# car.color = 'green'
# car.color
# del car.color
# car.color
