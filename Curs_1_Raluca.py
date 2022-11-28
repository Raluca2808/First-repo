# '''
# simulare bancomat
# '''
expectedUserName = 'andrei'
expectedParola= '1234'
sold= 200
# userName= input('user name:')
# assert expectedUserName == userName,'Username invalid'
# print('username ok')
# parola= input('pune parola:')
# assert expectedParola == parola,'Parola invalida'
# print ('parola ok')
# plata = int(input('Suma dorita:'))
# assert sold >= plata,'Fonduri insuficiente'
# print('suma ok')
print(f'sold= {sold}')
print(type(sold))
print(type(expectedUserName))
sold2='200'
print(type(sold2))
assert type(sold)==type(sold2)

myString= 'fiecare caracter are propriul sau index'
print(len(myString))
print(myString[0])
print(myString[-1])
print(myString[-3])
print(myString[5:8])
print(myString[::-1])
print(myString[:-3])
slicedString= slice(2)
print(myString[slicedString])
print(myString[:2])