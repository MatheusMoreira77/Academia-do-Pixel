from Balanca import adivinha_numero
from Prova_Real_Adicao import Prova_real_Mais
from Prova_Real_Subtracao import Prova_real_Sub
from Chute_Gol import chute_ao_gol
from Forca import Forca
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao_nome(nome):
    limpar_tela()
    print("🎉 Nome registrado! 🎉\n")
    print("Apresentando jogador...")
    time.sleep(1)
    for letra in nome:
        print(letra, end='', flush=True)
        time.sleep(0.15)
    print(" 🔥 está pronto para jogar!")
    time.sleep(1.5)

def animacao_inicial():
    cenas = [
        "🕹️ ",
        "🕹️ Mini-Jogos em Pixel",
        "🕹️ Mini-Jogos em Pixel 🔢🔤⚽",
        "Carregando jogos...",
        "Preparando diversão para você!"
    ]
    for cena in cenas:
        limpar_tela()
        print(cena)
        time.sleep(0.8)

def animacao_tema(titulo):
    limpar_tela()
    print(f"🎮 Entrando no tema: {titulo} 🎮")
    time.sleep(1)

def animacao_jogo(jogo):
    limpar_tela()
    print(f"🧩 Carregando jogo: {jogo}...")
    time.sleep(1)

# Início do programa
animacao_inicial()
print("Bem-vindo ao programa de mini-jogos com Pixels!")

while True:
    nick = input("Qual é o seu nome? \n").strip()
    if nick:
        break


animacao_nome(nick)

while True:
    print("\nEscolha um dos temas:")
    print("1 - Português")
    print("2 - Matemática")
    print("3 - Cores")
    print("Digite 'sair' para encerrar.")

    escolha_tema = input("Sua escolha: ")

    if escolha_tema.lower() == 'sair':
        limpar_tela()
        print("🎉 Obrigado por jogar! Até a próxima! 🎉")
        input("Pressione Enter para sair.")
        break

    match escolha_tema:
        case "1":
            animacao_tema("Português")
            print("Você escolheu o tema Português!")
            print("Escolha um dos jogos abaixo:")
            print("1 - Forca 🔤")
            print("2 - Caça-palavras 🔎")
            print("3 - Complete o Alfabeto 🅰️➡️🆎")
            print("Digite 'sair' para encerrar.")
            if escolha_tema.lower() == 'sair':
                limpar_tela()
                print("🎉 Obrigado por jogar! Até a próxima! 🎉")
                input("Pressione Enter para sair.")
                break
            escolha_jogo = input("Qual jogo você quer jogar? \n")
            match escolha_jogo:
                case "1":
                    animacao_jogo("Forca")
                    Forca()
                case "2":
                    animacao_jogo("Caça-palavras")
                    # Caca_palavras()  # Descomente para jogar Caça-palavras
                case "3":
                    animacao_jogo("Complete o Alfabeto")
                    # Complete_alfabeto()  # Descomente para jogar Complete o Alfabeto
                case _:
                    print("🚫 Opção inválida! Por favor, escolha uma das opções.")

        case "2":
            animacao_tema("Matemática")
            print("Você escolheu o tema Matemática! ➕➖")
            print("Escolha um dos jogos abaixo:")
            print("1 - Balança ⚖️")
            print("2 - Adivinhação ❓")
            print("3 - Prova Real de Adição ➕")
            print("4 - Prova Real de Subtração ➖")
            print("5 - Chute ao Gol ⚽🥅")
            print("Digite 'sair' para encerrar.")
            if escolha_tema.lower() == 'sair':
                limpar_tela()
                print("🎉 Obrigado por jogar! Até a próxima! 🎉")
                input("Pressione Enter para sair.")
                break

            escolha_jogo = input("Qual jogo você quer jogar? \n")
            match escolha_jogo:
                case "1":
                    animacao_jogo("Balança")
                    adivinha_numero()
                case "2":
                    animacao_jogo("Adivinhação")
                    adivinha_numero()
                case "3":
                    animacao_jogo("Prova Real de Adição")
                    Prova_real_Mais()
                case "4":
                    animacao_jogo("Prova Real de Subtração")
                    Prova_real_Sub()
                case "5":
                    animacao_jogo("Chute ao Gol")
                    chute_ao_gol()
                case _:
                    print("🚫 Opção inválida! Por favor, escolha uma das opções.")
        case "3":
            print("\n🎨 Você escolheu o tema *CORES*! 🌈✨")
            print("Escolha um dos jogos abaixo:")
            print("1️⃣ - Sequenciador de Cores  🔴🟢🔵🟡")
            print("2️⃣ - Cores Rápidas ⚡🟣🟤⬜ \n")
            print("Digite 'sair' para encerrar.")
            escolha_jogo = input("Qual jogo você quer jogar? \n")
            match escolha_jogo:
                case "1":
                    animacao_jogo("Sequenciador de Cores")
                    # Sequenciador_de_cores()  # Descomente para jogar Sequenciador de Cores
                case "2":
                    animacao_jogo("Cores Rápidas")
                    # Cores_rapidas()  # Descomente para jogar Cores Rápidas
                case _:
                    print("🚫 Opção inválida! Por favor, escolha uma das opções.")

            if escolha_tema.lower() == 'sair':
                limpar_tela()
                print("🎉 Obrigado por jogar! Até a próxima! 🎉")
                input("Pressione Enter para sair.")
                break
        case _:
            print("🚫 Por favor, escolha Português ou Matemática.")
