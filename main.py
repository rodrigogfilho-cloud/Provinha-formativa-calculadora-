import flet as ft

def main (pagina:ft.Page):
    pagina.window.width = 1000
    pagina.window.height = 800
    pagina.title='Calculadora (Prova-formativa)'
    pagina.horizontal_alignment= 'center'
    pagina.bgcolor="#011b4d"

    resultados = []


    #Título
    title = ft.Text(value='Calculadora Gordoxz',
                    size = 35,
                    color='#ffffff',
                    weight=ft.FontWeight.BOLD,
                    )

    #Linha dos valores
    value01= ft.TextField(value='',
                          label='Digite o número aqui',
                          width=200,
                          bgcolor="#4554aa",
                          border_radius=50,
                          color='#ffffff',
                         )

    value02= ft.TextField(value='',
                          label='Digite o número aqui',
                          width= 200,
                          bgcolor='#4554aa',
                          border_radius=50,color='#ffffff')

    row_values = ft.Row(controls=[value01, value02],
                        alignment='center',
                        )

    # Criação das def´s para gerar o resultado


    def adicao():
        valor_01 = int(value01.value)
        valor_02 =  int(value02.value)
        resultado = valor_01 + valor_02
        if resultado != 67:
            resultados.append(ft.Container(ft.Text(value= f'{valor_01} + {valor_02} = {resultado}', color='#ffffff',size=18),bgcolor="#5077F8",padding=6 ,
                                                       border_radius=20))
        elif resultado == 67:
             pagina.show_dialog(ft.AlertDialog(content=ft.Text("SIX SEVENNNNN 67"),
                                        open=True,
                                        ))

    def subtracao():
        valor_01 = int(value01.value)
        valor_02 =  int(value02.value)
        resultado = valor_01 - valor_02
        if resultado != 67:
            resultados.append(ft.Container(ft.Text(value= f'{valor_01} - {valor_02} = {resultado}', color='#ffffff',size=18),bgcolor="#5077F8",
                                           padding=6 ,
                                                                                      border_radius=20))
        elif resultado == 67:
             pagina.show_dialog(ft.AlertDialog(content=ft.Text("SIX SEVENNNNN 67"),
                                        open=True,
                                        ))
        
    def multi():
        valor_01 = int(value01.value)
        valor_02 =  int(value02.value)
        resultado = valor_01 * valor_02
        if resultado != 67:
            resultados.append(ft.Container(ft.Text(value= f'{valor_01} * {valor_02} = {resultado}', color='#ffffff',size=18),bgcolor="#5077F8",
                                           padding=6 ,
                                                                                      border_radius=20
                                           ))
        elif resultado == 67:
            pagina.show_dialog(ft.AlertDialog(content=ft.Text("SIX SEVENNNNN 67"),
                                       open=True,
                                       bgcolor="#f5e504",
                                       
                                    
                                       ))


    def divisao():
        valor_01 = int(value01.value)
        valor_02 =  int(value02.value)
        resultado = round(valor_01 / valor_02,2)
        if resultado != 67:
            # resultado.append (serve para adicionar o item a lista) ft.Container (serve para criar o container, para englobar tudo) ft.Text (é para inserir o value, que vai conter. Por ex: f'{valor_01} / {valor_02} = {resultado}' e o que vem depois, serve apenas para personalizar o Container e o text
            resultados.append(ft.Container(ft.Text(value= f'{valor_01} / {valor_02} = {resultado}', color='#ffffff',size=18),bgcolor="#5077F8",
                                           padding=6 ,
                                           border_radius=20))
        elif resultado == 67:
            pagina.show_dialog(ft.AlertDialog(content=ft.Text("SIX SEVENNNNN 67"),
                           open=True,
))

    # Botões dos cálculos

    botao_adicao = ft.Button(content='+',
                             on_click=adicao,
                             bgcolor="#89b2ff",
                             color='#ffffff',
                             )

   
    botao_subtracao = ft.Button(content='-',
                                 on_click=subtracao,
                             bgcolor="#89b2ff",
                             color='#ffffff')

   
    botao_multiplicacao = ft.Button(content='*',
                                    on_click=multi,
                             bgcolor="#89b2ff",
                             color='#ffffff')

    
    botao_divisao = ft.Button(content='/',
                              on_click=divisao,
                             bgcolor="#89b2ff",
                             color='#ffffff')

    row_calc = ft.Row(controls=[botao_adicao,
                                botao_subtracao,
                                botao_multiplicacao,
                                botao_divisao],
                                alignment='center')

    text_history = ft.Text(value='Histórico',
                        size = 25,
                        color='#ffffff',
                        weight=ft.FontWeight.BOLD,
                        )

    # Criar uma coluna, para colocar na lista de controls ( para aparecer na página ) OBS: 'resultado' é o nome da lista ( lista que os resultados dos calculos vão entrar ) 
    coluna = ft.Column(controls=resultados, )

    
    
    pagina.update()
    
    pagina.controls= [
         title,
         row_values,
         row_calc,
         text_history,
         coluna,
]

ft.run(main)