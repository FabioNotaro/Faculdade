
def soma(a, b):
    return a + b

resultado = soma(3, 5)

print("O resultado da soma é:", resultado)

""" Variaveis com tipagem dinamica:
No primeiro momento, a variável 'x' recebeu um valor inteiro, sendo assim, do tipo inteiro, mas após isso, 
recebeu um valor do tipo string, alterando assim, seu tipo para string. """

x = 10

print("O tipo da variavel x é:", type(x))

x = "Agora é uma string"

print("O tipo da variavel x agora é:", type(x))

# Exemplo de uso de biblioteca: no caso, 'Math'

import math

numero = 16

raiz_quadrada = math.sqrt(numero)

print("A raiz quadrada de", numero, " é:", raiz_quadrada)

# Programação Procedural:

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
print("Fatorial de 5 (Procedural):", fatorial(5))

# Programação Orientada a Objeto / POO

class Fatorial:
    def calcular(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calcular(n-1)
        
f = Fatorial()

print("Fatorial de 5 (orientado a objetos):", f.calcular(5))

# Exemplo de Loop

a = 0

for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3

print (a)

# Programa simples para calculo de 2 médias

nota1 = 8
nota2 = 9

media = (nota1 + nota2) / 2

print("A média das notas é:", media)