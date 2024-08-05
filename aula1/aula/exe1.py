#Criando lista

lista_cpf = ["123.456.789-11".replace(".","").replace("-",""),"119.876.543-21".replace(".","").replace("-",""),"157.851.431-21".replace(".","").replace("-","")]
print(lista_cpf)

print("########### for ##############")

for index, cpf in enumerate(lista_cpf):
    lista_cpf=cpf.replace(".","").replace("-","")
    print("-------------------------------")
    print(lista_cpf)