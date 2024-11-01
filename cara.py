#Exemplos meu:

# contador = 0

# while contador < 10:
#     print(f'Valor do contador é {contador}')
#     contador += 1

# contador = 0

# while contador < 10:
#     contador += 1
#     print(f'Valor do contador é {contador}')    
# else:
#     print(f'Fim do while e o valor do contador é {contador}')


# print('-------------------------------------------------------------------------------------')


# lista = [1, 2, 3, 4, 5]

# print(item)


# for item in lista:
#     print(item)
# else:
#     print('Todos os items foram exibidos com sucesso')




# print('-------------------------------------------------------------------------------------')




# carro = ['gol', 'palio', 'celta', 'fusca']

# for carro in carro:

#     print(carro)


# for i in range(4):
#     print(i)
#     print(carro[i])

# for i in "fusca":
#     print(i)



# print('-------------------------------------------------------------------------------------')

#Exemplo Professor:


#  for x in range(10):
#         print(x) # imprime de 0 a 9



# print('-------------------------------------------------------------------------------------')

# 1.Faça um programa que imprima todos os números de 1 até 100.

# x = 1
# while x <= 100:
#     print(x)
#     x = x + 1


#Exemplo 1 Professor:

#   x = 0
#     while x < 10:
#         print(x)
#         x += 1 # é a mesma coisa que x = x + 1

#Exemplo 2 Professor:

#  for x in range(1,101):
#         print(x, end = " ")


#print('-------------------------------------------------------------------------------------')

#2. Faça um programa que imprima todos os números pares de 100 até 1.


# x = 100
# while x >= 1:
#     print(x)
#     x = x - 1


#Exemplo Professor:

#  for x in range(100,0,-2):
#         print(x, end = " ")


#print('-------------------------------------------------------------------------------------')

#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.


# for m in range (1,500):

#     if (m % 5) == 0:
#         print(m)



#print('-------------------------------------------------------------------------------------')

#4. Faça umprograma que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.

# for x in range (3):
#     nome = str(input ('Digite seu nome: '))
#     idade = float(input ('Digite a idade: '))
#     sexo = str(input ('Digite o sexo: '))
#     if sexo == "m" and idade > 21:
#         print(f'O nome da pessoa é: {nome}')
#     else:
#         print(f'Menor de idade.')


#print('-------------------------------------------------------------------------------------')


#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.



# primeironum = int(input("Primeiro número: "))
# segundonum = int(input("Segundo número: "))

# x = 1
# r = 0
# while x <= segundonum:
#     r = r + primeironum
#     x = x + 1
# print(f"{primeironum} x {segundonum} = {r}")




#print('-------------------------------------------------------------------------------------')

#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.



# termo = int(input("Digite o numero de termos: "))

# termo1 = 0
# termo2 = 1

# print('{} * {}'.format(termo1, termo2), end='')

# cont = 3
# while cont <= 20:
#     termo3 = termo1 + termo2
#     print(' * {}'.format(termo3), end='')
#     termo1 = termo2
#     termo2 = termo3
#     cont += 1
# print(' = final')

# Exemplo professor ----------------------------------------------------------------------------

#   anterior = 0
#     atual = 1
#     print(atual, end = " ")
#     for x in range(19):
#         proximo = anterior + atual
#         print(proximo, end = " ")
#         anterior = atual
#         atual = proximo


#print('-------------------------------------------------------------------------------------')

#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.

# soma = 0

# for x in range (15):
#     nome = str(input("Digite o nome do aluno: "))
#     nota1 = float(input("Digite a nota 1 do aluno: "))
#     nota2 = float(input("Digite a nota 2 do aluno: "))

#     media = (nota1 + nota2) / 2
#     soma = soma + media

#     print(f'A nota da prova 1 é {nota1} e a nota de prova2 é {nota2} sendo sua média: {media}')

# mediageral = soma / 3

# print(f'A média geral de turma é: {mediageral}')



#print('-------------------------------------------------------------------------------------')

#8. Faça um programa que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRRF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto


# for x in range (3):
#     nome = str(input("Digite seu nome: "))
#     salariobruto = float(input("Digite o salário bruto: "))
   
#     if salariobruto < 1300:
#         print(f'O Fulano {nome} está isento de declaração.')

#     if salariobruto >= 1300 and salariobruto < 2300:
#         print(f'O Fulano {nome} ira pagar {salariobruto * 10 / 100} do seu salário.')

#     if salariobruto >= 2300:
#         print(f'O Fulano {nome} ira pagar {salariobruto * 15 /100} do seu salário.')


#print('-------------------------------------------------------------------------------------')

#9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.


#  qtdePessoasExcelente = 0
#     somaIdadeExcelente = 0
#     qtdePessoasRegular = 0
#     qtdePessoasBom = 0
#     qtdeTotalPessoas = int(input('Número de Pessoas: '))
#     for x in range(qtdeTotalPessoas):
#         idade = int(input('Idade: '))
#         opiniao = int(input('Opinião ([3]-Excelente - [2]-Bom - [1]-Regular): '))
#         match(opiniao):
#             case 1: qtdePessoasRegular += 1
#             case 2: qtdePessoasBom += 1
#             case 3:
#                 qtdePessoasExcelente +=1
#                 somaIdadeExcelente += idade
#             case _: print('Opção Inválida!')
#     print(f'Média idade excelente: {somaIdadeExcelente/qtdePessoasExcelente}')
#     print(f'Qtde de pessoas regular: {qtdePessoasRegular}')
#     print(f'% de pessoas que responderam bom: {qtdePessoasBom/qtdeTotalPessoas*100}%')

#print('-------------------------------------------------------------------------------------')

#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times; ------ok
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.
    
# somatimesi = 0
# mediatimesi= 0
# somatimesp = 0
# mediatimesp = 0

# somamediaidadet = 0
# somamediapesot = 0

# maior = 0
# menor = 1000

# print('\n')

# for p in range (3):
#     print(f'---------------------------------------')
#     for j in range (2):

#         print(f'time:{p+1}')
#         print(f' jogador:{j+1}')

#         idade = int(input("Digite a idade do jogador: "))
#         peso = float(input("Digite o peso do jogador: "))
    
#         if peso > maior:
#             maior = peso

#         if idade < menor:
#             menor = idade

#         print('\n')

#         somatimesi += idade
#         somatimesp += peso


#     mediatimesi = somatimesi / 2
#     mediatimesp = somatimesp / 2

#     somamediaidadet += mediatimesi
#     somamediapesot += mediatimesp

        


#     print(f'====================================')

#     print(f'O peso médio do time é: {mediatimesp}')
#     print(f'A idade média do time é: {mediatimesi}')
#     print(f'O atleta mais pesado do time tem: {maior} kg')
#     print(f'O atleta mais jovem do time tem: {menor} anos.')
    
#     print(f'====================================')
    
    
#     somatimesi = 0
#     mediatimesi= 0
#     somatimesp = 0
#     mediatimesp = 0

#     maior = 0
#     menor = 1000

#     print('\n')

# mediatodospi = somamediaidadet / 3
# mediatodospp = somamediapesot / 3

# print('\n')

# print(f'O peso médio de todos os participantes é: {mediatodospp} e a idade média de todos os participantes é:{mediatodospi}')

# print('\n')

 #print('-------------------------------------------------------------------------------------')   
#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.

#Exemplo 1:

# contador = 100

# while contador < 200:
#     contador += 1

#     print(f'{contador}')

# print('\n')

# print(f'====================================')

# print('\n')

# #Exemplo 2:

# total = 100

# for i in range (100, 200):
#     total = total + 1
#     print(total)


#print('-------------------------------------------------------------------------------------') 

#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.


# a = 500000000
# b = 700000000
# ano = 0

# while a < b:
# 	a += a * 0.03
# 	b += b * 0.02
# 	ano += 1

# print ( "O Pais A ultrapassa o pais B em %d anos" %ano )


#print('-------------------------------------------------------------------------------------') 

#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:

#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7

#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:

#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• A média de consumo dos tipos 1.
#• A média de consumo dos tipos 2.


# total_consumo_residencial = 0
# total_consumo_comercial = 0
# total_consumo_industrial = 0

# total_consumidores_tipo1 = 0
# total_consumidores_tipo2 = 0

# total_consumo_tipo1 = 0
# total_consumo_tipo2 = 0

# #preco_por_kwh = 0

# print('\n')
# for x in range(4):
#     print(f'#####################################################################################################################')
#     print(f'Consumidor:{x+1}')
#     print('\n')

#     erro=True
#     while erro == True:
#         try:
#             numero_consumidor = int(input("Digite o número do consumidor: "))
#             erro=False
#         except ValueError:
#             print(f'Valor Invalido, Digite apenas numeros inteiros.')
#             erro=True
#     erro=True
#     while erro == True:
#         try:
#             quantidade_kwh = float(input("Digite a quantidade de kWh consumidos durante o mês: "))
#             erro=False
#         except ValueError:
#             print(f'Valor Invalido, Digite o valor em números reais.')
#             erro=True
#     erro=True
#     while erro == True:
#         try:
#             tipo_consumidor = int(input("Digite o tipo de consumidor (1 - residencial, 2 - comercial, 3 - industrial): "))
#             if tipo_consumidor < 1 or tipo_consumidor > 3:
#                 raise ValueError('Valor inválido')
#             erro=False
#         except ValueError:
#             print(f'Valor Invalido, Digite apenas o número 1 , 2 ou 3.')
#             erro=True
#         finally:
#             print(f'Insira a informação do próximo consumidor!!!!!!')

#     if tipo_consumidor == 1:
#         preco_por_kwh = 0.3
#         total_consumo_residencial += quantidade_kwh
#         total_consumidores_tipo1 += 1
#         total_consumo_tipo1 += quantidade_kwh
#     elif tipo_consumidor == 2:
#         preco_por_kwh = 0.5
#         total_consumo_comercial += quantidade_kwh
#         total_consumidores_tipo2 += 1
#         total_consumo_tipo2 += quantidade_kwh
#     elif tipo_consumidor == 3:
#         preco_por_kwh = 0.7
#         total_consumo_industrial += quantidade_kwh
    
    
#     custo_total = quantidade_kwh * preco_por_kwh

#     print('\n')
#     print('----------------------------------------------------------------------------')
#     print(f"O custo total para o consumidor {numero_consumidor} é: R$ {custo_total:.2f}")
#     print('----------------------------------------------------------------------------')
# media_consumo_tipo1 = total_consumo_tipo1 / total_consumidores_tipo1 if total_consumidores_tipo1 != 0 else 0
# media_consumo_tipo2 = total_consumo_tipo2 / total_consumidores_tipo2 if total_consumidores_tipo2 != 0 else 0


# print("Resumo:")

# print(f"Total de consumo residencial: {total_consumo_residencial} kWh")
# print(f"Total de consumo comercial: {total_consumo_comercial} kWh")
# print(f"Total de consumo industrial: {total_consumo_industrial} kWh")
# print(f"Média de consumo do tipo 1: {media_consumo_tipo1:.2f} kWh")
# print(f"Média de consumo do tipo 2: {media_consumo_tipo2:.2f} kWh")
# print('\n')
# print(f'#####################################################################################################################')






#Exemplo meu sala de aula somar quantidade de consumidor:






# somaconsumidor1 = 0
# somaconsumidor2 = 0
# somaconsumidor3 = 0

# print('\n')
# for x in range(4):
#     print(f'########################################################################################')
#     print(f'Consumidor:{x+1}')
#     print('\n')
   
#     numeroconsumidor = int(input("Digite o número do consumidor: "))
#     quantidadekwh = float(input("Digite a quantidade de KWH /mês: "))
#     codigotipoconsumidor = int(input('Informe o código do consumidor sendo: [1 = Residencial] [2 = Comercial] [3 = Industrial]: '))




#     if codigotipoconsumidor == 1:
#         somaconsumidor1 += 1
#     elif codigotipoconsumidor == 2:
#         somaconsumidor2 += 1
#     elif codigotipoconsumidor == 3:        
#         somaconsumidor3 += 1
#     else:
#         print("Tipo de consumidor inválido!")

# print(f'A quantidade de consumidor tipo 1 é:{somaconsumidor1}')
# print(f'A quantidade de consumidor tipo 1 é:{somaconsumidor2}')
# print(f'A quantidade de consumidor tipo 1 é:{somaconsumidor3}')





#print('-------------------------------------------------------------------------------------') 
#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n


# def calcular_fatorial(numero):
#     if numero == 0:
#         return 1
#     else:
#         return numero * calcular_fatorial(numero - 1)

# while True:
#     numero = int(input("Digite um número inteiro (digite um número menor que 1 para sair): "))
    
#     if numero < 1:
#         print(" FIM DO CALCULO")
#         break
    
#     fatorial = calcular_fatorial(numero)
#     print(f"O fatorial de {numero} é: {fatorial}")


#print('-------------------------------------------------------------------------------------')

#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos


# menos_de_21 = 0
# mais_de_50 = 0
# print('\n')
# for x in range(6):
#     print(f'#####################################################################################################################')
#     print(f'PESSOAS:{x+1}')
#     print('\n')
#     idade = int(input("Digite a idade da pessoa: "))

#     if idade < 21:
#         menos_de_21 += 1
#     elif idade > 50:
#         mais_de_50 += 1

# print(f'#####################################################################################################################')
# print(f'------------------------------------------------------')
# print(f"Total de pessoas com menos de 21 anos: {menos_de_21}")
# print(f"Total de pessoas com mais de 50 anos: {mais_de_50}")
# print(f'------------------------------------------------------')


#print('-------------------------------------------------------------------------------------') 
#16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão





#print('-------------------------------------------------------------------------------------')

#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#72 Aula 3. Estruturas de Iteração
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.


# def calcular_total_pedido(preco_unitario, quantidade):
#     return preco_unitario * quantidade

# total_compra = 0

# while True:

#     numero_pedido = input("Digite o número do pedido (ou '0' para finalizar a compra): ")
    
    
#     if numero_pedido.lower() == '0':
#         print("COMPRA FINALIZADA COM SUCESSO.")
#         break
    
#     dia_pedido = int(input("Digite o dia do pedido: "))
#     mes_pedido = int(input("Digite o mês do pedido: "))
#     ano_pedido = int(input("Digite o ano do pedido: "))
#     preco_unitario = float(input("Digite o preço unitário do item: "))
#     quantidade = int(input("Digite a quantidade do item: "))
    
    
#     total_pedido = calcular_total_pedido(preco_unitario, quantidade)
    
#     total_compra += total_pedido
    
#     print(f"--------------------------------------------------------------------")
#     print(f"Pedido {numero_pedido} - Data: {dia_pedido}/{mes_pedido}/{ano_pedido}")
#     print(f"Preço unitário: R$ {preco_unitario:.2f}")
#     print(f"Quantidade: {quantidade}")
#     print(f"Total do pedido: R$ {total_pedido:.2f}")
#     print(f"--------------------------------------------------------------------")
#     print()

# print(f"Valor total da compra: R$ {total_compra:.2f}")


#print('-------------------------------------------------------------------------------------')


#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça umprograma que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.













#print('-------------------------------------------------------------------------------------')
#19. Em uma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado com nota >= 7.0



















#print('-------------------------------------------------------------------------------------')
#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:

#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Flamengo;
#5-Outros

#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros

#• Qual o seu salário?

#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.


# time = str(input('Digite o nome do time: 1 para '))
# endereco = str(input('Digite o nome do time: '))
# salario = float(input('Digite o nome do time: '))



#print('-------------------------------------------------------------------------------------')
#21. Emuma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.

#print('-------------------------------------------------------------------------------------')
#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número demultas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir tambémo número da carteira domotorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.

#print('-------------------------------------------------------------------------------------')
#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexomasculinomais pesado;
#• amédia de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

#print('-------------------------------------------------------------------------------------')
#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores nãonegativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar umvalor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração

#print('-------------------------------------------------------------------------------------')
#25. Faça umprograma que calcule o imposto de renda de umgrupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito umabatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

#print('-------------------------------------------------------------------------------------')
#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em umdeterminado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

#print('-------------------------------------------------------------------------------------')
#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.

#print('-------------------------------------------------------------------------------------')
#28. Construa umprograma que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#3.12. Exercícios da Aula 75
#• a quantidade de pessoas com idade superior a 50 anos;
#• amédia das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

#print('-------------------------------------------------------------------------------------')
#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em umdeterminado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

#print('-------------------------------------------------------------------------------------')
#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, Vviúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• amédia das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.