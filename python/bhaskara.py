import math

def calcula_delta (a, b, c):
    delta = b ** 2 - 4 * a * b * c
    return delta

def calcula_raizes(a, b, c):
    delta = calcula_delta(a, b, c)
    print(f'Delta = {delta}')
    if(delta > 0):
        raiz1 = -b - math.sqrt(delta) / (2 * a)
        raiz2 = b - math.sqrt(delta) / (2 * a)

        return (raiz1, raiz2)
    elif(delta == 0):
        raiz = b - math.sqrt(delta) / (2 * a)

        return raiz
    else:
        #Deltas negativos
        return 'Equação sem raizes reais, delta com valor negativo'
    
a = int(input('insira o coeficiente de a:'))
b = int(input('insira o coeficiente de b:'))
c = int(input('insira o coeficiente de c:'))

resultado =  calcula_raizes(a, b, c)
print(f'O resultado da equação do segundo grau é: {resultado}')