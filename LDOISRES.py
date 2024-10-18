#####################################################
from datetime import date, datetime           # pip3 install datetime
from deep_translator import GoogleTranslator  # pip3 install deep-translator
#####################################################
HOJE = datetime.now()
tradutor = GoogleTranslator(source = 'en', target = 'pt')
#####################################################
#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.

def q1():
    numero1 = int(input("NUMERO INTEIRO UM:  "))
    numero2 = int(input("NUMERO INTEIRO DOIS: "))
    nota = (numero1 + numero2)
    print(f'Teste: {numero1} e {numero2}\n')


    if nota >= 10:
        print('Aprovado')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.

def q2():
    numero1 = int(input("NUMERO INTEIRO UM:  "))
    numero2 = int(input("NUMERO INTEIRO DOIS:  "))
    nota = (numero1 + numero2)
    print(f'Teste: {numero1} e {numero2}\n')


    if nota > 20:
        print(f'Maior que 20: {nota + 8 }\n')
    elif nota <= 20:
        print(f'Menor que 20: {nota - 5 }\n ')

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".

def q3():
    num = int(input("Numero teste inteiro:  "))
    if num % 3== 0:
        print ("O valor Inserido é múltiplo de 3")
    else : 
        print("O valor Inserido Não é múltiplo de 3")     

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.

def q4():
    numero = int(input("NUMERO UM:  "))
    if numero % 5 == 0:
        print("É divisivel por 5")
    else :
        print("Não é divisivel por 5")
 
#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.

def q5():
    num = int(input("Digite um número: "))
    if num % 3 == 0 and num % 7 == 0:
        print("É divisível por 3 e por 7")
    else:
        print("Não é divisível por 3 e por 7")

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

def q6():
    salario_bruto = float(input("Digite o salário bruto: "))
    prestacao = float(input("Digite o valor da prestação: "))
    if prestacao <= 0.3 * salario_bruto:
        print("Empréstimo pode ser concedido")
    else:
        print("Empréstimo não pode ser concedido")

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.

def q7():
    num = int(input("Digite um número: "))
    if 20 <= num <= 50:
        print("O número está entre 20 e 50")
    else:
        print("O número não está entre 20 e 50")

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".

def q8():
    num = int(input("Digite um número: "))
    if num > 20:
        print("Maior do que 20")
    elif num == 20:
        print("Igual a 20")
    else:
        print("Menor do que 20")

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.

def q9():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    if ano_nascimento > ano_atual:
        print("Ano de nascimento inválido")
    else:
        idade = ano_atual - ano_nascimento
        print(f"A idade da pessoa é: {idade} anos")

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.

def q10():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    numeros = [num1, num2, num3]
    numeros.sort()
    print(f"Números em ordem crescente: {numeros}")

#11. Faça um programa que leia 3 números e imprima o maior deles.

def q11():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    maior = max(num1, num2, num3)
    print(f"O maior número é: {maior}")

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos

def q12():
    idade = int(input("Digite a idade: "))
    if idade >= 65:
        print("Maior de 65 anos")
    elif idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).


def q13():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota da prova 1: "))
    nota2 = float(input("Digite a nota da prova 2: "))
    media = (nota1 + nota2) / 2
    print(f"Nome: {nome}")
    print(f"Nota da prova 1: {nota1}")
    print(f"Nota da prova 2: {nota2}")
    print(f"Média: {media}")
    if media >= 7:
        print("Aprovado")
    elif media < 3:
        print("Reprovado")
    else:
        print("Em Prova Final")

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

def q14():
    salario = float(input("Digite o salário: "))
    if salario <= 600:
        desconto = 0
    elif salario <= 1200:
        desconto = 0.2 * salario
    elif salario <= 2000:
        desconto = 0.25 * salario
    else:
        desconto = 0.3 * salario
    print(f"Desconto do INSS: R${desconto}")

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

def q15():
    valor_compra = float(input("Digite o valor de compra do produto: "))
    if valor_compra < 20:
        valor_venda = valor_compra * 1.45
    else:
        valor_venda = valor_compra * 1.30
    print(f"Valor de venda: R${valor_venda}")

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

def q16():
    idade = int(input("Digite a idade do nadador: "))
    if 5 <= idade <= 7:
        categoria = "Infantil A"
    elif 8 <= idade <= 10:
        categoria = "Infantil B"
    elif 11 <= idade <= 13:
        categoria = "Juvenil A"
    elif 14 <= idade <= 17:
        categoria = "Juvenil B"
    elif idade >= 18:
        categoria = "Sênior"
    else:
        categoria = "Idade fora das categorias"
    print(f"Categoria: {categoria}")

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

def q17():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    if idade <= 10:
        valor = 30
    elif idade <= 29:
        valor = 60
    elif idade <= 45:
        valor = 120
    elif idade <= 59:
        valor = 150
    elif idade <= 65:
        valor = 250
    else:
        valor = 400
    print(f"Nome: {nome}, Valor a pagar: R${valor}")

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

#def q18():
#    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
#    numero = int(input("Digite um número entre 1 e 12: "))
#    if 1 <= numero <= 12:
#        print(f"Mês: {meses[numero - 1]}")
#    else:
#        print("Não existe mês com este número")

def q18():
    mes = int(input('Digite um numero do mes:  '))
    if mes < 1 or mes > 12:
        print('Mes invalido')
    else:
        data = datetime.strptime(f'01/{mes}/24','%d/%m/%y')
        mes_extenso = data.strftime('%B')
        print(tradutor.translate(mes_extenso))

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

def q19():
    pontos = []
    for i in range(3):
        ponto = int(input(f"Digite os pontos do jogador {i+1}: "))
        pontos.append(ponto)
    pontos.sort(reverse=True)
    soma = sum(pontos)
    print(f"Pontos em ordem decrescente: {pontos}")
    if soma > 100:
        media = soma / 3
        print(f"Média aritmética: {media}")
    else:
        print("Equipe desclassificada")


#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

def q20():
    saldo_medio = float(input("Digite o saldo médio: "))
    if saldo_medio <= 500:
        credito = 0
    elif saldo_medio <= 1000:
        credito = 0.3 * saldo_medio
    elif saldo_medio <= 3000:
        credito = 0.4 * saldo_medio
    else:
        credito = 0.5 * saldo_medio
    print(f"Saldo médio: R${saldo_medio}, Crédito: R${credito}")

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:


def q21():
    nome_livro = input("Nome do livro: ")
    tipo_usuario = input("Tipo de usuário (professor/aluno): ").lower()
    if tipo_usuario == "professor":
        dias = 10
    elif tipo_usuario == "aluno":
        dias = 3
    else:
        dias = 0
        print("Tipo de usuário inválido")
    if dias > 0:
        print(f"Nome do livro: {nome_livro}")
        print(f"Tipo de usuário: {tipo_usuario.capitalize()}")
        print(f"Total de dias: {dias}")

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

def q22():
    percurso = float(input("Digite o percurso em quilômetros: "))
    tipo_carro = input("Digite o tipo do carro (A, B, C): ").upper()
    if tipo_carro == "A":
        consumo = percurso / 12
    elif tipo_carro == "B":
        consumo = percurso / 9
    elif tipo_carro == "C":
        consumo = percurso / 8
    else:
        consumo = 0
        print("Tipo de carro inválido")
    if consumo > 0:
        print(f"Consumo estimado de combustível: {consumo} litros")

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

def q23():
    pratos = {"Vegetariano": 180, "Peixe": 230, "Frango": 250, "Carne": 350}
    sobremesas = {"Abacaxi": 75, "Sorvete diet": 110, "Mousse diet": 170, "Mousse chocolate": 200}
    bebidas = {"Chá": 20, "Suco de laranja": 70, "Suco de melão": 100, "Refrigerante diet": 65}
    
    prato = input("Escolha um prato (Vegetariano, Peixe, Frango, Carne): ")
    sobremesa = input("Escolha uma sobremesa (Abacaxi, Sorvete diet, Mousse diet, Mousse chocolate): ")
    bebida = input("Escolha uma bebida (Chá, Suco de laranja, Suco de melão, Refrigerante diet): ")
    
    if prato in pratos and sobremesa in sobremesas and bebida in bebidas:
        total_calorias = pratos[prato] + sobremesas[sobremesa] + bebidas[bebida]
        print(f"Total de calorias: {total_calorias} cal")
    else:
        print("Escolha inválida")


#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

def q24():
    placa = input("Digite a placa do carro: ")
    ultimo_digito = placa[-1]
    meses = {
        "1": "Janeiro",
        "2": "Fevereiro",
        "3": "Março",
        "4": "Abril",
        "5": "Maio",
        "6": "Junho",
        "7": "Julho",
        "8": "Agosto",
        "9": "Setembro",
        "0": "Outubro"
    }
    if ultimo_digito in meses:
        print(f"O emplacamento deve ser renovado em: {meses[ultimo_digito]}")
    else:
        print("Placa inválida")

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

def q25():
    indice = float(input("Digite o índice de poluição: "))
    if indice >= 0.5:
        print("Indústrias do 1º, 2º e 3º grupos devem suspender atividades")
    elif indice >= 0.4:
        print("Indústrias do 1º e 2º grupos devem suspender atividades")
    elif indice >= 0.3:
        print("Indústrias do 1º grupo devem suspender atividades")
    else:
        print("Índice de poluição aceitável")

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}')
match questao:
    case 1:
        q1()
    case 2:
        q2()
    case 3:
        q3()
    case 4:
        q4()
    case 5:
        q5()
    case 6:
        q6()
    case 7:
        q7()
    case 8:
        q8()
    case 9:
        q9()
    case 10:
        q10()
    case 11:
        q11()
    case 12:
        q12()
    case 13:
        q13()
    case 14:
        q14()
    case 15:
        q15()       
    case 16:
        q16()
    case 17:
        q17()
    case 18:
        q18()
    case 19:
        q19()
    case 20:
        q20()
    case 21:
        q21()
    case 22:
        q22()
    case 23:
        q23()
    case 24:
        q24()
    case 25:
        q25()     
    case _:
        print('Questão Inválida')   
