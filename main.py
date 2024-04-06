import flet as ft
import requests

def main(page: ft.Page):
   page.title = "Shop Owner"
   page.theme_mode = ft.ThemeMode.LIGHT

   

   def route_change(route):
      page.views.clear()
      if page.route == "/":
            page.views.append(
                  ft.View(
                     "/",
                     [
                        ft.AppBar(
                              leading=ft.Icon(ft.icons.STYLE),
                              title=ft.Text("Shop Owner"),
                              bgcolor=ft.colors.AMBER_100,
                           ),

                           #ft.SafeArea(ft.Switch(label="Dark Theme Mode", on_change=switch_theme_mode)),

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
            )

      ######dash
      if page.route == "/dash":
         

         def service_card(item_id, image, text, text2, market, category):

            def handle_detail(e):
               page.session.set("shop_id", item_id)

               page.go("/detail")

            col1 = ft.Image(src=image, width=150, fit=ft.ImageFit.CONTAIN, border_radius=ft.border_radius.all(5))
            col2 = ft.Column([
                        ft.Text(text, size=16, weight=ft.FontWeight.BOLD),
                        ft.Text(text2, size=10, color="grey600"),
                        ft.TextButton(
                              market,
                              icon="SHOP",
                              icon_color="AMBER",
                              on_click=handle_detail
                        ),
                        ft.TextButton(
                              category,
                              icon="STOREFRONT",
                              icon_color="AMBER",
                              on_click=handle_detail
                        ),
                  
            ])

            #page.session.set("shop_id", item_id)
            
            service_card = ft.Card(
                  color="rgba(255, 255, 255, 1)",
                  elevation=5,
                  width=350,
                  
                  content=ft.Container(
                     padding=10,
                     alignment=ft.alignment.center,
                     ink=True,
                     on_click=handle_detail,
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
            try:
               shops = requests.get("https://shopowner.app/api/all/", headers=headers).json()["shops"]
            except:
               shops = []
            for item in shops:
                  item_id = item["id"]
                  image = "https://shopowner.app" + item["logo"] + "/"

                  #image = "https://shopowner.app/media/account_files/logos/Alaba-Rago-Market.jpg/"
                  #image = "https://dominuskelvin.dev/koo"
                  
                  name = item["name"][:15] + "..."
                  description = item["description"][:25] + "..."
                  market = item["market"]
                  category = item["category"]
                  items.append(
                     ft.Container(
                        content=ft.Row([service_card(item_id, image, name, description, market, category)], alignment="center"),
                        alignment=ft.alignment.center,
                        width=400,
                        border_radius=ft.border_radius.all(5),
                     )
                  )

            return items

         page.views.append(
            ft.View(
               "/dash",
               [
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
         )
      page.update()
      ################


      #####################
      if page.route == "/sign-up":
            email = ft.TextField(label="Email Address..", width=300, height=50, border_radius=15, prefix_icon=ft.icons.EMAIL)
            password1 = ft.TextField(label="Password..", width=300, height=50, border_radius=15, password=True, prefix_icon=ft.icons.PASSWORD)

            def handle_signup(e):
               
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

                  page.go("/sign-up-finish")
                  page.update()
               
            back = ft.IconButton(
               icon=ft.icons.ARROW_BACK_IOS, on_click=lambda _: page.go("/")
            )


            page.views.append(
                     ft.View(
                        "/sign-up",
                        [
                        ft.Container(
                           content=back,
                           alignment=ft.alignment.top_left,
                        ),

                        #ft.SafeArea(ft.Switch(label="Dark Theme Mode", on_change=switch_theme_mode)),

                        ft.Container(height=10),
                        ft.Image(
                           src="images/sign_up.svg",
                           width=150,
                           height=150,
                           fit=ft.ImageFit.CONTAIN,
                        ),
                        ft.Container(height=5),
                        ft.Text("Create an account", weight="bold", theme_style="titleLarge"),
                        ft.Text("Begin your journey to increasing online visibility.", text_align="center"),

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
            )
      page.update()

      #######################




      ########################
      if page.route == "/sign-up-finish":
            email = ft.TextField(hint_text="Email Address..", width=300, height=50, border_radius=15)
            password1 = ft.TextField(hint_text="Password..", width=300, height=50, border_radius=15, password=True)
            password2 = ft.TextField(hint_text="Confirm Password..", width=300, height=50, border_radius=15, password=True)

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
                        border_radius=15,
                        label="Market Category",
                        hint_text="Select a Market Category",
                        options=markets,
                        prefix_icon=ft.icons.FORMAT_LIST_BULLETED_OUTLINED,
                     )

            def handle_signup_finish(e):
               req = requests.post("https://shopowner.app/api/add/1/", data={"app_id":page.session.get("id"), "market":dd.value})
               print("the compiler is here.....")
               #print(page.session.get("%s" % dd.value))
               page.session.set("market_id", dd.value)
               page.go("/sign-up-close")
               #page.go(f"/sign-up-close/%s" % str(page.session.get("%s" % dd.value)))
               page.update()

            back = ft.IconButton(
               icon=ft.icons.ARROW_BACK_IOS, on_click=lambda _: page.go("/sign-up")
            )

            page.views.append(
               ft.View(
                  "/sign-up-finish",
                  [
                        ft.Container(
                           content=back,
                           alignment=ft.alignment.top_left,
                        ),

                        #ft.SafeArea(ft.Switch(label="Dark Theme Mode", on_change=switch_theme_mode)),

                        ft.Container(height=10),
                        ft.Image(
                           src="images/option.svg",
                           width=200,
                           height=200,
                           fit=ft.ImageFit.CONTAIN,
                        ),
                        ft.Container(height=10),
                        ft.Text("Choose Market Category", weight="bold", theme_style="titleLarge"),
                        ft.Text("Help customer find you easily on Shop Owner.", text_align="center"),

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
            )
      page.update()
      ################


      #####################
      if page.route == "/sign-up-close":
         def handle_signup_close(e):
            req = requests.post("https://shopowner.app/api/add/2/", data={"app_id":page.session.get("id"), "categoey":cat.value})
            page.go("/add-shop")
            page.update()

            
         def get_categorys(market_id):
            req = requests.get("https://shopowner.app/api/categorys/%s/" % market_id).json()

            categorys = []
            for item in req["categorys"]:
                  category = ft.dropdown.Option(item["name"])
                  categorys.append(category)

            return categorys

         

         market = page.session.get("market_id")
         market_id = page.session.get("%s" % market)
         print("This market id is %s" % market_id)
         #market_id = page.route[15:]
         categorys = get_categorys(market_id)
                     

         cat = ft.Dropdown(
                     width=250,
                     label="Sub Category",
                     hint_text="Select a Market Sub Category",
                     options=categorys,
                     prefix_icon=ft.icons.FORMAT_LIST_BULLETED_OUTLINED,
                  )

         back = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS, on_click=lambda _: page.go("/sign-up-finish")
         )
         
         page.views.append(
            ft.View(
               "/sign-up-close",
               [
                     ft.Container(
                           content=back,
                           alignment=ft.alignment.top_left,
                        ),

                     #ft.SafeArea(ft.Switch(label="Dark Theme Mode", on_change=switch_theme_mode)),

                     ft.Container(height=10),
                     ft.Image(
                        src="images/option.svg",
                        width=200,
                        height=200,
                        fit=ft.ImageFit.CONTAIN,
                     ),
                     ft.Container(height=10),
                     ft.Text("Choose Sub Category", weight="bold", theme_style="titleLarge"),
                     ft.Text("Maintaining a niche of your own and remain unique.", text_align="center"),

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
         )
      page.update()
      #####################
         
      #####################
      if page.route == "/add-shop":
         name = ft.TextField(label="Business Name", width=300, height=50, border_radius=15, prefix_icon=ft.icons.BUSINESS_CENTER)
         description = ft.TextField(
                  label="About your Business",
                  multiline=True,
                  min_lines=1,
                  max_lines=3,
                  width=300, border_radius=15,
                  prefix_icon=ft.icons.DESCRIPTION,
            )
         phone = ft.TextField(label="Phone Number", width=300, height=50, border_radius=15, prefix_icon=ft.icons.LOCAL_PHONE)
         map_link = ft.TextField(
                  label="Google map link",
                  multiline=True,
                  min_lines=1,
                  max_lines=3,
                  width=300, border_radius=15, 
                  prefix_icon=ft.icons.LOCATION_ON
            )

         def on_dialog_result(e: ft.FilePickerResultEvent):
            print("Selected files:", e.files)
            print("Selected file or directory:", e.path)

         file_picker = ft.FilePicker(on_result=on_dialog_result)
         page.overlay.append(file_picker)



         def handle_add_shop(e):
            req = requests.post("https://shopowner.app/api/add/2/", data={"app_id":page.session.get("id"), "categoey":cat.value})
            page.go("/dash")
            page.update()


         back = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS, on_click=lambda _: page.go("/sign-up-close")
         )

         page.views.append(
               ft.View(
                  "/add-shop",
                  [
                     ft.Container(
                           content=back,
                           alignment=ft.alignment.top_left,
                        ),
                        
                     ft.Text("Register your Shop", weight="bold", theme_style="titleLarge"),
                     ft.Text("Get listed on Shop Owner for more online visibility for your Shop.", text_align="center"),

                     ft.Container(height=5),
                     name, 
                     ft.Container(height=5),
                     description,
                     ft.Container(height=5),
                     phone,
                     ft.Container(height=5),
                     map_link,
                     ft.Container(height=5),
                     ft.Row([
                           ft.ElevatedButton("Upload Logo", on_click=lambda _: file_picker.pick_files()), 
                           ft.ElevatedButton("Upload Images", on_click=lambda _: file_picker.pick_files())
                        ], alignment="center"),
                     
                     ft.Container(height=5),
                     ft.ElevatedButton("Save", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_add_shop),
                     
                     ft.Container(height=10),
                  ],

                  scroll="always",
                  vertical_alignment="center",
                  horizontal_alignment="center",
                  padding=5,
               )
         )
      page.update()
      #####################






      #####################
      if page.route == "/manage-shop":
         name = ft.TextField(label="Edit Name", width=300, height=50, border_radius=15, prefix_icon=ft.icons.BUSINESS_CENTER)
         description = ft.TextField(
                  label="Edit About Business",
                  multiline=True,
                  min_lines=1,
                  max_lines=3,
                  width=300, border_radius=15,
                  prefix_icon=ft.icons.DESCRIPTION,
            )
         phone = ft.TextField(label="Phone Number", width=300, height=50, border_radius=15, prefix_icon=ft.icons.LOCAL_PHONE)
         map_link = ft.TextField(
                  label="Edit Google map link",
                  multiline=True,
                  min_lines=1,
                  max_lines=3,
                  width=300, border_radius=15, 
                  prefix_icon=ft.icons.LOCATION_ON
            )

         def on_dialog_result(e: ft.FilePickerResultEvent):
            print("Selected files:", e.files)
            print("Selected file or directory:", e.path)

         file_picker = ft.FilePicker(on_result=on_dialog_result)
         page.overlay.append(file_picker)



         def handle_add_shop(e):
            req = requests.post("https://shopowner.app/api/add/2/", data={"app_id":page.session.get("id"), "categoey":cat.value})
            page.go("/dash")
            page.update()


         back = ft.IconButton(
            icon=ft.icons.ARROW_BACK_IOS, on_click=lambda _: page.go("/dash")
         )

         page.views.append(
               ft.View(
                  "/manage-my-shop",
                  [
                     ft.Container(
                           content=back,
                           alignment=ft.alignment.top_left,
                        ),
                     ft.Text("Manage my Shop", weight="bold", theme_style="titleLarge"),
                     ft.Container(height=5),
                     name, 
                     ft.Container(height=5),
                     description,
                     ft.Container(height=5),
                     phone,
                     ft.Container(height=5),
                     map_link,
                     ft.Container(height=5),
                     ft.Row([
                           ft.ElevatedButton("Upload Logo", on_click=lambda _: file_picker.pick_files()), 
                           ft.ElevatedButton("Upload Images", on_click=lambda _: file_picker.pick_files())
                        ], alignment="center"),
                     
                     ft.Container(height=5),
                     ft.ElevatedButton("Save", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_add_shop),
                     
                     ft.Container(height=10),
                  ],

                  scroll="always",
                  vertical_alignment="center",
                  horizontal_alignment="center",
                  padding=5,
               )
         )
      page.update()
      #####################





      ##############################
      if page.route == "/detail":

         def bs_dismissed(e):
            print("Dismissed!")

         def show_bs(e):
            bs.open = True
            bs.update()

         def close_bs(e):
            bs.open = False
            bs.update()

         def handle_show_bs(e):
            show_bs(e)

         def handle_shop(id):
            print("handling shop")
            shop = requests.get(f"https://shopowner.app/api/detail/%s" % (id)).json()
            print(shop)
            return shop

         shop_id = page.session.get("shop_id")

         #shop_id = page.route[8:]
         shop = handle_shop(shop_id)

         def launch_direction(e):
            #page.launch_url(shop["google_map"])
            page.launch_url("https://wa.me/+23490875678")

         bs = ft.BottomSheet(
            ft.Container(
               content=ft.Column(
                  [  
                     ft.Container(height=25),  
                     ft.Text("Get Directions.", weight="bold", theme_style="titleLarge"),
                     ft.Text("Easily locate your way to this Shop by clicking.", text_align="center"),
                     ft.Container(height=5),  
                     ft.ElevatedButton("Get Direction", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=launch_direction),
                     
                  ], 
               
               ),
               padding=10,
            ),

            
            on_dismiss=bs_dismissed,
         )

         page.overlay.append(bs)

         back = ft.IconButton(
                     icon=ft.icons.ARROW_BACK_IOS, on_click=lambda _: page.go("/dash")
                  )
         page.views.append(
            ft.View(
               "/detail",
               [
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
                     ft.Container(height=1),
                     ft.ElevatedButton("Get Direction", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_show_bs),

                     ft.Container(height=10),

                     #ft.WebView(
                     #    "https://www.instantstreetview.com/@9.149066,7.319175,289.87h,5p,1z,bJEGfLcnpKuV1fI1gFv4kw",
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
         )
      page.update()
      ##############################



      
















   def view_pop(view):
      page.views.pop()
      top_view = page.views[-1]
      page.go(top_view.route)

   page.on_route_change = route_change
   page.on_view_pop = view_pop
   page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
