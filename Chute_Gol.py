import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpar_tela()
    print("Bem-vindo ao jogo Chute ao Gol!")
    print("Descubra qual o resultado da operação matemática.")
    
    # Gera dois números aleatórios entre 1 e 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    sinais = ['+', '-']

    sinal = random.choice(sinais)

    if sinal == '+':
        resultado = num1 + num2
    else:
        resultado = num1 - num2

    print(f"Qual é o resultado de {num1} {sinal} {num2}?")