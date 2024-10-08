def q1():
    numero1 = int(input("NUMERO INTEIRO UM: "))
    numero2 = int(input("NUMERO INTEIRO DOIS: "))
    soma = numero1 + numero2
    if soma > 10:
        print(f'Resultado: {soma}')

def q2():
    numero1 = int(input("NUMERO INTEIRO UM: "))
    numero2 = int(input("NUMERO INTEIRO DOIS: "))
    soma = numero1 + numero2
    if soma > 20:
        soma += 8
    else:
        soma -= 5
    print(f'Resultado: {soma}')

def q3():
    num = int(input("Numero teste inteiro: "))
    if num % 3 == 0:
        print("É múltiplo de 3")
    else:
        print("Não é múltiplo de 3")

def q4():
    num = int(input("Digite um número: "))
    if num % 5 == 0:
        print("É divisível por 5")
    else:
        print("Não é divisível por 5")

def q5():
    num = int(input("Digite um número: "))
    if num % 3 == 0 and num % 7 == 0:
        print("É divisível por 3 e por 7")
    else:
        print("Não é divisível por 3 e por 7")

def q6():
    salario_bruto = float(input("Digite o salário bruto: "))
    prestacao = float(input("Digite o valor da prestação: "))
    if prestacao <= 0.3 * salario_bruto:
        print("Empréstimo pode ser concedido")
    else:
        print("Empréstimo não pode ser concedido")

def q7():
    num = int(input("Digite um número: "))
    if 20 <= num <= 50:
        print("O número está entre 20 e 50")
    else:
        print("O número não está entre 20 e 50")

def q8():
    num = int(input("Digite um número: "))
    if num > 20:
        print("Maior do que 20")
    elif num == 20:
        print("Igual a 20")
    else:
        print("Menor do que 20")

def q9():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))
    if ano_nascimento > ano_atual:
        print("Ano de nascimento inválido")
    else:
        idade = ano_atual - ano_nascimento
        print(f"A idade da pessoa é: {idade} anos")

def q10():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    numeros = [num1, num2, num3]
    numeros.sort()
    print(f"Números em ordem crescente: {numeros}")

def q11():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    maior = max(num1, num2, num3)
    print(f"O maior número é: {maior}")

def q12():
    idade = int(input("Digite a idade: "))
    if idade >= 65:
        print("Maior de 65 anos")
    elif idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")

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
    print(f"Desconto do INSS: R${desconto:.2f}")

def q15():
    valor_compra = float(input("Digite o valor de compra do produto: "))
    if valor_compra < 20:
        valor_venda = valor_compra * 1.45
    else:
        valor_venda = valor_compra * 1.30
    print(f"Valor de venda: R${valor_venda:.2f}")

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
    print(f"Nome: {nome}, Valor a pagar: R${valor:.2f}")

def q18():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    numero = int(input("Digite um número entre 1 e 12: "))
    if 1 <= numero <= 12:
        print(f"Mês: {meses[numero - 1]}")
    else:
        print("Não existe mês com este número")

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
        print(f"Média aritmética: {media:.2f}")
    else:
        print("Equipe desclassificada")

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
    print(f"Saldo médio: R${saldo_medio:.2f}, Crédito: R${credito:.2f}")

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
        print(f"Consumo estimado de combustível: {consumo:.2f} litros")

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
q21()
q22()
q23()
q24()
q25()