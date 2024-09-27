print("Olá Mundo!")

nome   = 'joca' #variavel global
idade  = 0
altura = 1.5 
print(f'Olá {nome} Mundo!')

def ola(nome): #variavel local
    print(f'Olá {nome} Seja Bem Vindo Mundo!')


ola('LUCA')
ola('TUCAS')

ola(input('Digite seu nome: '))

def num(idade):
    print("Insira numero: ")

num(input(idade))    