from flet import *

#Clone do Whatsaap

#Variaveis
corBarraAPP = "#085567"
corpoTextoFundo = "#91ddd9"
corTextoUsuario = "#d6fdc6"
corDeTexto = "#ffffff"

#Função main -> Método principal
def main(page:Page):

    # CONFIGURAÇÕES DA TELA

    #Titulo da página   <tile> Clone zap </title>
    page.title = "Clone Zap"

    #Tamanho padrão da tela
    page.windows_width=412
    page.window_min=915

    #Tamanho minimo da tela
    page.window_min_width=412
    page.window_min_height=915

    #Tamanho maximo da tela
    page.window_max_width=412
    page.window_max_height=915

    #Organizar os elementos no centro da tela
    page.window_center()

    #Atiaçozar a página com os elementos inseridos acima
    page.update()

    # FIM CONFIGURAÇÕES DA TELA


    # ELEMENTOS DA TELA

    #Criando icone para avatar
    avatar=CircleAvatar(foreground_image_src="img/Avatar.png", width=50)

    # #Criando linha para o avatar
    # linhaIconeAvatar=Row(controls=[IconButton(icon=icons.ARROW.BACK, icon_color="corDeTexto"), avatar])

    #Criando o Nome e estado
    nome=Text("Nome do Usuario", size=18, color=corDeTexto)
    estado=Text("online", size=16, color=corDeTexto)

    colunaNomeEstado=Column(controls=[nome,estado])

    iconeCamera=Icon(icons.VIDEO_CAMERA_FRONT_ROUNDED, color=corDeTexto)
    iconeTelefone=Icon(icon.PHONE, color=corDeTexto)

    linhaCentral=Row(controls=[avatar, colunaNomeEstado])


    #Definições para a barra superior
    #leading = elemento que fica a esquerda, no caso a seta
    #title = o que representa o titulo da pagina, no caso imagem do usuario, nome e estado
    #action são os icones de camera, telefone e 3 pontos que ao clicar mostra um coluna com uma lista.
    barra=AppBar(leading=IconButton(icon=icons.ARROW.BACK, icon_color=corDeTexto), title=linhaCentral, center_title=True, actions=[iconeCamera,iconeTelefone,PopupMenuButton(
        items=[PopupMenuButton(text="Item 1"),
               PopupMenuButton(text="Item 2"),
               PopupMenuButton(text="Item 3"),], icon_color=corDeTexto
    )], bgColor=corBarraAPP)

    #Adicionando a barra a pagina
    page.add(barra)

    #Atualizando a pagina para receber as atualizações
    page.update()

    # FIM ELEMENTOS TELA

app(main)