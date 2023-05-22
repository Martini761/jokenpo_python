#Imports

from time import sleep
from os import system
import random

#Defeniçôes da Interface

def clean():
    system("cls")


#Variáveis

Intro = "Bem vindo ao pedra-papel-tesoura (Jokenpo)!"
Empate = "  Empate  "
nome_utilizador = str(input("Digite o seu nome de utilizador: "))
Pontos = ". . ."
tracos = "-=>"
agradecimentos = "Obrigado por jogar!"

#Introdução

clean()                                   #Limpar Console

for Char in Pontos:
    print(Char, end="")
    sleep(0.2)
clean()                                   #Limpar Console

#Jogo

def escolha_do_utilizador():
    
    escolha = input("Escolha o objeto predestinado: ")
    while escolha not in ["pedra", "papel", "tesoura"]:
        escolha = input("Erro: Por favor selecione UMA das opçoes [pedra, papel, tesoura]: ")
    return escolha

def escolha_da_maquina():
    
    opcoes_possiveis = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes_possiveis)

def vencedor(escolha_jogador , escolha_pc):
    
    if escolha_jogador == escolha_pc:
        for Char in Empate:
            print(Char, end="")
            sleep(0.07)
        sleep(2)
    
    elif (
        (escolha_jogador == "pedra" and escolha_pc == "tesoura") or
        (escolha_jogador == "papel" and escolha_pc == "pedra") or
        (escolha_jogador == "tesoura" and escolha_pc == "papel")
    ):
        print(f"O vencedor e {nome_utilizador} , parabens :P")
        sleep(2)


    else:
        print(f"Nao foi desta querido {nome_utilizador} !!")
        sleep(2)
        

def novo_jogo():
    
    for Char in Intro:
        print(Char, end="")
        sleep(0.07)
    clean()

    while True:
        
        clean()
        
        for Char in tracos:
            print(Char, end="")
            sleep(0.07)
        
        escolha_jogador = escolha_do_utilizador()
        escolha_pc = escolha_da_maquina()
        
        print(f"Tu escolheste: {escolha_jogador}")
        print(f"Computador escolhe: {escolha_pc}")
        print(vencedor(escolha_jogador, escolha_pc))
        clean()
        
        jogar_denovo = input("Deseja jogar denovo? (Sim/não): ")
        
        if jogar_denovo.lower() != "sim":
            for Char in agradecimentos:
                print(Char, end="")
                sleep(0.07)
            sleep(2)
            clean()
            break

novo_jogo()