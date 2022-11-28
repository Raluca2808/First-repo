# def contbancar(user,parola,plata):
#     i=0
#     while i<3:
#         if user == 'raluca':
#             if parola=='2424':
#                 if plata <= 200:
#                     print('tranzactie reusita')
#                     break
#                 else:
#                     print('Fonduri insuficiente')
#                     break
#             else:
#                 print('parola gresita')
#                 parola=input('parola:')
#                 i=i+1
#         else:
#             print('user gresit')
#             user= input('id:')
#             i=i+1
#     print('Ms!o zi frumoasa')
# contbancar(input('id:'),input('parola:'),int(input('sold:')))
#
#
#
def bubblesort(list):
    for i in range (len(list)-1):
        for j in range (len(list)-1):
            if list[j] > list[j+1]:
                list[j],list[j+1]= list[j+1],list[j]
    return list
# list=[3,6,8,1,4,9,0,10] #bublesort
# lista_sortata= bubblesort(list)
# print(lista_sortata)

# # def max(list):
#     listSort=bubblesort(list)
#     return listSort[-1]
# maxim=max([3,6,8,1,4,9,0,10])
# print(maxim)

# def max2(list):
#     maxim=0
#     for i in range (len(list)):
#         if maxim<list[i]:
#             maxim=list[i]
#     return maxim
# maxim=max2([3,6,8,1,4,9,0,10])
# print(maxim)

# import random
# def dice_roll():
#     zar = [1,2,3,4,5,6]
#     dice= random.choice(zar)
#     numar= int(input('un nr:'))
#
#     if numar < dice:
#         print(f'nu e corect,nr este {dice} iar tu ai ales{numar}')
#     elif numar > dice:
#         print(f'nu e corect,nr este {dice} iar tu ai ales {numar}')
#     else:
#         print('numar corect')
# dice_roll()

