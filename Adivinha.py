import random

def jogar():
    print("\n=================================")
    print("Bem vindo ao jogo da Adivinhação!")
    print("=================================\n")

    #Gerando número secreto e total tentativas e pontos (As Variávies)
    numero_secreto = random.randrange(1, 101) # 0.0 1.0
    total_tentativas = 0
    pontos = 1000

    #Definindo a quntiade de tentativas que a pessoa terá de acordo com a dificuldade
    print("Escolha o nivel de dificuldade!")
    print("(1) Facil (2)Médio e (3)Difícil")

    nivel = int(input("Escolha o nivel desejado: "))
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel==2):
        total_tentativas = 10
    else:
        total_tentativas = 5
        
    #Definindo Pontuação (quanto mais disteante o numero colocado for do chute mais pontos vc perde)    


    #Rodar a em laço de repetição as tentativas
    for rodada in range(1, total_tentativas + 1):
        print("Tentativa, {} de {}".format(rodada, total_tentativas))
        chute= int(input("Digite um número: "))
        
        if chute > 100 or chute < 0:
            print("Digite um número de 1 a 100!!")
            continue
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Parabéns! você acertou e fez {} pontos.".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior que o número secreto")
            if (rodada == total_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(menor):
                print("Que pena você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(chute - numero_secreto)   #pontos perdidos da rodada
            pontos = pontos - pontos_perdidos               #subtraindo os pontos perdidos da pontuação total 

    print("\n Fim de jogo") 
if(__name__ == "__main__"):
    jogar()