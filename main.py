from Balanca import adivinha_numero
from Prova_Real_Adicao import Prova_real_Mais
from Prova_Real_Subtracao import Prova_real_Sub
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Bem vindo ao programa de mini-jogos com Pixels!")

while True:

    nick = input("Qual é o seu nome? \n").strip()
    if nick:
        break

print(f"Olá, {nick}! Vamos começar a jogar!")

while True:
    print("\nEscolha um dos temas:")
    print("1 - Português")
    print("2 - Matemática")
    print("Digite 'sair' para encerrar.")

    escolha_tema = input("Sua escolha: ")

    if escolha_tema.lower() == 'sair':
        limpar_tela()
        print("Obrigado por jogar! Até a próxima!")
        input("Pressione Enter para sair.")
        break

    match escolha_tema:
        case "1":
            print("Você escolheu o tema Português!")
            print("Escolha um dos jogos abaixo:")
            print("1 - Forca")
            print("2 - Caça-palavras")
            print("3 - Complete o Alfabeto")
        case "2":
            print("Você escolheu o tema Matemática!")
            print("Escolha um dos jogos abaixo:")
            print("1 - Balanaça")
            print("2 - Adivinhação")
            print("3 - Prova Real de Adição")
            print("4 - Prova Real de Subtração")
            escolha_jogo = input("Qual jogo você quer jogar? \n")
            match escolha_jogo:
                case "1":
                    print("Você escolheu o jogo Balança!")
                    adivinha_numero()
                case "2":
                    print("Você escolheu o jogo Adivinhação!")
                case "3":
                    print("Você escolheu o jogo Prova Real de Adição!")
                    Prova_real_Mais()
                case "4":
                    print("Você escolheu o jogo Prova Real de Subtração!")
                    Prova_real_Sub()
                case _:
                    print("Opção inválida! Por favor, escolha uma das opções escritas.")
        case _:
            print("Por favor, escolha Português ou Matemática.")