""" Amarrações
Chamamos de amarração (binding) a associação entre entidades de programação. Veja alguns exemplos!

Variável amarrada a um valor.
Operador amarrado a um símbolo.
Identificador amarrado a um tipo.
O tempo em que a amarração ocorre é chamado de tempo de amarração. """

valor = 10

print(type(valor))

#resposta <class 'int'>

valor = 'a'

print(type(valor))

#resposta <class 'str'>

#Variaveis Globais e Locais 

def multiplicador(numero):
        a = 2 # esta variável tem escopo local
        print(f"Dentro da função, a variável vale: {a}")
        return a * numero

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {a}")

"""As variáveis globais têm o tempo de vida que é o de execução do programa, ao passo que as variáveis 
locais somente existem no intervalo de duração da função ou do bloco a que se limitam."""

#Python não tem conceito de constante, mas podemos nomear variaveis com todos os caracteres maiusculos ou acrescentando um c_ na frente, para diferenciar das demais

#Exemplo de constante:

NUMEROBASE = 100

PI = 3,14

c_variavelConstante = 'Não pode ser alterado'

#Exercicio:
# Passo 1: Definir a função imprimir_dados
def imprimir_dados(numero, texto):
    print("Número:", numero)
    print("Texto:", texto)
 
# Passo 2: Chamar a função imprimir_dados com dois argumentos
imprimir_dados(10, "Ola, mundo!") 

#Precedencias de operadores: () -> ** // -> * / % -> + - Exemplo:

resultado = 2 * 3 + (5 - 2) - 4 % 2 + (4 + 2)

#No exemplo acima, vai resolvido primeiro os parenteses, depois o mod e a multiplicação e por fim, somas e subtrações

print("Resultado:", resultado)

#Exercicio:
#Vamos criar um programa que calcule a média de três notas fornecidas pelo usuário, mostrando o resultado final com duas casas decimais. Veja o código com o qual vamos trabalhar!

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

print(f"A média é: {media:.2f}")

"""
Exercicio 2:
    Você foi designado para desenvolver um programa que solicita ao usuário que insira três números: um número inteiro, 
    um número de ponto flutuante e uma string representando um valor booleano (True ou False). 
    Seu objetivo é converter esses valores para os tipos corretos e exibi-los ao usuário de forma formatada. Você deve seguir as seguintes instruções: 

Solicite ao usuário que insira um número inteiro.
Solicite ao usuário que insira um número de ponto flutuante.
Converta os valores fornecidos pelo usuário para os tipos corretos (int, float e bool).
Exiba os valores convertidos ao usuário de forma formatada, mostrando o tipo de cada valor.

"""

#Solução:

numero_inteiro = int(input("Digite um numero inteiro:"))
numero_flutuante = float(input("Digite um numero float:"))
valor_booleano = input("Digite um valor booleano:")

valor_booleano = valor_booleano.lower()
valor_booleano = valor_booleano == "true"

print(f"- Número inteiro: {numero_inteiro} (tipo: {type(numero_inteiro).__name__})")
print(f"- Número flutuante: {numero_flutuante} (tipo: {type(numero_flutuante).__name__})")
print(f"- Valor booleano: {valor_booleano} (tipo: {type(valor_booleano).__name__})")

#Atribuições multiplas a variaveis:

x, y = 2, 5
print(x)
print(y)

#Exercicio: Valor total da compra:

valor_hamburguer = 13.00
valor_batataFrita = 8.00
valor_refrigerante = 5.00

qtd_hamburguer = int(input("Digite a quantidade de Hamburguer desejado:"))
qtd_batataFrita = int(input("Digite a quantidade de Batata Fritas desejada:"))
qtd_refrigerante = int(input("Digite a quantidade de Refrigerantes desejado:"))

valor_total = valor_hamburguer * qtd_hamburguer + valor_batataFrita * qtd_batataFrita + valor_refrigerante * qtd_refrigerante

print(f"O valor total é: R$ {valor_total:.2f}")

