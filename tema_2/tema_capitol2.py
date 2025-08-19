#Tema 2 - Capitolul 2
#Ex1
a=int(input('Cat este a?'))
b=int(input('Cat este b?'))

print('a+b=', a+b)
print('a-b=' , a-b)
print('a*b=', a*b)
print('a/b=' , a/b)
print('a//b=' , a//b)
print('a%b =' , a%b)
print('\n')

#Ex2
lungime=int(input('cat este lungimea? '))
latime=int(input('Cat este latimea? '))

print('Perimetrul = ', 2*latime + 2*lungime)
print('Aria = ', lungime*latime)
print('\n')

#Ex3

a=int(input('Cat este a?'))
b=int(input('Cat este b?'))

print('a<b - ' , a<b)
print('a>b - ', a>b)
print('a==b - ', a==b)
print('\n')

#Ex4

a=int(input('Cat este a?'))
print('a este par - ' , a%2 == 0)
print('\n')

#Ex5

an_nastere=int(input('Care este anul nasterii?'))
print('Deci tu ai: ' , 2025 - an_nastere , 'ani')
print('\n')

#Ex6

a=int(input('Adauga nr secunde:'))
ore=a//3600
rest_secunde=a%3600
minute=rest_secunde//60
secunde=a%60
print('Rezultat:', ore , 'ore',',' , minute , 'minute', ',' , secunde, 'secunde')


