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
        for x in range(10):
                proximo = anterior + atual
                print(proximo,end="")
                anterior = atual
                atual = proximo

q6()