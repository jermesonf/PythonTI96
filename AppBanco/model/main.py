from model.contato import Contato #importando a classe contato e insanciando Contato
from model.cliente import Cliente #importando a classe cliente e instanciando Cliente
from model.endereco import Endereco #importando a classe endereco e instanciando Endereco


contato1 = Contato("(11)1234-56789","jao@emai.com")
endereco1 = Endereco("São Paulo", "Santana", "Voluntarios da patria", "02312345-123", "SP", "123")
cliente = Cliente("joao", "123.456.789.10", "12/12/2012", "1234",contato1,endereco1)

print(cliente.contato.email)
print(cliente.endereco.cep)

