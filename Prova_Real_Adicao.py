import random
import os
import time

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def Prova_real_Mais():
    print("🎉 Bem-vindo ao jogo Prova Real de Adição! 🎉")
    print("Descubra qual número está faltando para completar a adição.\n")
    time.sleep(1)

    while True:
        limpar_tela()
        
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        resultado = num1 + num2
        
        print(f"🧮 Descubra qual é o valor que falta para completar: {num1} + ? = {resultado}\n")
        palpite = input("👉 Qual número você acha que falta? \n")
        
        print("\n🔎 Conferindo sua resposta", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")
        
        try:
            if int(palpite) == resultado - num1:
                print("👏 Parabéns! Você acertou! 🎯")
            else:
                print(f"😢 Que pena! Você errou. O número correto era {resultado - num1}.")
        except ValueError:
            print("⚠️ Entrada inválida! Por favor, digite um número inteiro.")
        
        print("\n🔄 Vamos jogar novamente?")
        jogar_novamente = input("Digite 's' para continuar ou qualquer outra tecla para sair: ").lower()
        if jogar_novamente != "s":
            print("\n🙏 Obrigado por jogar! Até a próxima! 👋")
            return
