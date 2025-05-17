import random
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


#Codigo que colocara numeros e o usuario tera que adivinhar qual o maior
def adivinha_numero():
    print("Bem-vindo ao jogo de adivinhação de números!")
    print("Você terá que adivinhar qual número é maior entre dois números aleatórios.")
    
    while True:
        limpar_tela()
        # Gera dois números aleatórios entre 1 e 10
        # Garante que os dois números sejam diferentes
        while True:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            if num1 == num2:
                break
        
        print(f"Os números gerados são: {num1} e {num2}")
        
        # Pede ao usuário para adivinhar qual número é maior
        palpite = input("Qual número você acha que é maior? (Digite 1 ou 2) \n")
        
        # Verifica se o palpite está correto
        if (palpite == "1" and num1 > num2) or (palpite == "2" and num2 > num1):
            print("Parabéns! Você acertou!")
        else:
            print("Que pena! Você errou.")
        print("Vamos jogar novamente!")
        # Pergunta se o usuário quer jogar novamente
        jogar_novamente = input("Você quer jogar novamente? (s/n) \n")
        if jogar_novamente.lower() != "s":
            print("Obrigado por jogar! Até a próxima!")
            return