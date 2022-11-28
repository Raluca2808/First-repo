#LIST#

list1=[10,20,30,'alex','andrei',50]
print(list1)
print(len(list1))
list1.remove(10)
print(list1)
list1.remove(list1[0])
print(list1)
list1.pop(0)
print(list1)
list1.extend([1,2,3,4])
print(list1)
list1 = list1 + [1,2,3,4]
print(list1)
list1.append('string')
print(list1)
list1.insert(2,2)
print(list1)
list2= [7,7,7]
list2.extend(list1)
print(list2)
list2.insert(3,list1)
print(list2)

#DICT#

dictionar = {'fructe': 'mere', 'legume': 'rosie'}
print(dictionar)
print(dictionar.values())
print(dictionar.keys())
dictionar.update({2:'sambata'})
print(dictionar)
print(dictionar.get(2))
valoare = dictionar.pop(len(dictionar)-1)
print(dictionar)

#SET#

masini= {'opel','volvo',1,2}
masini2={'opel','audi',5,6}
print(masini)
print(masini.intersection(masini2))
print(masini.difference(masini2))
masini.update([5,6,7,8])
print(masini)
print(type(masini))
newSet= set()
newSet.update({2,3,2})
print(newSet)

#TUPLE#

zile= ('vineri','marti','duminica')
print(zile)
luni='a','b','c'
print(luni)
print(type(luni))
mai,iunie,iulie = luni
print(mai,iunie,iulie)
mai2=luni
saptamana= ('luni','marti',('miercuri','joi'))
print(saptamana)
print(saptamana[2][1])


