import random
from flet import *

def resposta(resp):
    pc = random.randint(0,10)
    if int(resp) == pc:
        return f"Parabéns o valor é realmente {resp}"
    else:
        return f"Você errou feio a resposta era {pc} "

def main (page:Page):
    page.title="Jogo"
    page.window_min_width = 600
    page.window_min_height = 700

    #Elementos da tela
    # TEXT() = elemento texto
    # weight = espessura do texto tipo deixar ele Bold, negrito, italico
    titulo = Text("Vamos Jogar !", size=20, weight = FontWeight.BOLD, color="#5f95ed")
    img_totem=Image(src="img/joaoEmbaixadinha.jpg")
    entradaResposta = TextField(label="Resposta")
    btnTentar = ElevatedButton(text="Tentar")
    respostaCorreta = Text("")


    #funçoes
    def verificarRepost(e):
        #seria como um textbox.text
        resposta(entradaResposta.value)
        respostaCorreta.update()

    btnTentar.on_click = verificarRepost()
    #Organizadores de conteudo / container
    #Cirado uma linha para centralizar os elementos
    #controls permite inserir uma lista de elementos
    lineTitulo = Row(controls=[titulo], alignment = MainAxisAlignment.CENTER)

    line2 = Row(controls=[
                            Column(controls=[img_totem]),
                            Column(controls=[entradaResposta, btnTentar], horizontal_alignment=CrossAxisAlignment.CENTER)
                           ], alignment=MainAxisAlignment.SPACE_AROUND)

    line3 = Row(controls=[
                                          Column(controls=[img_totem]),
                                          Column(controls=[respostaCorreta])
                                      ], alignment=MainAxisAlignment.CENTER)


    page.add(lineTitulo)
    page.add(line2)
    page.add(Divider())
    page.add(line3)
    page.update()

    page.add(titulo)
    page.update()

# estou passando uma função para dentro de outra função
#função app recebendo como parametro a função main
app(main)