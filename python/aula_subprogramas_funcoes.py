#exemplo de funcoes:

escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    res = func1(10)
 
else:
    def func2(x):
        return x + 2
    res = func2(10)
 
print(res)

#Validando CPF

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    if int(cpf[9]) != digito_verificador_1:
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    if int(cpf[10]) != digito_verificador_2:
        return False

    return True
 
cpf = "123.456.789-09"
if validar_cpf(cpf):
    print(f"O CPF {cpf} é válido.")
else:
    print(f"O CPF {cpf} é inválido.")


#Funcao que busca o maior elemento de uma lista de inteiros

listaNumeros = [12, 13, 59, 38, 10, 32, 7]
tamanhoLista = len(listaNumeros)
contador = 0

def buscaMaior(listaNumeros):
    if len(listaNumeros) <= 1:
        return listaNumeros[0]

    maior_elemento = listaNumeros[0]
    for numero in listaNumeros[1:]:
        if numero > maior_elemento:
            maior_elemento = numero

    return maior_elemento

maior_elemento = buscaMaior(listaNumeros)

print(f"O maior elemento encontrador é: {maior_elemento}")

#Buca Maior Recursivo

listaNumeros = [12, 13, 59, 38, 10, 32, 7]

def maiorNumero(listaNumeros):
    
    if len(listaNumeros) == 1:
        return listaNumeros[0]
    else:
        # Divide a lista recursivamente
        maiorRestante = maiorNumero(listaNumeros[1:])
        # Compara o primeiro elemento com o maior do restante da lista
        if listaNumeros[0] > maiorRestante:
            return listaNumeros[0]
        else:
            return maiorRestante

maior_elemento = maiorNumero(listaNumeros)

print(f"O maior elemento encontrador é: {maior_elemento}")

#Função Recursiva

def contagemRegressiva(x):
    print(x)
    if(x > 0):
        x = x - 1
        contagemRegressiva(x)
    else:
        print('acabou')

contagemRegressiva(10)


#Funcao que retorna o n-ésimo termo da sequencia de Fibonacci

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
res = fibo(20)
print(res)