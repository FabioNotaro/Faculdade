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

