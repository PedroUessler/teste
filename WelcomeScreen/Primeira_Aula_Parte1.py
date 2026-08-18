import sys

km = float(input('Km percorridos com o carro: '))
dias = int(input('Quantos dias ficou com o carro: '))
preco = (60 * dias) + (km * 0.15)

print (f'O preço total do alugel é ${preco:.2f}.')

print('---------------------------------------------------')
print()

b = 6
h = 5
A = (b*h) / 2
print(A)

print('---------------------------------------------------')
print()

def fibonnacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

n = int(input('Informe n: '))
print()
fibonnacci(n)

print('---------------------------------------------------')
print()

vetor_Lista = [0,1,2,3,4]
print(vetor_Lista)

print(type(vetor_Lista))
print(vetor_Lista[2])
vetor_Lista[2] = 9
print(vetor_Lista[2])

vetor_Lista[2] = 'Texto'
print(vetor_Lista[2])
print(vetor_Lista)

print(len(vetor_Lista))
vetor_Lista.append('Mais uma String')
print(len(vetor_Lista))
print(vetor_Lista)

for i in range(len(vetor_Lista)):
    print(vetor_Lista[i])

for x in vetor_Lista:
    print(x)

print(vetor_Lista)
print(vetor_Lista[3:6])
print(vetor_Lista[3:])
print(vetor_Lista[:5])

