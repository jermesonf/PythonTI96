#importando biblioteca flet
from flet import *

#Classe que tem herança em uma classe do flet
class LoginView(UserControl):


    #Função/Metodo
    def __init__(self):

        super().__init__()

        self.login = TextField(label="Login")

        self.passWord = TextField(label="Password", password=True, can_reveal_password=True)

        self.btnEnter = ElevatedButton(text="Entrar")

        self.btnCriarConta = ElevatedButton(text="Criar Conta")



    #Metodo construtor
    #Retorna a tela pronta.
    def build(self):

        # TESTE
        # #Criando primeira linha responsiva
        # line1 = ResponsiveRow(controls=[Column(col=4,controls=[self.login], alignment=MainAxisAlignment.CENTER)])
        #
        # # Criando segunda linha responsiva
        # line2 = ResponsiveRow(controls=[Column(col=4, controls=[self.passWord], alignment=MainAxisAlignment.CENTER)])
        #
        # # Criando terceira linha responsiva
        # line3 = ResponsiveRow(controls=[Column(col=4, controls=[self.btnEnter],expand=True, alignment=MainAxisAlignment.CENTER)])

        layout = (ResponsiveRow(
            controls=[
            Column(
                col={"md":5,"lg":7},
                controls=[
                    self.login, self.passWord, self.btnEnter, self.btnCriarConta
                ]
            )
            ], alignment=MainAxisAlignment.CENTER
        )
        )

        #Retonar tudo isso acima dentro de colunas
        #return Row(controls=[Column(controls=[line1, line2, line3])])

        return layout