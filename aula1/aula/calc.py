from flet import *

# def somar(val1, val2):
#     resposta = float(val1) + float(val2)
#     return resposta

def main (page:Page):
    page.title="Somar"
    page.window_min_width = 600
    page.window_min_height = 700

    titulo = Text("Somar", size = 20, weight = FontWeight.BOLD, color="#5f95ed")
    valor1 = TextField(label="Digite o primeiro valor")
    valor2 = TextField(label="Digite o segundo valor")

    btnSomar = ElevatedButton(text="+")
    btnSubtrair = ElevatedButton(text="-")
    btnMultiplicar = ElevatedButton(text="*")
    btnDividir = ElevatedButton(text="/")

    respostaSoma = Text("")

    def verificarResposta(e):
        print(valor1.value + valor2.value)
        respostaSoma.value=(float(valor1.value)+float(valor2.value))
        respostaSoma.update()

    def verificarRespostaSubtrair(e):
        respostaSoma.value=(float(valor1.value)-float(valor2.value))
        respostaSoma.update()

    def verificarRespostaMultiplicar(e):
        respostaSoma.value=(float(valor1.value)*float(valor2.value))
        respostaSoma.update()

    def verificarRespostaDividir(e):
        respostaSoma.value=(float(valor1.value)/float(valor2.value))
        respostaSoma.update()


    btnSomar.on_click = verificarResposta
    btnSubtrair.on_click = verificarRespostaSubtrair
    btnMultiplicar.on_click = verificarRespostaMultiplicar
    btnDividir.on_click = verificarRespostaDividir


    lineTitulo = Row(controls=[titulo], alignment=MainAxisAlignment.CENTER)

    line2 = Row(controls=[

                            Column(controls=[valor1]),
                            Column(controls=[valor2])

                         ], alignment=MainAxisAlignment.SPACE_AROUND)

    line3 = Row(controls=[respostaSoma], alignment=MainAxisAlignment.CENTER)

    linebtnSomarSubtrair = Row(controls = [
                                            Column(controls=[btnSomar]),
                                            Column(controls=[btnSubtrair])
                                          ], alignment=MainAxisAlignment.CENTER)

    linebtnMultiplicarDividir = Row(controls=[
                                            Column(controls=[btnMultiplicar]),
                                            Column(controls=[btnDividir])
                                        ], alignment=MainAxisAlignment.CENTER)


    page.add(lineTitulo)
    page.add(line2)
    page.add(linebtnSomarSubtrair)
    page.add(linebtnMultiplicarDividir)

    page.add(Divider())

    page.add(line3)
    page.update()


app(main)