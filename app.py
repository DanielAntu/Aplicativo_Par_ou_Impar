import flet as ft
from uteis import reset, calculo

def main(page: ft.Page):
    page.title = 'Par ou Impar'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    num = ft.TextField(label='Digite um número', keyboard_type='NUMBER')
    res = ft.Text(value='Não Informado', text_align='CENTER', width=100, weight=ft.FontWeight.BOLD)

    def click_reset(e):
        reset.reset_input(num)
        page.update()

    def click_calcular(e):
        if(num.value.isnumeric()):
            res_num = calculo.Calcular(int(num.value))
            res.value = str(res_num)
            num.value = ''
        else:
            res.value = 'Não Informado'
            num.value = ''

        page.update()

    c1 = ft.Container(
            ft.Column(
                [
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text(value='Digite o número no campo abaixo:', size=20, color=ft.colors.WHITE, text_align='CENTER', weight=ft.FontWeight.BOLD),
                                num,
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(text='Calcular', bgcolor=ft.colors.GREEN_500, color=ft.colors.WHITE, on_click=click_calcular),
                                            ft.ElevatedButton(text='Apagar', bgcolor=ft.colors.RED_500, color=ft.colors.WHITE, on_click=click_reset)
                                        ],
                                    ),
                                    width=1300,
                                    padding=10
                                )
                            ]
                        ),
                        alignment=ft.alignment.center,
                        height=200,
                        width=1300
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text('O número é:', size=20, weight=ft.FontWeight.BOLD),
                                res
                            ]
                        ),
                        alignment=ft.alignment.bottom_center,
                        bgcolor=ft.colors.WHITE,
                        width=1300,
                        height=90,
                    )
                ],
                alignment='Top'
            ),
            bgcolor=ft.colors.INDIGO_200,
            width=1500,
            height=900,
            padding=10,
            alignment=ft.alignment.bottom_center,
        )
    

    page.add(c1)


ft.app(target=main)