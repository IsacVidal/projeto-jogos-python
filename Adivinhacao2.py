# ALGORITMO COM  EM QUE TRANSFORMAMOS A VARIAVEL CHUTE_STR EM INT.

print("*************************************")
print("olá bem-vindo no jogo de adivinhação")
print("*************************************")

numero_secreto=42
total_de_tentativas=3
rodada=1

while (rodada<=total_de_tentativas):
    print("Tentativa: {} de {}".format(rodada,total_de_tentativas))
    chute_str=input("Digite o seu número:")
    chute=int(chute_str)
    print("Você digitou:", chute_str)

    acertou =numero_secreto == chute
    maior   =chute>numero_secreto
    menor   =chute<numero_secreto

    if (acertou):
        print("você acertou")
    else:
        if (maior):
            print("você errou: O seu chute foi maior o que o número secreto")
        elif(menor):
            print("você errou: O seu chute foi menor o que o número secreto")
    rodada=rodada+1


print("Fim do jogo!")