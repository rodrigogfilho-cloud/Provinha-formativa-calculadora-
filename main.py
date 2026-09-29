import flet as ft

def main (pagina:ft.Page):
    pagina.window.width = 1000
    pagina.window.height = 800
    pagina.title='Calculadora (Prova-formativa)'
    pagina.horizontal_alignment= 'center'
    pagina.bgcolor="#0c5df3"

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
                          bgcolor='#ffffff')

    value02= ft.TextField(value='',
                          label='Digite o número aqui',
                          width= 200,
                          bgcolor='#ffffff')

    row_values = ft.Row(controls=[value01, value02],
                        alignment='center',
                        )

    

    def adicao():
        valor_01 = int(value01.value)
        valor_02 =  int(value02.value)
        resultado = valor_01 + valor_02
        if resultado != 67:
            print(f'{valor_01} + {valor_02} = {resultado}')
        elif resultado == 67:
                    print('SIXXXXXXXXXX SEVENNNNNNNNNN')


    def subtracao():
        valor_01 = int(value01.value)
        valor_02 =  int(value02.value)
        resultado = valor_01 - valor_02
        if resultado != 67:
            print(f'{valor_01} - {valor_02} = {resultado}')
        elif resultado == 67:
                    print('SIXXXXXXXXXX SEVENNNNNNNNNN')
        

    def multi():
        valor_01 = int(value01.value)
        valor_02 =  int(value02.value)
        resultado = valor_01 * valor_02
        if resultado != 67:
            print(f'{valor_01} * {valor_02} = {resultado}')
        elif resultado == 67:
            print('SIXXXXXXXXXX SEVENNNNNNNNNN')

    def divisao():
        valor_01 = int(value01.value)
        valor_02 =  int(value02.value)
        resultado = round(valor_01 / valor_02,2)
        
        if resultado != 67:
            print(f'{valor_01} / {valor_02} = {resultado}')
        elif resultado == 67:
            print('SIXXXXXXXXXX SEVENNNNNNNNNN')


    botao_adicao = ft.Button(content='+',
                             on_click=adicao,
                             bgcolor="#89b2ff",
                             color='#ffffff')

   
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
                        bgcolor="#010a8f",
                        )
    
    pagina.update()
    
    pagina.add(title)
    pagina.add(row_values)
    pagina.add(row_calc)
    pagina.add(text_history)

ft.run(main)