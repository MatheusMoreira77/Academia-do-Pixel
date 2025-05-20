import random
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_acerto_balcanca():
    frames = [
        "⚖️   ",
        "   ⚖️",
        "      ⚖️✅",
    ]
    for frame in frames:
        limpar_tela()
        print("Você acertou!\n")
        print(frame)
        time.sleep(0.5)

def animacao_erro_balanca():
    frames = [
        "⚖️   ",
        "⚖️❌  ",
        "💥   ",
    ]
    for frame in frames:
        limpar_tela()
        print("Você errou!\n")
        print(frame)
        time.sleep(0.5)

def animacao_inicio_balanca():
    limpar_tela()
    print("🧠 Carregando jogo da Balança...\n")
    time.sleep(1)
    print("⚖️  ⚖️  ⚖️")
    time.sleep(1)
    print("Vamos testar seu raciocínio!\n")
    time.sleep(1.5)


#Codigo que colocara numeros e o usuario tera que adivinhar qual o maior
def adivinha_numero():
    animacao_inicio_balanca()
    print("Bem-vindo ao jogo de adivinhação de números!")
    ...
    print("Você terá que adivinhar qual número é maior entre dois números aleatórios.")
    
    while True:
        limpar_tela()
        # Gera dois números aleatórios entre 1 e 10
        # Garante que os dois números sejam diferentes
        while True:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            if num1 != num2:
                break
        
        print(f"Os números gerados são: {num1} e {num2}")
        
        # Pede ao usuário para adivinhar qual número é maior
        palpite = input("Qual número você acha que é maior? (Digite 1 ou 2) \n")
        
        # Verifica se o palpite está correto
        if (palpite == "1" and num1 > num2) or (palpite == "2" and num2 > num1):
            animacao_acerto_balcanca()
        else:
            animacao_erro_balanca()

        print("\n🔄 Vamos jogar novamente?")
        
        # Pergunta se o usuário quer jogar novamente
        jogar_novamente = input("Digite 's' para continuar ou qualquer outra tecla para sair: ").lower()
        if jogar_novamente != "s":
            print("\n🙏 Obrigado por jogar! Até a próxima! 👋")
            return