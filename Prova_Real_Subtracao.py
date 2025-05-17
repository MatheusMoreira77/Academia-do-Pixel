import random
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#Codigo que mostrara um calculo e o usuario tera que advinhar qual o valor que falta para descobrir o resutado

def Prova_real_Sub():
    print("Bem-vindo ao jogo Prova Real de Subtração!")
    print("Descubra qual número está faltando para completar a Subtração.")
    
    while True:
        limpar_tela()
        # Gera dois números aleatórios entre 1 e 10
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        resultado = num1 - num2

        if resultado < 0:
            resultado = num2 - num1



        print(f"Descubra qual é o valor que falta para descobrir o resultado: {num1} - ? = {resultado}")
        # Pede ao usuário para adivinhar qual número é maior
        palpite = input("Qual número você acha que falta? \n")
        # Verifica se o palpite está correto
        if int(palpite) == resultado + num1:
            print("Parabéns! Você acertou!")
        else:
            print("Que pena! Você errou.")

        print("Vamos jogar novamente!")
        # Pergunta se o usuário quer jogar novamente
        jogar_novamente = input("Você quer jogar novamente? (s/n) \n")
        if jogar_novamente.lower() != "s":
            print("Obrigado por jogar! Até a próxima!")
            return