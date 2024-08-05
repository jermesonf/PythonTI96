from flet import *

class CadastreView(UserControl):

    #Funções
    def __init__(self):
        super().__init__()
        self.nome = TextField(label = "Nome: ")
        self.email = TextField(label = "E-mail: ")
        self.password = TextField(label = "Senha: ")
        self.btnCadastrar = ElevatedButton(text="Cadastrar")


    #Metodo Construtor
    def build(self):

        layout = (ResponsiveRow(
            controls=[
                Column(
                    col={"md": 5, "lg": 7},
                    controls=[
                        self.nome, self.email, self.password, self.btnCadastrar
                    ]
                )
            ], alignment=MainAxisAlignment.CENTER
        )
        )

        return layout