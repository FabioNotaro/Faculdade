#Condicionais:

#Um sistema simples para orientação sobre a vacina

idade_criança = eval(input("Informe a idade da criança: \n"))

if idade_criança < 5:
    print("A criança deve ser vacinada contra a gripe")
    print("Procure o posto de saúde mais próximo")
elif idade_criança == 5:
    print("A vacina estará disponível em breve")
else:
    print("A vacina so ocorrerá daqui a 3 meses")
    print("Informe-se novamente após o prazo")

print("Cuide da sua saúde sempre")


#Repetições:
#For:
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    quadrado = numero ** 2

    print(f"O quadrado de {numero} é: {quadrado}")

#Contador de letras de uma palavra com for:

palavra = input("Digite a palavra que você deseja:")
letra_para_contagem = input("Digite a letra que você deseja contar:")
contador = 0

for letra in palavra:
    if(letra_para_contagem == letra):
        contador += 1

print(f"A letra {letra_para_contagem} aparece {contador} vezes, na palavra {palavra}")

#Exemplo uando o Range:

numero = 5

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

#Criando a tabuada multiplicação do 1 ao 10 utilizando o Range:

for numero_principal in range(1, 11):
    print(f"Tabuada do número: {numero_principal} \n")
    for multiplicador in range(1, 11):
        resultado_multiplicacao = numero_principal * multiplicador
        print(f"{numero_principal} x {multiplicador} = {resultado_multiplicacao}")


#While:

palavra = input('Digite uma palavra:')

while palavra != 'Sair':
    print('Você entrou no loop')
    palavra = input('Digite Sair para encerrar o loop')

print("Você encerrou o loop com sucesso!")

#arquivo temporario

"""Crie um projeto no PYCHARM.
Utilize uma estrutura de for para gerar os números a serem testados.
Gere o número formado pelos algarismos menos significativos.
Gere o número formado pelos algarismos mais significativos.
Obtenha a raiz somando os dois números obtidos.
Eleve a raiz ao quadrado e valide se é igual ao número que está sendo testado.
Se for igual, exiba o número que está sendo testado, os números dos algarismos mais e menos significativos e a raiz.
Ao término do loop, informe que terminou e mostre o valor final da variável do for."""

for num in range (1000, 10000):
    menor = num % 100
    maior = num // 100
    raiz  = menor + maior

    if(raiz * raiz) == num:
        print(num)
        print(maior)
        print(menor)
        print(raiz)
print('Terminou')
print(num)

"""Altere então o programa, de modo que os valores 32 e 99 da otimização 
possam ser obtidos de maneira automática, sem nenhum cálculo anterior à execução do programa."""

#O programa abaixo é otimizado, pois faz a busca entre 32 e 99 (que são as menores e maiores raizes entre  1000 e 10000, imprimindo o mesmo resultado)

start = int(1000**0.5) 

if start * start < 1000: 
	start += 1

end = int(9999**0.5)

for raiz in range (start, end + 1): 
	num = raiz * raiz
	menor = num % 100
	maior = num // 100
 
	if (menor +maior) ==raiz:
		print(num)
		print(menor)
		print(maior)
		print(raiz)
print('terminou')
print('saiu ', raiz) 

