#ENQUANTO CONDIÇÃO FIXA DE LOOP

# funciona com uma condição verdadeira, enquanto ela for verdadeira
# count = 0
#
# while count < 10:
#     #Incremento
#     count += 1
#     print(count)

print("------------ SISTEMA ---------------")

#SISTEMA
pergunta = input("Deseja entrar no sistema: ").strip().upper()

listaNome = []
while pergunta == "SIM":
    print("Dentro do sistema")
    nome = input("Digite o seu nome: ").strip().upper()
    listaNome.append(nome)
    pergunta = input("Deseja continuar dentro do sistema? ").strip().upper()

print(listaNome)

#SISTEMA IDADE
print("------------ SISTEMA IDADE ---------------")

perguntaIdade = input("Deseja entrar no sistema IDADE? ").strip().upper()
listaIdade = []

while perguntaIdade == "S":

    print("Dentro do sistema IDADE")
    idade = int(input("Digite sua idade: ")) #Definindo a lista como inteiro para poder organizar
    listaIdade.append(idade)
    perguntaIdade = input("Deseja continuar no sistema IDADE? ").strip().upper()



listaIdade.sort()
print(listaIdade)

media = sum(listaIdade)/len(listaIdade)
print(media)


print("------------ SISTEMA SOMA ---------------")

listaIdade2 = [3,23,66,10,67]

#A função sum vai somar os valores dentro da lista
print(sum(listaIdade2))

# tamanho, verifica a quantidade de elementos dentro da minha lista
print(len(listaIdade2))
media2 = sum(listaIdade2)/len(listaIdade2)
print(media2)