# ALGORITMO NUMERO_SECRETO ALEATÓRIO RANDOM.RANDOM()

import random

print("*************************************")
print("olá bem-vindo no jogo de adivinhação")
print("*************************************")

numero_secreto=random.randrange(1,101)
total_de_tentativas=3

for rodada in range(1,total_de_tentativas+1):
    print("Tentativa: {} de {}".format(rodada,total_de_tentativas))
    chute_str=input("Digite um número entre 1 e 100: ")
    chute=int(chute_str)
    print("Você digitou:", chute_str)

    if(chute<1 or chute>100):
        print("Você deve digitar um númeor entre 1 e 100!")
        continue

    acertou =numero_secreto == chute
    maior   =chute>numero_secreto
    menor   =chute<numero_secreto

    if (acertou):
        print("você acertou")
        break
    else:
        if (maior):
            print("você errou: O seu chute foi maior o que o número secreto")
        elif(menor):
            print("você errou: O seu chute foi menor o que o número secreto")


print("Fim do jogo!")