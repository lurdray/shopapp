import flet as ft
from flet_route import Params, Basket
import requests



def detail(page: ft.Page, params:Params, basket:Basket):

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

    
    def handle_shop(id):
        print("handling shop")
        shop = requests.get(f"https://shopowner.app/api/detail/%s" % (id)).json()
        return shop

    shop_id = page.route[8:]
    print(shop_id)
    shop = handle_shop(shop_id)

    back = ft.IconButton(
                icon=ft.icons.ARROW_BACK_IOS, on_click=lambda _: page.go("/dash")
            )


    return ft.View(
        "/detail/",
        controls=[

            ft.Container(
                    content=back,
                    alignment=ft.alignment.top_left,
                ),

            


            ft.Container(
                image_src="https://shopowner.app" + shop["logo"] + "/",
                image_fit="cover",
                height=150,
                border_radius=5,
                padding=0,
            ),
        


            ft.Container(height=1),  

            ft.Row(scroll="always", 
                controls=[
                    ft.Image(
                            src="https://shopowner.app" + shop["image1"] +"/",
                            width=55,
                            height=55,
                            fit=ft.ImageFit.CONTAIN,
                            border_radius=ft.border_radius.all(15),
                        ),

                    ft.Image(
                            src="https://shopowner.app" + shop["image2"] +"/",
                            width=55,
                            height=55,
                            fit=ft.ImageFit.CONTAIN,
                            border_radius=ft.border_radius.all(15),
                        ),   
                    ft.Image(
                            src="https://shopowner.app" + shop["image3"] +"/",
                            width=55,
                            height=55,
                            fit=ft.ImageFit.CONTAIN,
                            border_radius=ft.border_radius.all(15),
                        ),   

                    ft.Image(
                            src="https://shopowner.app" + shop["image4"] +"/",
                            width=55,
                            height=55,
                            fit=ft.ImageFit.CONTAIN,
                            border_radius=ft.border_radius.all(15),
                        ),    

                ]
            ),
            

            ft.Container(height=10),

            ft.Text(shop["name"], weight="bold", theme_style="titleLarge"),
            ft.Row(controls=[ft.Icon(ft.icons.STAR, color=ft.colors.YELLOW_600), ft.Icon(ft.icons.STAR, color=ft.colors.YELLOW_600), ft.Icon(ft.icons.STAR, color=ft.colors.YELLOW_600)], alignment="center", ),
            
            ft.Text(shop["description"], text_align="center", width=350),

            ft.Container(height=10),

            #ft.WebView(
            #    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3654.3406974350205!2d90.48469931445422!3d23.663771197998262!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3755b0d5983f048d%3A0x754f30c82bcad3cd!2sJalkuri%20Bus%20Stop!5e0!3m2!1sen!2sbd!4v1610539261654!5m2!1sen!2sbd",
            #    expand=True,
            #    on_page_started=lambda _: print("Page started"),
            #    on_page_ended=lambda _: print("Page ended"),
            #    on_web_resource_error=lambda e: print("Page error:", e.data),
            #    height=100
            #),


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
