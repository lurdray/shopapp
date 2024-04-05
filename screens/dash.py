import flet as ft
from flet_route import Params, Basket
import requests


def dash(page: ft.Page, params:Params, basket:Basket):


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

    
    def service_card(id, image, text, text2, market, category):
        col1 = ft.Image(src=image, width=150, fit=ft.ImageFit.CONTAIN, border_radius=ft.border_radius.all(5))
        col2 = ft.Column([
                    ft.Text(text, size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(text2, size=10, color="grey600"),
                    ft.TextButton(
                        market,
                        icon="SHOP",
                        icon_color="AMBER",
                        on_click=lambda _: page.go(f"/detail/%s" % (id))
                    ),
                    ft.TextButton(
                        category,
                        icon="STOREFRONT",
                        icon_color="AMBER",
                        on_click=lambda _: page.go(f"/detail/%s" % (id))
                    ),
            
        ])
        
        service_card = ft.Card(
            color="rgba(255, 255, 255, 1)",
            elevation=5,
            width=350,
            
            content=ft.Container(
                padding=10,
                alignment=ft.alignment.center,
                ink=True,
                on_click=lambda _: page.go(f"/detail/%s" % (id)),
                content=ft.Column(
                            
                            [
                                ft.Row([col1, col2])
                                
                                
                            ]
                        ),
                    ),
                    
                )
        
        return service_card


    def items():
        
        
        items = []
        headers = {"Content-Type": "application/json; charset=utf-8"}
        shops = requests.get("https://shopowner.app/api/all/", headers=headers).json()["shops"]
        for item in shops:
            id = item["id"]
            image = "https://shopowner.app" + item["logo"] + "/"

            #image = "https://shopowner.app/media/account_files/logos/Alaba-Rago-Market.jpg/"
            #image = "https://dominuskelvin.dev/koo"
            
            name = item["name"][:15] + "..."
            description = item["description"][:25] + "..."
            market = item["market"]
            category = item["category"]
            items.append(
                ft.Container(
                    content=ft.Row([service_card(id, image, name, description, market, category)], alignment="center"),
                    alignment=ft.alignment.center,
                    width=400,
                    border_radius=ft.border_radius.all(5),
                )
            )

        return items

    return ft.View(
        "/dash/",
        controls=[

            ft.AppBar(
                leading=ft.Icon(ft.icons.STYLE),
                title=ft.Text("Shop Owner"),
                bgcolor=ft.colors.AMBER_100,
            ),

            ft.Container(height=10),

            ft.Column(spacing=0, controls=items()),

            #ft.ElevatedButton("Get Started", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=lambda _: page.go("/sign-up")),
            ft.Container(height=10),

            ft.NavigationBar(
                bgcolor=ft.colors.AMBER,
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
