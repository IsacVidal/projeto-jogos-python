import forca
import Adivinhacao6

def escolhe_jogo():
    print("*************************************")
    print("*****Escolha o jogo*****")
    print("*************************************")

    print("(1) Forca (2) Adivinhação")
    jogo=int(input("Qual é o jogo?"))

    if(jogo==1):
        print("Jogar o jogo da forca")
        forca.jogar()
    elif(jogo==2):
        print("Jogar o jogo de adivinhação")
        Adivinhacao6.jogar()

if __name__=="__main__":
    escolhe_jogo()

