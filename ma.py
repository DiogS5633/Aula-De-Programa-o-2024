# Vamos criar um programa para calcular as informações de cada time de Volleyball
times = 30
jogadores_por_time = 12

# Dados fictícios para exemplo
times_dados = [
    {"jogadores": [{"peso": 80, "idade": 25}, {"peso": 85, "idade": 30}]},  # Exemplo Time 1
    # Adicione mais times aqui
]

# Função para calcular as médias e outras informações
def calcular_informacoes(times_dados):
    for i, time in enumerate(times_dados):
        pesos = [jogador["peso"] for jogador in time["jogadores"]]
        idades = [jogador["idade"] for jogador in time["jogadores"]]
        
        peso_medio = sum(pesos) / len(pesos)
        idade_medio = sum(idades) / len(idades)
        jogador_mais_pesado = max(pesos)
        jogador_mais_jovem = min(idades)
        
        print(f"Time {i+1}:")
        print(f"Peso Médio: {peso_medio:.2f}")
        print(f"Idade Média: {idade_medio:.2f}")
        print(f"Jogador Mais Pesado: {jogador_mais_pesado}kg")
        print(f"Jogador Mais Jovem: {jogador_mais_jovem} anos\n")
        
calcular_informacoes(times_dados)



# Ler números e informar quantos estão entre 100 e 200
count = 0

while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    if 100 <= num <= 200:
        count += 1

print(f"Números entre 100 e 200 digitados: {count}")


# Calcular tempo necessário para que a população do país A ultrapasse a de B
populacao_A = 5000000
taxa_A = 0.03
populacao_B = 7000000
taxa_B = 0.02
anos = 0

while populacao_A <= populacao_B:
    populacao_A += populacao_A * taxa_A
    populacao_B += populacao_B * taxa_B
    anos += 1

print(f"Anos necessários para que a população do país A ultrapasse a do país B: {anos}")


# Calcular custo total e outros dados de consumo de energia
consumidores = []

while True:
    numero = int(input("Número do consumidor (0 para sair): "))
    if numero == 0:
        break
    kwh = float(input("Quantidade de kWh consumidos: "))
    tipo = int(input("Tipo do consumidor (1-Residencial, 2-Comercial, 3-Industrial): "))
    
    if tipo == 1:
        preco = 0.3
    elif tipo == 2:
        preco = 0.5
    elif tipo == 3:
        preco = 0.7
    
    custo_total = kwh * preco
    consumidores.append((numero, custo_total, tipo, kwh))

total_consumo_residencial = sum([c[3] for c in consumidores if c[2] == 1])
total_consumo_comercial = sum([c[3] for c in consumidores if c[2] == 2])
total_consumo_industrial = sum([c[3] for c in consumidores if c[2] == 3])

print(f"Total consumo residencial: {total_consumo_residencial} kWh")
print(f"Total consumo comercial: {total_consumo_comercial} kWh")
print(f"Total consumo industrial: {total_consumo_industrial} kWh")


# Calcular o fatorial de vários números
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

while True:
    num = int(input("Digite um número inteiro (menor que 1 para sair): "))
    if num < 1:
        break
    print(f"Fatorial de {num} é {fatorial(num)}")


# Ler idades de várias pessoas e imprimir estatísticas
menos_21 = 0
mais_50 = 0

while True:
    idade = int(input("Digite a idade (valor negativo para sair): "))
    if idade < 0:
        break
    if idade < 21:
        menos_21 += 1
    if idade > 50:
        mais_50 += 1

print(f"Total de pessoas com menos de 21 anos: {menos_21}")
print(f"Total de pessoas com mais de 50 anos: {mais_50}")


# Calcular o resto da divisão por meio de subtrações sucessivas
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0
resto = dividendo

while resto >= divisor:
    resto -= divisor
    quociente += 1

print(f"Quociente: {quociente}")
print(f"Resto: {resto}")


# Ler um conjunto de pedidos de compra e calcular o valor total
pedidos = []

while True:
    numero_pedido = int(input("Número do pedido (0 para sair): "))
    if numero_pedido == 0:
        break
    dia = int(input("Dia do pedido: "))
    mes = int(input("Mês do pedido: "))
    ano = int(input("Ano do pedido: "))
    preco_unitario = float(input("Preço unitário: "))
    quantidade = int(input("Quantidade: "))
    
    valor_total = preco_unitario * quantidade
    pedidos.append(valor_total)

print(f"Valor total da compra: R$ {sum(pedidos):.2f}")


# Calcular conta de clientes em uma pousada
total_faturado = 0

while True:
    numero_conta = int(input("Número da conta (0 para sair): "))
    if numero_conta == 0:
        break
    nome = input("Nome do cliente: ")
    dias = int(input("Número de dias: "))
    
    diaria = 30.0
    if dias < 10:
        taxa = 15.0
    else:
        taxa = 8.0
    
    conta = (diaria * dias) + (taxa * dias)
    total_faturado += conta
    
    print(f"Nome: {nome}, Conta: R$ {conta:.2f}, Número da conta: {numero_conta}")

print(f"Total faturado pela pousada: R$ {total_faturado:.2f}")


# Analisar resultados de prova de algoritmos
turmas = []

while True:
    num_alunos = int(input("Digite o número de alunos na turma (0 para sair): "))
    if num_alunos == 0:
        break
    notas = []
    for i in range(num_alunos):
        nota = float(input(f"Nota do aluno {i+1}: "))
        notas.append(nota)
    
    aprovados = len([nota for nota in notas if nota >= 7.0])
    media = sum(notas) / num_alunos
    reprovados_percentual = len([nota for nota in notas if nota < 7.0]) / num_alunos * 100
    
    turmas.append({"aprovados": aprovados, "media": media, "reprovados_percentual": reprovados_percentual})

for i, turma in enumerate(turmas):
    print(f"Turma {i+1}:")
    print(f"Quantidade de alunos aprovados: {turma['aprovados']}")
    print(f"Média da turma: {turma['media']:.2f}")
    print(f"Percentual de reprovados: {turma['reprovados_percentual']:.2f}%")


# Pesquisa de opinião no Rio de Janeiro
times = {1: "Fluminense", 2: "Botafogo", 3: "Vasco", 4: "Flamengo", 5: "Outros"}
locais = {1: "RJ", 2: "Niterói", 3: "Outros"}
torcedores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
salario_botafogo = []
torcedores_rj_outros = 0
torcedores_niteroi_flu = 0

while True:
    time = int(input("Qual o seu time de coração (1-5, 0 para sair)? "))
    if time == 0:
        break
    local = int(input("Onde você mora (1-RJ, 2-Niterói, 3-Outros)? "))
    salario = float(input("Qual o seu salário? "))
    
    torcedores[time] += 1
    if time == 2:
        salario_botafogo.append(salario)
    if local == 1 and time == 5:
        torcedores_rj_outros += 1
    if local == 2 and time == 1:
        torcedores_niteroi_flu += 1

media_salario_botafogo = sum(salario_botafogo) / len(salario_botafogo) if salario_botafogo else 0

print(f"Torcedores por clube: {torcedores}")
print(f"Média salarial dos torcedores do Botafogo: R$ {media_salario_botafogo:.2f}")
print(f"Número de pessoas do RJ, torcedores de outros clubes: {torcedores_rj_outros}")
print(f"Número de pessoas de Niterói torcedores do Fluminense: {torcedores_niteroi_flu}")


# Analisar dados financeiros dos alunos
alunos = []
while True:
    renda_pessoal = float(input("Renda pessoal (0 para sair): "))
    if renda_pessoal == 0:
        break
    renda_familiar = float(input("Renda familiar: "))
    gasto_alimentacao = float(input("Total gasto com alimentação: "))
    gasto_despesas = float(input("Total gasto com outras despesas: "))
    
    alunos.append({
        "renda_pessoal": renda_pessoal,
        "renda_familiar": renda_familiar,
        "gasto_alimentacao": gasto_alimentacao,
        "gasto_despesas": gasto_despesas
    })

acima_200_despesas = len([a for a in alunos if a["gasto_despesas"] > 200])
renda_maior_pessoal = len([a for a in alunos if a["renda_pessoal"] > a["renda_familiar"]])
total_alunos = len(alunos)
percent_gasto_alimentacao = sum([a["gasto_alimentacao"] for a in alunos]) / sum([a["renda_pessoal"] for a in alunos]) * 100
percent_gasto_despesas = sum([a["gasto_despesas"] for a in alunos]) / sum([a["renda_familiar"] for a in alunos]) * 100

print(f"Porcentagem de alunos que gastam acima de R$200,00 com outras despesas: {acima_200_despesas / total_alunos * 100:.2f}%")
print(f"Número de alunos com renda pessoal maior que a familiar: {renda_maior_pessoal}")
print(f"Porcentagem gasta com alimentação: {percent_gasto_alimentacao:.2f}%")
print(f"Porcentagem gasta com outras despesas: {percent_gasto_despesas:.2f}%")


# Calcular total de recursos arrecadados com multas de trânsito
total_arrecadado = 0
maior_numero_multas = 0
carteira_maior_num_multas = 0

while True:
    carteira = int(input("Número da carteira (0 para sair): "))
    if carteira == 0:
        break
    numero_multas = int(input("Número de multas: "))
    valor_multas = [float(input(f"Valor da multa {i+1}: ")) for i in range(numero_multas)]
    
    valor_divida = sum(valor_multas)
    total_arrecadado += valor_divida
    if numero_multas > maior_numero_multas:
        maior_numero_multas = numero_multas
        carteira_maior_num_multas = carteira
    
    print(f"Carteira {carteira}, Dívida: R$ {valor_divida:.2f}")

print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
print(f"Carteira com maior número de multas: {carteira_maior_num_multas}")


# Analisar dados de atletas em uma olimpíada
atletas = []
while True:
    nome = input("Nome do atleta (@ para sair): ")
    if nome == "@":
        break
    sexo = input("Sexo (M/F): ")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    
    atletas.append({"nome": nome, "sexo": sexo, "idade": idade, "peso": peso, "altura": altura})

atleta_mais_alta = max([a for a in atletas if a["sexo"] == "F"], key=lambda x: x["altura"], default=None)
atleta_mais_pesado = max([a for a in atletas if a["sexo"] == "M"], key=lambda x: x["peso"], default=None)
media_idade = sum([a["idade"] for a in atletas]) / len(atletas)

print(f"Atleta feminina mais alta: {atleta_mais_alta['nome']} com {atleta_mais_alta['altura']}m" if atleta_mais_alta else "Nenhuma atleta feminina registrada.")
print(f"Atleta masculino mais pesado: {atleta_mais_pesado['nome']} com {atleta_mais_pesado['peso']}kg" if atleta_mais_pesado else "Nenhum atleta masculino registrado.")
print(f"Média de idade dos atletas: {media_idade:.2f} anos")


# Calcular a quantidade de gasolina usada em uma viagem
total_litros = 0

while True:
    velocidade = float(input("Digite a velocidade do carro (valor negativo para sair): "))
    if velocidade < 0:
        break
    tempo = float(input("Digite o tempo de viagem nessa velocidade (horas): "))
    distancia = velocidade * tempo
    litros_consumidos = distancia / 10
    total_litros += litros_consumidos
    print(f"Distância percorrida: {distancia} km, Litros consumidos: {litros_consumidos:.2f} L")

print(f"Total de litros gastos na viagem: {total_litros}")

# Calcular imposto de renda para um grupo de contribuintes
total_imposto = 0
contribuintes_isentos = 0

while True:
    cic = int(input("Digite o CIC (0 para sair): "))
    if cic == 0:
        break
    dependentes = int(input("Número de dependentes: "))
    renda_bruta = float(input("Renda bruta anual: "))
    
    abatimento = dependentes * 600
    renda_liquida = renda_bruta - abatimento
    
    if renda_liquida <= 1000:
        imposto = 0
        contribuintes_isentos += 1
    elif renda_liquida <= 5000:
        imposto = renda_liquida * 0.15
    else:
        imposto = renda_liquida * 0.25
    
    total_imposto += imposto
    print(f"CIC: {cic}, Imposto a pagar: R$ {imposto:.2f}")

print(f"Total de imposto arrecadado: R$ {total_imposto:.2f}")
print(f"Número de contribuintes isentos: {contribuintes_isentos}")


# Pesquisa de audiência de canais de TV
audiencia = {4: 0, 5: 0, 7: 0, 12: 0}
total_pessoas = 0

while True:
    canal = int(input("Digite o número do canal (4, 5, 7, 12, 0 para sair): "))
    if canal == 0:
        break
    pessoas = int(input("Número de pessoas assistindo: "))
    
    if canal in audiencia:
        audiencia[canal] += pessoas
    total_pessoas += pessoas

for canal, pessoas in audiencia.items():
    percentual = (pessoas / total_pessoas * 100) if total_pessoas else 0
    print(f"Canal {canal}: {percentual:.2f}% de audiência")


# Calcular o CR dos alunos de computação
melhor_cr = 0
alunos_com_5_ou_mais_disciplinas = []

while True:
    matricula = int(input("Número da matrícula (0 para sair): "))
    if matricula == 0:
        break
    disciplinas = int(input("Quantidade de disciplinas cursadas: "))
    notas = [float(input(f"Nota da disciplina {i+1}: ")) for i in range(disciplinas)]
    
    cr = sum(notas) / disciplinas
    if disciplinas >= 5:
        alunos_com_5_ou_mais_disciplinas.append(cr)
    
    if cr > melhor_cr:
        melhor_cr = cr

print(f"Melhor CR dos alunos: {melhor_cr:.2f}")
if alunos_com_5_ou_mais_disciplinas:
    print(f"Melhor CR dos alunos com 5 ou mais disciplinas: {max(alunos_com_5_ou_mais_disciplinas):.2f}")


# Calcular várias estatísticas sobre idade, altura e peso
quantidade_idade_maior_50 = 0
soma_alturas_10_20 = 0
contagem_10_20 = 0
peso_inferior_40 = 0
total_pessoas = 0

while True:
    idade = int(input("Digite a idade (valor negativo para sair): "))
    if idade < 0:
        break
    altura = float(input("Digite a altura (em metros): "))
    peso = float(input("Digite o peso (em kg): "))
    
    total_pessoas += 1
    
    if idade > 50:
        quantidade_idade_maior_50 += 1
    if 10 <= idade <= 20:
        soma_alturas_10_20 += altura
        contagem_10_20 += 1
    if peso < 40:
        peso_inferior_40 += 1

media_alturas_10_20 = (soma_alturas_10_20 / contagem_10_20) if contagem_10_20 else 0
percentual_peso_inferior_40 = (peso_inferior_40 / total_pessoas * 100) if total_pessoas else 0

print(f"Quantidade de pessoas com idade superior a 50 anos: {quantidade_idade_maior_50}")
print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {media_alturas_10_20:.2f} m")
print(f"Porcentagem de pessoas com peso inferior a 40 kg: {percentual_peso_inferior_40:.2f}%")


# Calcular vendas de mercadorias por categoria
total_vendas = 0
vendas_por_codigo = {"L": 0, "A": 0, "H": 0}

while True:
    valor = float(input("Digite o valor da mercadoria (0 para sair): "))
    if valor == 0:
        break
    codigo = input("Digite o código da mercadoria (L, A, H): ").upper()
    
    if codigo in vendas_por_codigo:
        vendas_por_codigo[codigo] += valor
    total_vendas += valor

print(f"Total vendido no dia: R$ {total_vendas:.2f}")
for codigo, total in vendas_por_codigo.items():
    print(f"Total vendido no código {codigo}: R$ {total:.2f}")


# Calcular estatísticas sobre idade e estado civil
casados = 0
solteiros = 0
soma_idades_viuvos = 0
contagem_viuvos = 0
desquitados_separados = 0
total_pessoas = 0

while True:
    idade = int(input("Digite a idade (valor negativo para sair): "))
    if idade < 0:
        break
    estado_civil = input("Digite o estado civil (C-casado, S-solteiro, V-viúvo, D-desquitado/separado): ").upper()
    
    total_pessoas += 1
    
    if estado_civil == "C":
        casados += 1
    elif estado_civil == "S":
        solteiros += 1
    elif estado_civil == "V":
        soma_idades_viuvos += idade
        contagem_viuvos += 1
    elif estado_civil == "D":
        desquitados_separados += 1

media_idades_viuvos = (soma_idades_viuvos / contagem_viuvos) if contagem_viuvos else 0
percentual_desquitados_separados = (desquitados_separados / total_pessoas * 100) if total_pessoas else 0

print(f"Quantidade de pessoas casadas: {casados}")
print(f"Quantidade de pessoas solteiras: {solteiros}")
print(f"Média das idades das pessoas viúvas: {media_idades_viuvos:.2f} anos")
print(f"Porcentagem de pessoas desquitadas/separadas: {percentual_desquitados_separados:.2f}%")

##################################################################################################################
# Simular uma máquina de venda de refrigerantes
refrigerantes = {"Coca-Cola": 4.00, "Pepsi": 3.50, "Guaraná": 3.00, "Fanta": 2.50, "Sprite": 3.00}

def exibir_refrigerantes():
    print("Refrigerantes disponíveis:")
    for i, (nome, preco) in enumerate(refrigerantes.items(), start=1):
        print(f"{i}. {nome} - R$ {preco:.2f}")

def selecionar_refrigerante(opcao):
    refrigerante = list(refrigerantes.keys())[opcao-1]
    preco = refrigerantes[refrigerante]
    return refrigerante, preco

total_vendido = 0

while True:
    exibir_refrigerantes()
    opcao = int(input("Selecione um refrigerante (0 para sair): "))
    if opcao == 0:
        break
    if 1 <= opcao <= len(refrigerantes):
        refrigerante, preco = selecionar_refrigerante(opcao)
        print(f"Você comprou {refrigerante} por R$ {preco:.2f}")
        total_vendido += preco
    else:
        print("Opção inválida.")

print(f"Total vendido: R$ {total_vendido:.2f}")


# Calcular a média aritmética dos elementos de uma matriz 3x3
matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
        soma += elemento
    matriz.append(linha)

media = soma / 9

print(f"Matriz: {matriz}")
print(f"Média aritmética dos elementos: {media:.2f}")


# Calcular o total de vendas e a comissão de vendedores
vendas = {}

while True:
    vendedor = input("Digite o nome do vendedor (ou 'fim' para encerrar): ")
    if vendedor.lower() == 'fim':
        break
    valor_venda = float(input(f"Digite o valor da venda de {vendedor}: "))
    if vendedor in vendas:
        vendas[vendedor] += valor_venda
    else:
        vendas[vendedor] = valor_venda

for vendedor, total_vendas in vendas.items():
    comissao = total_vendas * 0.05
    print(f"Vendedor: {vendedor}, Total de Vendas: R$ {total_vendas:.2f}, Comissão: R$ {comissao:.2f}")


# Calcular o imposto de um produto
produtos = {"Produto A": 100, "Produto B": 150, "Produto C": 200}

def calcular_imposto(preco):
    if preco <= 100:
        return preco * 0.05
    elif preco <= 200:
        return preco * 0.10
    else:
        return preco * 0.15

for produto, preco in produtos.items():
    imposto = calcular_imposto(preco)
    print(f"Produto: {produto}, Preço: R$ {preco:.2f}, Imposto: R$ {imposto:.2f}")
