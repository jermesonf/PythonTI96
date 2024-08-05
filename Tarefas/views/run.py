
#Importando o flet porem so PAGE, APP E VIEW
from flet import Page,app,View,Text

import views.loginView
#Importando a pasta local Views e a Classe LogginView
from views.loginView import LoginView

from views.cadastreView import CadastreView

# Mostra as coisas que foram importadas
# print(dir())

# Metodo principal
def main(page:Page):

    page.title="Gerenciador de Tarefas"

    #Insantciando
    viewLogin = LoginView()
    viewCadastre = CadastreView()

    #Adicionando a classe dentro da pagina
    # page.add(viewLogin)

    def eventoTrocarDeTela(e):

        if viewLogin.btnCriarConta:
            page.go("/cadastro")
            page.update()

    viewLogin.btnCriarConta.on_click = eventoTrocarDeTela

        # if viewLogin.login.value=="carlos" and viewLogin.passWord.value == "1234":
        #     page.go("/cadastro")
        #     page.update()
        # else:
        #     viewLogin.login.error_text="Login não está no sistema"
        #     viewLogin.passWord.error_text = "Login não está no sistema"
        #     viewLogin.login.update()
        #     viewLogin.passWord.update()


    # viewLogin.btnEnter.on_click=eventoTrocarDeTela

    #Criando funçâo que troca de rota
    def changeRoute (route):

            # Definindo que a rota principal seja "/" exemplo "google.com/"
        page.views.append(
        View(route="/",
            controls=[viewLogin])
        )

        if page.route=="/cadastro":
            page.views.append(
                View(
                route="/cadastro", controls=[viewCadastre]
                )
            )

    #Todas vez que mudar algo na tela é preciso usar o metodo update
        page.update()

    page.on_route_change=changeRoute
    page.go(page.route)

app(target=main)