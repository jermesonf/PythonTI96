lista=["Carlos","Pedro","Lulu","Tita","José"]
listaIdades=[23,12,28,18,65,78]
listaSalarios=[2345.56,678.34,8888.10,9500.12,2001.12]

print("---------------------------------------------------------------------------------------------------------")

print("ADICIONAR NA LISTAS")
#Metodos de lista
# - adicionar na lista = append
listaSalarios.append(345.678)
print("Adicionado o valor 345.678 dentro dessa lista -> ", listaSalarios)

print("---------------------------------------------------------------------------------------------------------")
print("INDEX")
#Retorna o index de um determinado valor
listaSalarios.index(8888.10)
#Lembrando que o index se inicia em 0
# index = posição pense que o index é um ponteiro e aponta para onde este dado está guardado
print(listaSalarios.index(8888.10))
print(lista.index("Tita"))

print("---------------------------------------------------------------------------------------------------------")
print("SORT")

print("padrão")
print(lista)

print("ordem alfabética")
#O método sort
lista.sort() # organiza os elementos em ordem alfabética
print(lista)

print("maior para o menor")
lista.sort(reverse=True) #Organiza do maior para o menor
print(lista)

print("---------------------------------------------------------------------------------------------------------")

#Count vai contar a quantidade de vezes que o elemento aparece na lista
# exemplo se tiver dois carlos dentro da lista ira mostra 2 se tiver 1 carlos mostra 1
print("COUNT")
print("contar a quantidade de vezes que o elemento aparece na lista")
print(listaIdades.count(23)) #existe apenas um dado com numero 23 dentro dessa lista
print(lista.count("Carlos")) #existe apenas um carlos dentro dessa lista

print("Remover um valor da lista")
listaIdades.remove(12) #remove o dado 12 dessa lista
print("Removido o valor 12 dessa lista -> " , listaIdades)

print("---------------------------------------------------------------------------------------------------------")

print("Insert")
print("Repare no index 3 -> ",lista)
lista.insert(3,"Josevaldo") #Sobrescrevendo o index 3 com o seguitne dado
print("Inserido o josevaldo no lugar do josé que se encontra no index 3 -> ",lista) 