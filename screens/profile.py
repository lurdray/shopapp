import flet as ft
from flet_route import Params, Basket
from flet import IconButton



def profile(page: ft.Page, params:Params, basket:Basket):


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
                bgcolor=ft.colors.TRANSPARENT,
            ),

            ft.SafeArea(ft.Switch(label="Dark Theme Mode", on_change=switch_theme_mode)),

            ft.Container(height=10),

            ft.Card(
                elevation=10,
                width="1200",
                height="800",
                
                content=ft.Container(
                    padding=10,
                    content=ft.Column(
                                [
                                    ft.Image(src="images/1.jpe", width=150, fit=ft.ImageFit.CONTAIN, border_radius=ft.border_radius.all(10)), 
                                    ft.Text("Odiaga Raymond")
                                ], alignment="center"
                            ),
                        ),
                        
                    ),

            ft.Container(height=10),
            ft.NavigationBar(
                destinations=[
                    ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                    ft.NavigationDestination(icon=ft.icons.APP_BLOCKING_ROUNDED, label="My Business"),
                    ft.NavigationDestination(icon=ft.icons.HEADPHONES, label="Help"), 
                ]
            ),
            ft.Container(height=10),

            


        ],

        scroll="always",
        vertical_alignment="center",
        horizontal_alignment="center",
        padding=5,
    )
