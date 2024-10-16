

#Funcao para calcular fatorial não recursivo

numeroDigitado = int(input('Digite o numero que voce gostaria de calcular o Fatorial:'))

def fatorial(numero):
    res = 0

    while numero > 1:        
        if(res == 0):
            res = numero
        numero = numero - 1
        res = res * numero        
    return res

res = fatorial(numeroDigitado)
print(f"O resultado é: {res}")

#Fatorial recursivo

numeroDigitado = int(input('Digite o numero que voce gostaria de calcular o Fatorial:'))

def fatorial2(n):
    if n == 0 or n == 1:
         return 1
    else:
         return n*fatorial2(n-1)
    
res = fatorial2(numeroDigitado)
print(f"O resultado é: {res}")