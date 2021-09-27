# ALGORITMO COM  EM QUE  A VARIAVEL NUMERO_SECRETO É UMA STRING

print("*************************************")
print("olá bem-vindo no jogo de adivinhação")
print("*************************************")

numero_secreto="42"

chute=input("Digite o seu número:")

print("Você digitou:", chute)

if (numero_secreto == chute):
    print("você acertou")
else:
    print("você errou")

print("Fim do jogo!")