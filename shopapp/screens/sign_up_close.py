import flet as ft
from flet_route import Params, Basket
import requests



def sign_up_close(page: ft.Page, params:Params, basket:Basket):


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

    
    print("finally got here....")

    def handle_signup_close(e):
            req = requests.post("https://shopowner.app/api/add/2/", data={"app_id":page.session.get("id"), "categoey":cat.value})
            page.go("/dash")
            page.update()

        
    def get_categorys(market_id):
        req = requests.get("https://shopowner.app/api/categorys/%s/" % market_id).json()

        categorys = []
        for item in req["categorys"]:
            category = ft.dropdown.Option(item["name"])
            categorys.append(category)

        return categorys

    
    market_id = page.route[15:]
    print(market_id)
    print("yayyyyyyy")
    categorys = get_categorys(market_id)
                

    cat = ft.Dropdown(
                width=250,
                label="Sub Category",
                hint_text="Select a Market Sub Category",
                options=categorys,
            )
    return ft.View(
        "/sign-up/close/",
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
            ft.Text("Choose Sub Category", weight="bold", theme_style="titleLarge"),

            ft.Container(height=10),
            cat, 

            ft.Container(height=5),
            ft.ElevatedButton("Save", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_signup_close),
            ft.Container(height=10),

            


        ],

        scroll="always",
        vertical_alignment="center",
        horizontal_alignment="center",
        padding=5,
    )

