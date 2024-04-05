import flet as ft
from flet_route import Params, Basket
import requests



def sign_up_finish(page: ft.Page, params:Params, basket:Basket):


    page.title = "Sign up finish"

    page.fonts = {
        "TravelingTypewriter": "fonts/ojuju.ttf"
    }

    email = ft.TextField(hint_text="Email Address..", width=300, height=50, border_radius=20)
    password1 = ft.TextField(hint_text="Password..", width=300, height=50, border_radius=20, password=True)
    password2 = ft.TextField(hint_text="Confirm Password..", width=300, height=50, border_radius=20, password=True)

    page.theme_mode = ft.ThemeMode.LIGHT

    def switch_theme_mode(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    

    

        
    def get_markets():
        req = requests.get("https://shopowner.app/api/markets/").json()

        markets = []
        for item in req["markets"]:
            print(item["id"], item["name"])
            page.session.set("%s" % item["name"], "%s" % item["id"])
            print(page.session.get("%s" % item["name"]))
            market = ft.dropdown.Option(item["name"])
            markets.append(market)

        return markets

    
    markets = get_markets()

    dd = ft.Dropdown(
                width=250,
                label="Market Category",
                hint_text="Select a Market Category",
                options=markets,
            )

    def handle_signup_finish(e):
        req = requests.post("https://shopowner.app/api/add/1/", data={"app_id":page.session.get("id"), "market":dd.value})
        print(dd.value)
        print(page.session.get("%s" % dd.value))
        page.go(f"/sign-up/close/%s" % str(page.session.get("%s" % dd.value)))
        page.update()

    
    return ft.View(
        "/sign-up/finish/",
        controls=[

            ft.AppBar(
                leading=ft.Icon(ft.icons.STYLE),
                title=ft.Text("Shop Owner"),
                bgcolor=ft.colors.TRANSPARENT,
            ),

            ft.SafeArea(ft.Switch(label="Dark Theme Mode", on_change=switch_theme_mode)),

            ft.Container(height=10),
            ft.Image(
                src="images/option.svg",
                width=200,
                height=200,
                fit=ft.ImageFit.CONTAIN,
            ),
            ft.Container(height=10),
            ft.Text("Choose Market Category", weight="bold", theme_style="titleLarge"),

            ft.Container(height=10),
            dd,
            ft.Container(height=5),
            ft.ElevatedButton("Save", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_signup_finish),
            ft.Container(height=10),

            


        ],

        scroll="always",
        vertical_alignment="center",
        horizontal_alignment="center",
        padding=5,
    )

