# 1. Faça um programa que imprima o seu nome.
def q1():
    print('diogo')

################################################################################
# 2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    print(30 * 27)

################################################################################
# 3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    print(f'Média : {round((5+8+12)/3,1)}')

################################################################################
# 4. Faça um programa que leia e imprima um número inteiro.
def q4():
    numero = int(input('Forneça o Número: '))
    print(f'Teste: {numero}')

################################################################################
# 5. Faça um programa que leia dois números reais e os imprima.
def q5():
    numero1 = float(input('Forneça o primeiro número: '))
    numero2 = float(input('Forneça o segundo número: '))
    print(f'Teste: {numero1} e {numero2}')

################################################################################
# 6. Faça um programa que leia um número inteiro e imprima o seu antecessor e o seu sucessor.
def q6():
    numero = int(input('Forneça um número inteiro: '))
    print(f'Antecessor: {numero} : {numero - 1}, Sucessor:{numero}: {numero + 1}')

################################################################################
# 7. Faça um programa que leia o nome, o endereço e o telefone de um cliente e ao final, imprima esses dados.
def q7():
    nome = input('Forneça o nome: ')
    endereco = input('Forneça o endereço: ')
    telefone = input('Forneça o telefone: ')
    print(f'Nome: {nome}, Endereço: {endereco}, Telefone: {telefone}')

################################################################################
# 8. Faça um programa que leia dois números inteiros e imprima a subtração deles.
def q8():
    numero1 = int(input('Forneça o primeiro número inteiro: '))
    numero2 = int(input('Forneça o segundo número inteiro: '))
    print(f'Subtração: {numero1 - numero2}')

################################################################################
# 9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    numero = float(input('Forneça um número real: '))
    print(f'1/4 do número: {round(numero / 4,2)}')

################################################################################
# 10. Faça um programa que leia três números reais e calcule a média aritmética destes números. Ao final, o programa deve imprimir o resultado do cálculo.
def q10():
    numero1 = float(input('Forneça o primeiro número real: '))
    numero2 = float(input('Forneça o segundo número real: '))
    numero3 = float(input('Forneça o terceiro número real: '))
    media = (numero1 + numero2 + numero3) / 3
    print(f'Média aritmética: {round(media,2)}')

################################################################################
# 11. Faça um programa que leia dois números reais e calcule as quatro operações básicas entre estes dois números, adição, subtração, multiplicação e divisão. Ao final, o programa deve imprimir os resultados dos cálculos.
def q11():
    numero1 = float(input('Forneça o primeiro número real: '))
    numero2 = float(input('Forneça o segundo número real: '))
    print(f'Adição: {numero1 + numero2}')
    print(f'Subtração: {numero1 - numero2}')
    print(f'Multiplicação: {numero1 * numero2}')
    print(f'Divisão: {numero1 / numero2}')

################################################################################
# 12. Faça um programa que leia um número real e calcule o quadrado deste número. Ao final, o programa deve imprimir o resultado do cálculo.
def q12():
    numero = float(input('Forneça um número real: '))
    print(f'Quadrado do número: {numero ** 2}')

################################################################################
# 13. Faça um programa que leia o saldo de uma conta poupança e imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input('Forneça o saldo da poupança: '))
    novo_saldo = saldo * 1.02
    print(f'Novo saldo: {novo_saldo}')

################################################################################
# 14. Faça um programa que leia a base e a altura de um retângulo e imprima o perímetro (2 * (base + altura)) e a área (base * altura).
def q14():
    base = float(input('Forneça a base do retângulo: '))
    altura = float(input('Forneça a altura do retângulo: '))
    perimetro = 2 * (base *2 + altura*2)
    area = base * altura
    print(f'Perímetro: {perimetro}, Área: {area}')

################################################################################
# 15. Faça um programa que leia o valor de um produto, o percentual do desconto desejado e imprima o valor do desconto e o valor do produto subtraindo o desconto.
def q15():
    valor_produto = float(input('Forneça o valor do produto: '))
    percentual_desconto = float(input('Forneça o percentual de desconto: '))
    valor_desconto = valor_produto * (percentual_desconto / 100)
    valor_final = valor_produto - valor_desconto
    print(f'Valor do desconto: {valor_desconto}, Valor final: {valor_final}')

################################################################################
# 16. Faça um programa que calcule o reajuste do salário de um funcionário. Para isso, o programa deverá ler o salário atual do funcionário e ler o percentual de reajuste. Ao final imprimir o valor do novo salário.
def q16():
    salario_atual = float(input('Forneça o salário atual: '))
    percentual_reajuste = float(input('Forneça o percentual de reajuste: '))
    novo_salario = salario_atual * (1 + percentual_reajuste / 100)
    print(f'Novo salário: {novo_salario}')

################################################################################
# 17. Faça um programa que calcule a conversão entre graus centígrados e Fahrenheit. Para isso, leia o valor em centígrados e calcule com base na fórmula a seguir. Após calcular o programa deve imprimir o resultado da conversão.
# F = (9 x C + 160) / 5
def q17():
    celsius = float(input('Forneça a temperatura em graus centígrados: '))
    fahrenheit = (9 * celsius + 160) / 5
    print(f'Temperatura em Fahrenheit: {fahrenheit}')

################################################################################
# 18. Faça um programa que calcule a quantidade de litros de combustível consumidos em uma viagem, sabendo-se que o carro tem autonomia de 12 km por litro de combustível. O programa deverá ler o tempo decorrido na viagem e a velocidade média e aplicar as fórmulas:
# D = T x V       L = D / 12
# Em que:
# • D = Distância percorrida em horas
# • T = Tempo
# • V = Velocidade média
# • L = Litros de combustível consumidos
# Ao final, o programa deverá imprimir a distância percorrida e a quantidade de litros consumidos na viagem.
def q18():
    tempo = float(input('Forneça o tempo decorrido na viagem (em horas): '))
    velocidade_media = float(input('Forneça a velocidade média (em km/h): '))
    distancia = tempo * velocidade_media
    litros_consumidos = distancia / 12
    print(f'Distância percorrida: {distancia} km, Litros consumidos: {litros_consumidos} L')

################################################################################
# 19. Faça um programa que calcule o valor de uma prestação em atraso. Para isso, o programa deve ler o valor da prestação vencida, a taxa periódica de juros e o período de atraso. Ao final, o programa deve imprimir o valor da prestação atrasada, o período de atraso, os juros que serão cobrados pelo período de atraso, o valor da prestação acrescido dos juros. Considere juros simples.
def q19():
    valor_prestacao = float(input('Forneça o valor da prestação vencida: '))
    taxa_juros = float(input('Forneça a taxa periódica de juros (em %): '))
    periodo_atraso = int(input('Forneça o período de atraso (em dias): '))
    juros = valor_prestacao * (taxa_juros / 100) * periodo_atraso
    valor_final = valor_prestacao + juros
    print(f'Valor da prestação atrasada: {valor_prestacao}, Período de atraso: {periodo_atraso} dias, Juros: {juros}, Valor final: {valor_final}')

################################################################################
# 20. Faça um programa que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). Para isso, será necessário também ler o valor da cotação do dólar.
def q20():
    valor_dolar = float(input('Forneça o valor em dólar (US$): '))
    cotacao_dolar = float(input('Forneça a cotação do dólar: '))
    valor_real = valor_dolar * cotacao_dolar
    print(f'Valor em reais (R$): {valor_real}')
################################################################################


q1()
q2()
q3()
q4()
q5()
q6()
q7()
q8()
q9()
q10()
q11()
q12()
q13()
q14()
q15()
q16()
q17()
q18()
q19()
q20()
