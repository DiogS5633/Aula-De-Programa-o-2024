'''
Lista de Exercícios referentes a estruturas de iteração (repetição)
'''

from util import *
#def exemploPara():
#    for x in range (10):     # vai de 0 a 9
#        print(x)        
#    for x in range(1,10,2):  # vai de 1 a 9, avançando de 2 em 2
#        print(x)
#    for x in range(1,10,-1): # vai de 10 a 2
#        print(x)

#def exemploEnquanto():
#    opcao = -1
#    while opcao !=0
#        opcao = int(input('Escolha uma opcao (0 para sair): '))
#        print(opcao)

def exemplosInputPersonalizados():
    num = input_int('Inteiro: ')
    num2 = input_float('Real: ')
    senha = input_senha('Senha: ')

#1.Faça um programa que imprima todos os números de 1 até 100.

def q1():
        
    for x in range (1,100):    
        print(x)        

#2. Faça um programa que imprima todos os números pares de 100 até 1.

def q2():

   for x in range(100,1,-2):
        print(x)

#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.

def q3():

   for x in range(1,500,5):
        print(x)

#4. Faça umprograma que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.

def q4():

        for x in range(3):
                nome = input('Degite seu nome: ')
                idade = int(input('Digite a idade: '))
                sexo = input('Digite seu sexo: ')

                if sexo == "m" and idade > 21:
                        print(f'O nome da pessoa é : {nome}')
                else:
                        print(f'Menor de idade')

#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.

def q5():

        erro = True
        while erro == True:
                fator1 = 0
                try:
                        fator1= int(input('Numero 1:  '))
                        erro = False
                except ValueError:  # só é executado para o tipo de erro ValueError
                        print('O valor informado não um número inteiro')
                        erro = True 
                except: # captura qualquer erro
                        print('Ocoreu um erro desconhecido! Tente novamete!')
                        erro = True 
                else:
                        erro = False # executa se não ocorrer erro
                finally:
                        print(f'Numero 1 = {fator1}') # mensagem sempre é exibida,com erro ou não         

        erro = True
        while erro == True:
                try:
                        fator2 = int(input('Numero2: '))
                        erro = False
                except ValueError:
                        print('O valor informado não é um número inteiro!')  
                        erro = True
        produto = 0
        for _ in range (fator1):
                produto += fator2

        print(f'{fator1} * {fator2} = {produto}')

#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.
# 1 1 2 3 5 8 13 21

def q6():

        anterior = 0
        atual = 1
        print(atual,end="")
        for x in range(19):
                proximo = anterior + atual
                print(proximo,end="")
                anterior = atual
                atual = proximo

#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.

def q7():
    relatorio = '\nNOME\tN1\tN2\tMEDIA\n'
    media_geral = 0
    qtde_alunos = input_int('Qtde de Alunos: ')
    for _ in range(qtde_alunos):
        nome = input('Nome: ')
        n1 = input_float('Nota 1: ')
        n2 = input_float('Nota 2: ')
        media = (n1 + n2) / 2
        media_geral += media
        relatorio += f'{nome}\t{n1}\t{n2}\t{round(media,1)}\n'
    media_geral = media_geral / qtde_alunos
    print(relatorio)
    print(f'\nMédia Geral: {round(media_geral,1)}')

#8. Faça umprograma que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRRF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto

def q8():

        for x in range(3):
                nome = input('Digite o NOME: ')
                salariobruto = float(input('digite o salario bruto: '))

        if salariobruto < 1300 :
                print(f'O Fulano {nome} está isento de declaração.')

        if salariobruto >= 1300 and salariobruto < 2300:
                print(f'O Senhor {nome} ira pagar {salariobruto * 10 /100} do sálario.')

        if salariobruto >= 2300:
                print(f'O Senhor {nome} ira pagar {salariobruto * 15 /100} do sálario.')

#9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.

def q9():
    qtdePessoasExcelente = 0
    somaIdadeExcelente = 0
    qtdePessoasRegular = 0
    qtdePessoasBom = 0

    qtdeTotalPessoas = int(input('Número de Pessoas: '))

   
    if qtdeTotalPessoas <= 0:
        print("Número inválido de pessoas.")
        return  
  
    for x in range(qtdeTotalPessoas):
   
        while True:
            try:
                idade = int(input('Idade: '))
                if idade <= 0:
                    print("Idade inválida, por favor insira uma idade positiva.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido para a idade.")

        while True:
            try:
                opiniao = int(input('Opinião ([3]-Excelente - [2]-Bom - [1]-Regular): '))
                if opiniao not in [1, 2, 3]:
                    print('Opção inválida! Escolha entre 1, 2 ou 3.')
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido (1, 2 ou 3).")

        match opiniao:
            case 1:
                qtdePessoasRegular += 1
            case 2:
                qtdePessoasBom += 1
            case 3:
                qtdePessoasExcelente += 1
                somaIdadeExcelente += idade

   
    if qtdePessoasExcelente > 0:
        mediaIdadeExcelente = somaIdadeExcelente / qtdePessoasExcelente
        print(f'Média idade excelente: {mediaIdadeExcelente:.2f}')
    else:
        print('Nenhuma pessoa respondeu "Excelente".')

    print(f'Qtde de pessoas regular: {qtdePessoasRegular}')
    
    if qtdeTotalPessoas > 0:
        porcentagemBom = (qtdePessoasBom / qtdeTotalPessoas) * 100
        print(f'% de pessoas que responderam bom: {porcentagemBom:.2f}%')
    else:
        print('Número de pessoas inválido para calcular a porcentagem.')

    print('-------------------------------------------------------------------------------------')

#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos times;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.

#• O peso médio e a idade média de cada um dos times; ------ok
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.

def q10():

    somatotalidade = 0
    somatotalpeso = 0
    totaljugadores = 30 * 12  

    
    for pais in range(30):
        print(f"\n-----------------------------------")
        print(f"País {pais + 1}:")

        
        somatimeidade = 0
        somatimepeso = 0
        maiorpeso = 0
        menoridade = 1000

        
        for jogador in range(12):
            print(f"  Jogador {jogador + 1}:")

            
            idade = int(input("    Digite a idade do jogador: "))
            peso = float(input("    Digite o peso do jogador: "))

            
            somatimeidade += idade
            somatimepeso += peso

            
            if peso > maiorpeso:
                maiorpeso = peso
            if idade < menoridade:
                menoridade = idade

            
            somatotalidade += idade
            somatotalpeso += peso

      
        mediaidadepais = somatimeidade / 12
        mediapesopais = somatimepeso / 12

        
        print(f"\n  O peso médio do time {pais + 1} é: {mediapesopais:.2f} kg")
        print(f"  A idade média do time {pais + 1} é: {mediaidadepais:.2f} anos")
        print(f"  O atleta mais pesado do time {pais + 1} tem: {maiorpeso:.2f} kg")
        print(f"  O atleta mais jovem do time {pais + 1} tem: {menoridade} anos")

    
    mediapesoall = somatotalpeso / totaljugadores
    mediaidadeall = somatotalidade / totaljugadores

    
    print("\n-----------------------------------")
    print(f"O peso médio de todos os participantes é: {mediapesoall:.2f} kg")
    print(f"A idade média de todos os participantes é: {mediaidadeall:.2f} anos")
    print("\n-----------------------------------")

#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.

def q11():
    count = 0

    while True:
        num = int(input("Digite um número (0 para sair): "))
        if num == 0:
            break
        if 100 <= num <= 200:
            count += 1

    return count  # Retorna a contagem

# Chama a função e imprime o resultado
result = q11()
print(f"Números entre 100 e 200 digitados: {result}")

#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.


def q12():
    populacao_A = 5000000  
    taxa_A = 0.03  
    populacao_B = 7000000  
    taxa_B = 0.02  
    anos = 0  

    while populacao_A <= populacao_B:
        populacao_A += populacao_A * taxa_A  
        populacao_B += populacao_B * taxa_B  
        anos += 1  

    return anos  

result = q12()
print(f"Anos necessários para que a população do país A ultrapasse a do país B: {result}")

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
#• Amédia de consumo dos tipos 1 e 2

def q13():
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
        else:
            print("Tipo de consumidor inválido. Digite 1, 2 ou 3.")
            continue

       
        custo_total = kwh * preco
        consumidores.append((numero, custo_total, tipo, kwh)) 

    
    total_consumo_residencial = sum([c[3] for c in consumidores if c[2] == 1])
    total_consumo_comercial = sum([c[3] for c in consumidores if c[2] == 2])
    total_consumo_industrial = sum([c[3] for c in consumidores if c[2] == 3])

   
    print(f"Total consumo residencial: {total_consumo_residencial} kWh")
    print(f"Total consumo comercial: {total_consumo_comercial} kWh")
    print(f"Total consumo industrial: {total_consumo_industrial} kWh")

#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n

def q14():
    def fatorial(n):
        
        if n == 0:
            return 1
        else:
            return n * fatorial(n - 1)

   
    while True:
        num = int(input("Digite um número inteiro (menor que 1 para sair): "))
        if num < 1:
            break  
        print(f"Fatorial de {num} é {fatorial(num)}")

#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos

def q15():
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

def q16():
    
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))

    
    quociente = 0
    resto = dividendo

    
    while resto >= divisor:
        resto -= divisor
        quociente += 1

    
    print(f"Quociente: {quociente}")
    print(f"Resto: {resto}")

#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#72 Aula 3. Estruturas de Iteração
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.

def q17():
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

#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça um programa que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.

def q18():

    faturado = 0

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
    faturado += conta

    print(f"Nome: {nome}, Conta: R$ {conta}, Número da conta: {numero_conta}")

    print(f"Total faturado pela pousada: R$ {faturado}")

#19. Em uma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado com nota >= 7.0

def q19():
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
        print("-" * 40)

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

def q20():
   
    times = {1: "Fluminense", 2: "Botafogo", 3: "Vasco", 4: "Flamengo", 5: "Outros"}
    locais = {1: "RJ", 2: "Niterói", 3: "Outros"}
    
  
    torcedores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    salario_botafogo = []
    torcedores_rj_outros = 0
    torcedores_niteroi_flu = 0

  
    while True:
      
        time = int(input("Qual o seu time de coração (1-Fluminense, 2-Botafogo, 3-Vasco, 4-Flamengo, 5-Outros, 0 para sair)? "))
        
       
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

    
    print("\nResultados da pesquisa:")
    print(f"Torcedores por clube: {torcedores}")
    print(f"Média salarial dos torcedores do Botafogo: R$ {media_salario_botafogo:.2f}")
    print(f"Número de pessoas do RJ, torcedores de outros clubes: {torcedores_rj_outros}")
    print(f"Número de pessoas de Niterói torcedores do Fluminense: {torcedores_niteroi_flu}")

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

def q21():
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
    
    
    if total_alunos > 0:
        percent_gasto_alimentacao = sum([a["gasto_alimentacao"] for a in alunos]) / sum([a["renda_pessoal"] for a in alunos]) * 100
        percent_gasto_despesas = sum([a["gasto_despesas"] for a in alunos]) / sum([a["renda_familiar"] for a in alunos]) * 100
        percent_acima_200_despesas = (acima_200_despesas / total_alunos) * 100
    else:
        percent_gasto_alimentacao = 0
        percent_gasto_despesas = 0
        percent_acima_200_despesas = 0
    
    
    print(f"Porcentagem de alunos que gastam acima de R$200,00 com outras despesas: {percent_acima_200_despesas:.2f}%")
    print(f"Número de alunos com renda pessoal maior que a renda familiar: {renda_maior_pessoal}")
    print(f"Porcentagem gasta com alimentação em relação à renda pessoal: {percent_gasto_alimentacao:.2f}%")
    print(f"Porcentagem gasta com outras despesas em relação à renda familiar: {percent_gasto_despesas:.2f}%")

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

def q22():
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

#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexomasculinomais pesado;
#• amédia de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

def q23():
    atletas = []
    
    
    while True:
        nome = input("Nome do atleta (0 para sair): ")
        if nome == "0":
            break  
        
        sexo = input("Sexo (M/F): ")
        idade = int(input("Idade: "))
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        
        
        atletas.append({"nome": nome, "sexo": sexo, "idade": idade, "peso": peso, "altura": altura})
    
    
    atleta_mais_alta = max([a for a in atletas if a["sexo"] == "F"], key=lambda x: x["altura"], default=None)
    
    
    atleta_mais_pesado = max([a for a in atletas if a["sexo"] == "M"], key=lambda x: x["peso"], default=None)
    
    
    if len(atletas) > 0:
        media_idade = sum([a["idade"] for a in atletas]) / len(atletas)
    else:
        media_idade = 0 

    
    if atleta_mais_alta:
        print(f"Atleta feminina mais alta: {atleta_mais_alta['nome']} com {atleta_mais_alta['altura']}m")
    else:
        print("Nenhuma atleta feminina registrada.")
    
    if atleta_mais_pesado:
        print(f"Atleta masculino mais pesado: {atleta_mais_pesado['nome']} com {atleta_mais_pesado['peso']}kg")
    else:
        print("Nenhum atleta masculino registrado.")
    
    print(f"Média de idade dos atletas: {media_idade:.2f} anos")

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

def q27():
    total_litros = 0  

    while True:
      
        velocidade = float(input("Digite a velocidade do carro (valor negativo para sair): "))
        
        if velocidade < 0:
            break  
        
       
        tempo = float(input("Digite o tempo de viagem nessa velocidade (horas): "))
        
        
        distancia = velocidade * tempo
        
        
        litros_consumidos = distancia / 10
        
       
        total_litros += litros_consumidos
        
        
        print(f"Distância percorrida: {distancia:.2f} km, Litros consumidos: {litros_consumidos:.2f} L")

   
    print(f"Total de litros gastos na viagem: {total_litros:.2f} L")

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

def q25():
    total_imposto = 0  
    contribuintes_isentos = 0 

    while True:
       
        cic = int(input("Digite o CIC (0 para sair): "))
        
       
        if cic == 0:
            break
        
       
        dependentes = int(input("Número de dependentes: "))
        renda_bruta = float(input("Renda bruta anual: R$ "))
        
       
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

#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em umdeterminado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

def q26():
   
    audiencia = {4: 0, 5: 0, 7: 0, 12: 0}
    total_pessoas = 0  

    while True:
       
        canal = int(input("Digite o número do canal (4, 5, 7, 12, 0 para sair): "))
        
       
        if canal == 0:
            break
        
       
        if canal not in audiencia:
            print("Canal inválido, por favor insira 4, 5, 7 ou 12.")
            continue
        
       
        pessoas = int(input("Número de pessoas assistindo: "))
        
        
        audiencia[canal] += pessoas
        total_pessoas += pessoas

    
    if total_pessoas == 0:
        print("Nenhuma audiência registrada.")
    else:
        for canal, pessoas in audiencia.items():
            percentual = (pessoas / total_pessoas) * 100  
            print(f"Canal {canal}: {percentual:.2f}% de audiência")

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

def q27():
    melhor_cr = 0  
    melhor_cr_5_ou_mais = 0   
    alunos_com_5_ou_mais_disciplinas = 0  

    while True:
        
        matricula = int(input("Número da matrícula (0 para sair): "))
        
        if matricula == 0:
            break  
        
        if matricula < 1 or matricula > 5000:
            print("Matrícula inválida! A matrícula deve estar entre 1 e 5000.")
            continue  
        
        
        disciplinas = int(input("Quantidade de disciplinas cursadas: "))
        
        if disciplinas <= 0:
            print("Número de disciplinas inválido. Deve ser maior que 0.")
            continue  
        
        
        notas = []
        for i in range(disciplinas):
            while True:
                try:
                    nota = float(input(f"Nota da disciplina {i+1}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break 
                    else:
                        print("Nota inválida! A nota deve ser entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número para a nota.")
        
        
        cr = sum(notas) / disciplinas
        print(f"CR do aluno {matricula}: {cr:.2f}")
        
       
        if cr > melhor_cr:
            melhor_cr = cr
        
        
        if disciplinas >= 5:
            if cr > melhor_cr_5_ou_mais:
                melhor_cr_5_ou_mais = cr
            alunos_com_5_ou_mais_disciplinas += 1

    
    print(f"Melhor CR de todos os alunos: {melhor_cr:.2f}")
    if alunos_com_5_ou_mais_disciplinas > 0:
        print(f"Melhor CR dos alunos com 5 ou mais disciplinas: {melhor_cr_5_ou_mais:.2f}")
    else:
        print("Nenhum aluno com 5 ou mais disciplinas.")

#28. Construa umprograma que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#3.12. Exercícios da Aula 75
#• a quantidade de pessoas com idade superior a 50 anos;
#• amédia das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

def q28():
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

    
    media_alturas_10_20 = (soma_alturas_10_20 / contagem_10_20) if contagem_10_20 > 0 else 0
    
    
    percentual_peso_inferior_40 = (peso_inferior_40 / total_pessoas * 100) if total_pessoas > 0 else 0


    print(f"Quantidade de pessoas com idade superior a 50 anos: {quantidade_idade_maior_50}")
    print(f"Média das alturas das pessoas com idade entre 10 e 20 anos: {media_alturas_10_20:.2f} m")
    print(f"Porcentagem de pessoas com peso inferior a 40 kg: {percentual_peso_inferior_40:.2f}%")


#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em umdeterminado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

def q29():
    
    total_vendas = 0  
    vendas_por_codigo = {"L": 0, "A": 0, "H": 0}  

    while True:
        
        valor = float(input("Digite o valor da mercadoria (0 para sair): "))
        
        
        if valor == 0:
            break
        
        
        codigo = input("Digite o código da mercadoria (L, A, H): ").upper()
        
        
        if codigo in vendas_por_codigo:
            vendas_por_codigo[codigo] += valor
        else:
            print("Código inválido. Os códigos válidos são L (Limpeza), A (Alimentação), H (Higiene).")
            continue  
        
        
        total_vendas += valor

    
    print(f"Total vendido no dia: R$ {total_vendas:.2f}")
    for codigo, total in vendas_por_codigo.items():
        print(f"Total vendido no código {codigo}: R$ {total:.2f}")

#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, Vviúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• amédia das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.

def q30():

    
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
        else:
            print("Estado civil inválido! Digite novamente.")

    
    media_idades_viuvos = (soma_idades_viuvos / contagem_viuvos) if contagem_viuvos else 0

    
    percentual_desquitados_separados = (desquitados_separados / total_pessoas * 100) if total_pessoas else 0

    
    print(f"Quantidade de pessoas casadas: {casados}")
    print(f"Quantidade de pessoas solteiras: {solteiros}")
    print(f"Média das idades das pessoas viúvas: {media_idades_viuvos:.2f} anos")
    print(f"Porcentagem de pessoas desquitadas/separadas: {percentual_desquitados_separados:.2f}%")

questao = int(input('Questão a ser executada: '))


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
    case 26:
        q26()
    case 27:
        q27()
    case 28:
        q28()
    case 29:
        q29()
    case 30:
        q30()
    case _:
        print("Opção inválida. Digite um número entre 1 e 30.")
