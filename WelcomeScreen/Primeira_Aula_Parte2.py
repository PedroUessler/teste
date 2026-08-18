import sys

numeros = sys.argv[1:]

print(numeros)

x, y = int(sys.argv[-3]), int(sys.argv[-2])
print(x,y)

soma = int(numeros[x]) + int(numeros[y])
print(soma)


