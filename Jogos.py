import Forca
import Adivinha

def escolhe_jogo():
    print("\n=================================")
    print("****Bem vindo, Escolha um Jogo!****")
    print("=================================\n")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Insira o jogo: "))

    if(jogo == 1):
        print("Jogando Forca")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        Adivinha.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()