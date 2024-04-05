import flet as ft
from flet_route import Params, Basket
import requests



def sign_up(page: ft.Page, params:Params, basket:Basket):


    page.title = "Sign up"

    page.fonts = {
        "TravelingTypewriter": "fonts/ojuju.ttf"
    }
    #page.bgcolor = "#f8e2bf"

    email = ft.TextField(hint_text="Email Address..", width=300, height=50, border_radius=20)
    password1 = ft.TextField(hint_text="Password..", width=300, height=50, border_radius=20, password=True)

    page.theme_mode = ft.ThemeMode.LIGHT

    def switch_theme_mode(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    

    def handle_signup(e):
            
            print("gdfg")
            email.error_text = ""
            password1.error_text = ""
            if not email.value:
                email.error_text = "missing email..."
                page.update()
            elif not password1.value:
                password1.error_text = "missing password..."
                page.update()

            else:
                #import json
                headers = {"Content-Type": "application/json; charset=utf-8"}
                req = requests.post("https://shopowner.app/api/sign-up/", headers=headers, json={"email":email.value, "password":password1.value}).json()
                print(req)
                #req = json.loads(req)
                #print(req)
                
                #print(req["status"])
                #if req:
                #     ft.AlertDialog(
                #        title=ft.Text("Hey there!"), on_dismiss=lambda e: print("Close")
                #    )
                     
                #else:
                print(req)
                page.session.set("id", req["id"])

                page.go("/sign-up/finish/")
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
            ft.Text("Create an account", weight="bold", theme_style="titleLarge"),

            ft.Container(height=5),
            email,
            password1,

            ft.Container(height=5),
            ft.ElevatedButton("Sign Up", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_signup),
            ft.TextButton(
                "I already have an account",
                icon="account_circle",
                icon_color="AMBER",
                on_click=lambda _: page.go("/sign-in")
            ),
            ft.Container(height=10),

            


        ],

        scroll="always",
        vertical_alignment="center",
        horizontal_alignment="center",
        padding=5,
    )

