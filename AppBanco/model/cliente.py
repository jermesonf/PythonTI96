
class Cliente:

    def __init__(self,nome,cpf,data_nascimento,senha,contato,endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.senha = senha
        self.contato = contato
        self.endereco = endereco

#cliente1 = Cliente("Carlos") #criado classe / objeto = instancia
#cliente2 = Cliente("Carlos")
#print(cliente1 == cliente2)

# cliente1 = Cliente("Joao","123.456.789-10","10/10/2010","1234")
#
# print(cliente1)#espaco na memoria
# print(cliente1.nome)
# print(cliente1.senha)
# print(cliente1.cpf)
# print(cliente1.data_nascimento)
