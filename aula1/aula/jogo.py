import random

pergunta = input("Deseja participar do jogo? ").strip().upper()
valorgerado = random.randint(0,5)
contador = 1;

while pergunta == "SIM":

    valor = int(input("Digite um número: ").strip().upper())

    if(valor == valorgerado):
        print("Você acertou! \nNumero Sorteado: ", valorgerado, "\nTentativas: ", contador)
        break;
    elif(contador == 5):
        print("Ta burro? \nTentativa: " ,contador)
        contador += 1
    elif(contador == 10):
        print("Desiste logo seu leso \nTentativa: " ,contador)
        contador += 1
    elif(contador == 15):
        print("Você é um perdedor! \nTentativa: " ,contador)
        break
    else:
        print("errou! \nTentativa: ", contador)
        contador += 1

    print("---------------------------------------------------------------")

