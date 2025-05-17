import random
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_gol_cobertura():
    cenas = [
        "⚽         🥅",      # Bola começa
        "   ⚽      🥅",      # Sobe um pouco
        "     ⚽    🥅",      # Mais alto
        "       ⚽  🥅",      # No alto
        "         ⚽🥅",      # Chegando ao gol
        "       🧍   ⚽🥅",    # Goleiro não alcança
        "         💥⚽🥅",    # Gol no ângulo
        "          🥅\n\n🏹 Gol por cobertura! Uma pintura de gol!"
    ]

    for cena in cenas:
        limpar_tela()
        print("Chutando a bola...\n")
        print(cena)
        time.sleep(0.4)



def animacao_gol_canto():
    cenas = [
        "⚽         🥅",     
        "  ⚽       🥅",     
        "    ⚽     🥅",     
        "      ⚽   🥅",     
        "       ⚽  🥅",     
        "        ⚽🧍🥅",    # Goleiro está no meio
        "        🕴️⚽🥅",    # Goleiro tenta pular
        "         💥⚽🥅",   # Bola entra no canto
        "          🥅\n\n🎯 Golaço no canto! Sem chance para o goleiro!"
    ]

    for cena in cenas:
        limpar_tela()
        print("Chutando a bola...\n")
        print(cena)
        time.sleep(0.4)



def animacao_chute():
    

    # Cada posição é a bola + espaços + gol fixo
    posicoes_bola = [
        "⚽        🥅",
        "  ⚽      🥅",
        "    ⚽    🥅",
        "      ⚽  🥅" ,
        "        ⚽ 🥅"
    ]

    for linha in posicoes_bola:
        limpar_tela()
        print("Chutando a bola...\n")
        print(linha)
        time.sleep(0.4)

def animacao_defesa_estilosa():
    cenas = [
        "⚽        🥅",      
        "  ⚽      🥅",     
        "    ⚽    🥅",     
        "      ⚽  🥅",     
        "        ⚽🧍🥅",   # Goleiro no meio do gol
        "        🧍✋⚽🥅",  # Goleiro estica a mão
        "        🧍💥⚽🥅",  # Defesa feita
        "        🧍🥅\n\n🧤 Defesa espetacular do goleiro!"
    ]

    for cena in cenas:
        limpar_tela()
        print("Chutando a bola...\n")
        print(cena)
        time.sleep(0.5)


def animacao_trave():
    cenas = [
        "⚽        🥅",     # Bola no início
        "  ⚽      🥅",
        "    ⚽    🥅",
        "      ⚽  🥅",
        "        💥⚽🥅",   # Bola bate na trave
        "      ⚽💫   🥅",  # Bola voltando
        "    ⚽       🥅",
        "  ⚽         🥅",
        "⚽            🥅\n\n💥 A bola bateu na trave e voltou!"
    ]

    for cena in cenas:
        limpar_tela()
        print("Chutando a bola...\n")
        print(cena)
        time.sleep(0.4)

def animacao_erro():
    cenas = [
        "⚽         🥅",     # Preparando chute
        "  ⚽       🥅",     # Bola no meio
        "    ⚽     🥅",     # Bola se aproximando do gol
        "      🧍🥅",       # Goleiro aparece
        "     🧍💨⚽",     # Goleiro pula e defende
        "      🧍⚽",      # Bola na mão do goleiro
        "      🧍\n⚽ \nfoi defendida!"  # Final
    ]

    for cena in cenas:
        limpar_tela()
        print("Chutando a bola...\n")
        print(cena)
        time.sleep(0.5)

def chute_ao_gol():
    while True:
        limpar_tela()
        print("⚽ Bem-vindo ao jogo Chute ao Gol! ⚽")
        print("Descubra qual o resultado da operação matemática.\n")
        
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        sinais = ['+', '-']
        sinal = random.choice(sinais)

        if sinal == '-' and num1 < num2:
            num1, num2 = num2, num1

        if sinal == '+':
            resultado = num1 + num2
        else:
            resultado = num1 - num2

        print(f"Qual é o resultado de {num1} {sinal} {num2}?")

        resposta = input("Digite o resultado: ")
        if resposta.isdigit() and int(resposta) == resultado:
            animacoes_gol = [animacao_chute, animacao_gol_canto, animacao_gol_cobertura]
            random.choice(animacoes_gol)()
            print("\n🎉 GOL!!! Você acertou! 🎉")

        else:
            animacoes_erro = [animacao_erro, animacao_trave, animacao_defesa_estilosa]
            random.choice(animacoes_erro)()
            print(f"\n😢 Que pena! Você errou. O resultado correto é {resultado}.")

        print("\nVamos jogar novamente!")
        jogar_novamente = input("Você quer jogar novamente? (s/n) \n")
        if jogar_novamente.lower() != "s":
            print("Obrigado por jogar! Até a próxima!")
            return

if __name__ == "__main__":
    chute_ao_gol()
