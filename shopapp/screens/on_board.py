import flet as ft
from flet_route import Params, Basket



def on_board(page: ft.Page, params:Params, basket:Basket):


    page.title = "Shop Owner"
    page.fonts = {
        "TravelingTypewriter": "fonts/ojuju.ttf"
    }

    page.theme_mode = ft.ThemeMode.LIGHT

    def switch_theme_mode(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    return ft.View(
        "/on-board/",
        controls=[

            ft.AppBar(
                leading=ft.Icon(ft.icons.STYLE),
                title=ft.Text("Shop Owner"),
                bgcolor=ft.colors.AMBER_100,
            ),

            ft.SafeArea(ft.Switch(label="Dark Theme Mode", on_change=switch_theme_mode)),

            ft.Container(height=2),
            ft.Image(
                src="images/on_board.svg",
                width=250,
                height=250,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Container(height=5),

            ft.Text("Find Credible Shops Near You.", weight="bold", theme_style="titleLarge"),
            ft.Text("Explore recommended Shops that are in close prximity to you. Find trusted shops and discover what's new! ", text_align="center"),

            ft.Container(height=5),
            ft.ElevatedButton("I'm a buyer", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=lambda _: page.go("/dash")),
            ft.Container(height=2),
            ft.ElevatedButton("I'm' a shop owner", bgcolor="#161515", color="#FFC100", width="200", height="50", on_click=lambda _: page.go("/sign-up")),
            ft.Container(height=10),
            


        ],

        scroll="always",
        vertical_alignment="center",
        horizontal_alignment="center",
        padding=5,
    )
