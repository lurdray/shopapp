import flet as ft
from flet_route import Params, Basket
import requests



def sign_in(page: ft.Page, params:Params, basket:Basket):


    page.title = "Sign up"

    page.fonts = {
        "TravelingTypewriter": "fonts/ojuju.ttf"
    }

    email = ft.TextField(hint_text="Email Address..", width=300, height=50, border_radius=20)
    password = ft.TextField(hint_text="Password..", width=300, height=50, border_radius=20, password=True)

    page.theme_mode = ft.ThemeMode.LIGHT

    def switch_theme_mode(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    

    def handle_signin(e):
            
            print("gdfg")
            email.error_text = ""
            password.error_text = ""
            if not email.value:
                email.error_text = "missing email..."
                page.update()
            elif not password.value:
                password.error_text = "missing password..."
                page.update()

            else:
                req = requests.post("https://shopowner.app/api/sign-in/", data={"email":email.value, "password":password.value}).json()
                
                print(req)
                page.session.set("id", req["id"])

                page.go("/dash/")
                page.update()
                

    
    return ft.View(
        "/sign-up/",
        controls=[

            ft.AppBar(
                leading=ft.Icon(ft.icons.STYLE),
                title=ft.Text("Shop Owner"),
                bgcolor=ft.colors.AMBER_100,
            ),

            ft.SafeArea(ft.Switch(label="Dark Theme Mode", on_change=switch_theme_mode)),

            ft.Container(height=10),
            ft.Image(
                src="images/sign_up.svg",
                width=150,
                height=150,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Container(height=5),
            ft.Text("Sign in", weight="bold", theme_style="titleLarge"),

            ft.Container(height=5),
            email,
            password,
            ft.Container(height=5),
            ft.ElevatedButton("Sign In", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_signin),
            ft.TextButton(
                "Don't have an account?",
                icon="account_circle",
                icon_color="AMBER",
                on_click=lambda _: page.go("/sign-up")
            ),
            ft.Container(height=10),

            


        ],

        scroll="always",
        vertical_alignment="center",
        horizontal_alignment="center",
        padding=5,
    )

