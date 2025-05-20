import random
import os
import time

def animacao_inicio_forca():
    limpar_tela()
    print("🎬 Iniciando o Jogo da Forca...\n")
    time.sleep(1)
    print("🪢  👤")
    time.sleep(0.5)
    print("     |")
    time.sleep(0.5)
    print("     |")
    time.sleep(0.5)
    print("    / \\")
    time.sleep(0.5)
    print("\n🧠 Prepare-se para adivinhar a palavra!\n")
    time.sleep(1.5)

def animacao_vitoria_forca(palavra):
    limpar_tela()
    print("🎉 Parabéns! Você venceu! 🎉\n")
    frames = [
        "  \\o/  ",
        "   |   ",
        "  / \\  ",
        f"\nA palavra era: {palavra}\n",
    ]
    for frame in frames:
        print(frame)
        time.sleep(0.5)

def animacao_derrota_forca(palavra):
    limpar_tela()
    print("☠️  Que pena, você perdeu!\n")
    frames = [
        "  💀",
        "  /|\\ ",
        "  / \\ ",
        f"\nA palavra era: {palavra}\n",
    ]
    for frame in frames:
        print(frame)
        time.sleep(0.5)

def desenhar_forca(tentativas_restantes):
    estagios = [
        """
         _______
        |/      |
        |      (_)
        |      \\|/
        |       |
        |      / \\
        |
        |_""",
        """
         _______
        |/      |
        |      (_)
        |      \\|/
        |       |
        |      / 
        |
        |_""",
        """
         _______
        |/      |
        |      (_)
        |      \\|/
        |       |
        |      
        |
        |_""",
        """
         _______
        |/      |
        |      (_)
        |      \\|
        |       |
        |      
        |
        |_""",
        """
         _______
        |/      |
        |      (_)
        |       |
        |       |
        |      
        |
        |_""",
        """
         _______
        |/      |
        |      (_)
        |      
        |       
        |      
        |
        |_""",
        """
         _______
        |/      |
        |      
        |      
        |       
        |      
        |
        |_"""
    ]
    print(estagios[6 - tentativas_restantes])

def limpar_tela():
    # Limpa a tela do console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def Forca():
    while True:
        # Função principal do jogo da forca
        limpar_tela()
        animacao_inicio_forca()
        print("🎮 Jogo da Forca 🎮")
        print("Adivinhe a palavra com base na dica!")
        # Lista de palavras com dicas
        palavras_com_dicas = [
        ("gato", "Animal que mia"),
        ("bola", "Usada para jogar futebol"),
        ("doce", "É bem gostoso e as crianças adoram"),
        ("fada", "Personagem mágica com asas"),
        ("livro", "Tem histórias e desenhos"),
        ("sapo", "Pula e não lava o pé"),
        ("cama", "Lugar onde dormimos"),
        ("lua", "Brilha no céu à noite"),
        ("peixe", "Nada na água"),
        ("urso", "Animal fofo, tem de pelúcia também"),
        ("nuvem", "Fica no céu, é branca e fofa"),
        ("sol", "Ilumina e esquenta o dia"),
        ("pato", "Animal que vive na água e faz 'quá quá'"),
        ("flor", "Colorida e nasce na natureza"),
        ("boca", "Usamos para falar e comer"),
        ]

        # Escolhe uma palavra e dica aleatoriamente
        palavra, dica = random.choice(palavras_com_dicas)
        palavra = palavra.lower()
        letras_descobertas = ["_" for _ in palavra]
        tentativas_restantes = 6
        desenhar_forca(tentativas_restantes)

        letras_erradas = []

        print("Dica:", dica)

        # Loop principal do jogo
        while tentativas_restantes > 0 and "_" in letras_descobertas:
            print("\nPalavra:", " ".join(letras_descobertas))
            print("Tentativas restantes:", tentativas_restantes)
            print("Letras erradas:", ", ".join(letras_erradas))
            
            letra = input("Digite uma letra: ").lower()

            if letra in palavra:
                for i, l in enumerate(palavra):
                    if l == letra:
                        letras_descobertas[i] = letra
            else:
                if letra not in letras_erradas:
                    letras_erradas.append(letra)
                    tentativas_restantes -= 1

        # Verifica se venceu ou perdeu
        if "_" not in letras_descobertas:
            animacao_vitoria_forca(palavra)
        else:
            animacao_derrota_forca(palavra)


        print("\n🔄 Vamos jogar novamente?")
        jogar_novamente = input("Digite 's' para continuar ou qualquer outra tecla para sair: ").lower()
        if jogar_novamente != "s":
            print("\n🙏 Obrigado por jogar! Até a próxima! 👋")
            return