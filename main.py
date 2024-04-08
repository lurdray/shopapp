import flet as ft
import requests

def main(page: ft.Page):
   page.title = "Shop owner"
   page.theme_mode = ft.ThemeMode.LIGHT
   page.window_width = 350        # window's width is 200 px
   page.window_height = 650       # window's height is 200 px
   page.window_resizable = False  # window is not resizable
   page.update()

   def launch_help(e):
      #page.launch_url(shop["google_map"])
      page.launch_url("https://wa.me/+2348148737265")

   def changetab(e):
      index = e.control.selected_index
      print(" ")
      print(" ")
      print(" ")
      print("-----⏳")
      print("-----⏳")
      print("-----⏳")
      print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
      print("-----🤯----- The menue index is (%s) ....." % index)
      if index == 0:
         page.go("/dash")
      
      elif index == 1:
         if page.session.get("id"):
            page.go("/manage-my-shop")
         else:
            notify("You're not signed in")
            page.go("/sign-up")

      elif index == 2:
         launch_help(e)

      elif index == 3:
         page.go("/")
      
      else:
         pass


   def notify(msg):
      
      dlg = ft.AlertDialog(
         title=ft.Row(
            [
               ft.Icon(name=ft.icons.INFO, color=ft.colors.AMBER_500),
               ft.Text(msg, size="13", text_align="center"),
            ]
      )
      )
      page.dialog = dlg
      dlg.open = True
      page.update()

   

   def route_change(route):
      page.views.clear()
      if page.route == "/":
            page.views.append(
                  ft.View(
                     "/",
                     [
                        ft.AppBar(
                              leading=ft.Icon(ft.icons.STORE),
                       
                              bgcolor=ft.colors.AMBER,
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

                           ft.Text("Discover Shops Near You.", weight="bold", theme_style="titleLarge", color=ft.colors.GREY_700),
                           ft.Text("Explore recommended Shops that are in close prximity to you.", text_align="center", color=ft.colors.GREY),

                           ft.Container(height=5),
                           ft.ElevatedButton("I'm a buyer", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=lambda _: page.go("/dash")),
                           ft.Container(height=2),
                           ft.ElevatedButton("I'm' a shop owner", bgcolor=ft.colors.GREY_800, color="#FFC100", width="200", height="50", on_click=lambda _: page.go("/sign-up")),
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
         

         def service_card(item_id, image, image_type, text, text2, market, category):

            def handle_detail(e):
               page.session.set("shop_id", item_id)
               page.go("/detail")

            if image_type == "64":
               col1 = ft.Image(src_base64=image, width=150, fit=ft.ImageFit.CONTAIN, border_radius=ft.border_radius.all(5))
            
            else:
               col1 = ft.Image(src=image, width=150, fit=ft.ImageFit.CONTAIN, border_radius=ft.border_radius.all(5))

            col2 = ft.Column([
                        ft.Container(height=8),
                        ft.Text(text, size=16, weight=ft.FontWeight.BOLD, color="grey800"),
                        ft.Text(text2, size=11, color="grey600"),
                        ft.Row(
                              [
                                 ft.Icon(name=ft.icons.STOREFRONT_OUTLINED, color=ft.colors.AMBER_500),
                                 ft.Text(market, size=11, color="grey600"),
                              ]
                        ),
                        ft.Row(
                              [
                                 ft.Icon(name=ft.icons.SUBJECT, color=ft.colors.AMBER),
                                 ft.Text(category, size=11, color="grey600"),
                              ]
                        ),
                  
                  ])

            #page.session.set("shop_id", item_id)
            
            service_card = ft.Card(
                  color="AMBER50",
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
                  if item["logo_64"] == "None":
                     image = "https://shopowner.app" + item["logo"] + "/"
                     image_type = "not_64"
                  else:
                     image = item["logo_64"]
                     image_type = "64"

                  #image = "https://shopowner.app/media/account_files/logos/Alaba-Rago-Market.jpg/"
                  #image = "https://dominuskelvin.dev/koo"
                  
                  name = item["name"][:15] + "..."
                  description = item["description"][:25] + "..."
                  market = item["market"]
                  category = item["category"]
                  items.append(
                     ft.Container(
                        content=ft.Row([service_card(item_id, image, image_type, name, description, market, category)], alignment="center"),
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
                        leading=ft.Icon(ft.icons.STORE),
                        
                        bgcolor=ft.colors.AMBER,
                     ),

                     ft.Container(height=1),
                     ft.Row(
                              [
                                 ft.Icon(name=ft.icons.ARROW_DROP_DOWN_CIRCLE, color=ft.colors.AMBER),
                                 ft.Text("All shops", size=18, color="grey600"),
                                 ft.Text("                                         "),
                                 ft.Icon(name=ft.icons.MORE_VERT)
                              ]
                        ),
                     ft.Container(height=1),
                     ft.Column(spacing=0, controls=items()),

                     #ft.ElevatedButton("Get Started", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=lambda _: page.go("/sign-up")),
                     ft.Container(height=10),

                     ft.NavigationBar(
                        bgcolor=ft.colors.AMBER,
                        selected_index = 0,
                        on_change=changetab,
                        destinations=[
                           ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                           ft.NavigationDestination(icon=ft.icons.BUSINESS_CENTER, label="My Business"),
                           ft.NavigationDestination(icon=ft.icons.HELP, label="Help"), 
                           ft.NavigationDestination(icon=ft.icons.LOGOUT, label="Logout"), 
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
      if page.route == "/sign-in":
            emaill = ft.TextField(label="Email Address..", width=300, height=50, border_radius=15, prefix_icon=ft.icons.EMAIL)
            passwordd = ft.TextField(label="Password..", width=300, height=50, border_radius=15, password=True, prefix_icon=ft.icons.PASSWORD)

            def handle_signin(e):
               
               emaill.error_text = ""
               passwordd.error_text = ""
               if not emaill.value:
                  emaill.error_text = "missing email..."
                  page.update()
               elif not passwordd.value:
                  passwordd.error_text = "missing password..."
                  page.update()

               else:
                  #import json
                  headers = {"Content-Type": "application/json; charset=utf-8"}
                  try:
                     req = requests.get(url="https://shopowner.app/api/sign-in/%s/%s/" % (emaill.value, passwordd.value)).json()
                  except:
                     notify("Invalid login!")
                  if req["status"] == True:
                     print(" ")
                     print(" ")
                     print(" ")
                     print("-----⏳")
                     print("-----⏳")
                     print("-----⏳")
                     print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
                     print("-----🤯----- The sign in request response is: %s ....." % req)
                     page.session.set("id", req["id"])

                     page.go("/dash")
                     page.update()

                  else:
                     notify("Invalid login!")
                  
               
            back = ft.IconButton(
               icon=ft.icons.ARROW_BACK_IOS, on_click=lambda _: page.go("/")
            )


            page.views.append(
                     ft.View(
                        "/sign-in",
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
                        ft.Text("Sign in", weight="bold", theme_style="titleLarge"),
                        ft.Text("Help customers find you easily.", text_align="center"),

                        ft.Container(height=5),
                        emaill,
                        passwordd,

                        ft.Container(height=5),
                        ft.ElevatedButton("Sign In", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_signin),
                        ft.TextButton(
                           "I don't have an account.",
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
            )
      page.update()

      #######################


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
                  
                  if req != "Email Address already taken!":
                     pass
                  else:
                     notify("Email Address already taken!")
                  #req = json.loads(req)
                  #print(req)
                  
                  #print(req["status"])
                  #if req:
                  #     ft.AlertDialog(
                  #        title=ft.Text("Hey there!"), on_dismiss=lambda e: print("Close")
                  #    )
                        
                  #else:
                  print(" ")
                  print(" ")
                  print(" ")
                  print("-----⏳")
                  print("-----⏳")
                  print("-----⏳")
                  print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
                  print("-----🤯----- The sign in request response is: %s ....." % req)
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
                        ft.Text("Create an account", weight="bold", theme_style="titleLarge", color=ft.colors.GREY_700),
                        ft.Text("Begin your journey to increasing online visibility.", text_align="center", color=ft.colors.GREY),

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
                     page.session.set("%s" % item["name"], "%s" % item["id"])
                     print(" ")
                     print(" ")
                     print(" ")
                     print("-----⏳")
                     print("-----⏳")
                     print("-----⏳")
                     print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
                     print("-----🤯----- Market and Category saved: %s ....." % page.session.get("%s" % item["name"]))
                     
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
               dd.error_text = ""
               if not dd.value:
                  dd.error_text = "Select one"
                  page.update()
               
               else:
                  req = requests.post("https://shopowner.app/api/add/1/", data={"app_id":page.session.get("id"), "market":dd.value})
                  print(" ")
                  print(" ")
                  print(" ")
                  print("-----⏳")
                  print("-----⏳")
                  print("-----⏳")
                  print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
                  print("-----🤯----- The compiler got to handle_signup_finish .....")
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
                        ft.Text("Choose Market Category", weight="bold", theme_style="titleLarge", color=ft.colors.GREY_700),
                        ft.Text("Help customer find you easily on Shop Owner.", text_align="center", color=ft.colors.GREY),

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
            if not cat.value:
               cat.error_text = "Select one"
               page.update()
            
            else:
               req = requests.post("https://shopowner.app/api/add/2/", data={"app_id":page.session.get("id"), "category":cat.value})
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
         print(" ")
         print(" ")
         print(" ")
         print("-----⏳")
         print("-----⏳")
         print("-----⏳")
         print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
         print("-----🤯----- Saved marketing id to session (%s) ....." % market_id)
         
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
                     ft.Text("Choose Sub Category", weight="bold", theme_style="titleLarge", color=ft.colors.GREY_700),
                     ft.Text("Maintaining a niche of your own and remain unique.", text_align="center", color=ft.colors.GREY),

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
                  label="Shop Address",
                  multiline=True,
                  min_lines=1,
                  max_lines=3,
                  width=300, border_radius=15, 
                  prefix_icon=ft.icons.LOCATION_ON
            )

         def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files = e.files
            #print(selected_files[0])
            #selected_files = (
            #      ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
            #)
            print(" ")
            print(" ")
            print(" ")
            print("-----⏳")
            print("-----⏳")
            print("-----⏳")
            print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
            print("-----🤯----- The selected_files path is: %s " % selected_files)

            page.session.set("selected_files", selected_files)

         file_picker = ft.FilePicker(on_result=pick_files_result)
         page.overlay.append(file_picker)

         #####multiple files
         def pick_files_result2(e: ft.FilePickerResultEvent):
            selected_files2 = e.files
            print("-----🤯----- The selected_files path is: %s " % selected_files2)

            page.session.set("selected_files2", selected_files2)

         file_picker2 = ft.FilePicker(on_result=pick_files_result2)
         page.overlay.append(file_picker2)




         def handle_add_shop(e):
            selected_files = page.session.get("selected_files")
            selected_files2 = page.session.get("selected_files2")

            print("Printing the other images:", selected_files2)

            name.error_text = ""
            description.error_text = ""
            phone.error_text = ""
            map_link.error_text = ""
            if not name.value:
               name.error_text = "missing email..."
               page.update()
            elif not description.value:
               description.error_text = "missing password..."
               page.update()
            elif not phone.value:
               phone.error_text = "missing password..."
               page.update()
            elif not map_link.value:
               map_link.error_text = "missing password..."
               page.update()

            else:

               ###new code
               try:
                  import base64
                  with open(selected_files[0].path, 'rb') as file:
                     logo_file = base64.b64encode(file.read()).decode("utf-8")
               except:
                  logo_file = None

               other_images = []
               for item in selected_files2:
                  with open(item.path, 'rb') as file:
                     item_file = base64.b64encode(file.read()).decode("utf-8")
                     other_images.append(item_file)

               try:
                  other_images[0]
               except:
                  other_images[0] = None

               try:
                  other_images[1]
               except:
                  other_images[1] = None

               try:
                  other_images[2]
               except:
                  other_images.append(None)
               
               try:
                  other_images[3]
               except:
                  other_images.append(None)

               try:
                  other_images[4]
               except:
                  other_images.append(None)

               print(other_images)
            
               import urllib.request
               import urllib.parse
               import json

               

               data = {'logo_64': logo_file, 'image1_64': other_images[0], 'image2_64': other_images[1], 
                       'image3_64': other_images[2], 'image4_64': other_images[3], "app_id":page.session.get("id"), "name":name.value, 
                       "description":description.value, "phone":phone.value, "map_link":map_link.value
                       }
               
               encoded_data = urllib.parse.urlencode(data).encode('utf-8')
               request = urllib.request.Request("https://shopowner.app/api/add-shop/post/", data=encoded_data)
               
               print(" ")
               print(" ")
               print(" ")
               print("-----⏳")
               print("-----⏳")
               print("-----⏳")
               print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
               print("-----🤯----- The handle_add_shop request reponse is (%s) ....." % request)

               with urllib.request.urlopen(request) as response:
                  if response.getcode() == 200:
                     req = "Success!"
                     response_data = response.read()
                     json_response = json.loads(response_data)
                     print("JSON Response:", json_response)

                  else:
                     req = None

               ###end of new code

               if req == "Success!":
                  page.go("/dash")
                  page.update()

               else:
                  notify("An error occurred.")


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
                        
                     ft.Text("Register your Shop", weight="bold", theme_style="titleLarge", color=ft.colors.GREY_700),
                     ft.Text("Get listed on Shop Owner for more online visibility for your Shop.", text_align="center", color=ft.colors.GREY),

                     ft.Container(height=5),
                     name, 
                     ft.Container(height=5),
                     description,
                     ft.Container(height=5),
                     phone,
                     ft.Container(height=5),
                     map_link,
                     ft.Container(height=5),
                     ft.Text("Upload a logo and few(4) images for your product/service/shop.", text_align="center", color=ft.colors.GREY_700, size="9"),
                     ft.Row([
                           ft.ElevatedButton("Logo", on_click=lambda _: file_picker.pick_files()), 
                           ft.ElevatedButton("Images", on_click=lambda _: file_picker2.pick_files(allow_multiple=True))
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
      #####################
      if page.route == "/manage-my-shop":
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
                  label="Shop Address",
                  multiline=True,
                  min_lines=1,
                  max_lines=3,
                  width=300, border_radius=15, 
                  prefix_icon=ft.icons.LOCATION_ON
            )
         
         def handle_shop(id):
            print("handling shop")
            shop = requests.get(f"https://shopowner.app/api/detail/%s" % (id)).json()
            print(shop)
            return shop

         shop_id = page.session.get("id")

         #shop_id = page.route[8:]
         shop = handle_shop(shop_id)
         
         name.value = shop["name"]
         description.value = shop["description"]
         phone.value = shop["phone"]
         map_link.value = shop["google_map"]

         def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files = e.files
            #print(selected_files[0])
            #selected_files = (
            #      ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
            #)
            print(" ")
            print(" ")
            print(" ")
            print("-----⏳")
            print("-----⏳")
            print("-----⏳")
            print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
            print("-----🤯----- The selected_files path is: %s " % selected_files)

            page.session.set("selected_files", selected_files)

         file_picker = ft.FilePicker(on_result=pick_files_result)
         page.overlay.append(file_picker)

         #####multiple files
         def pick_files_result2(e: ft.FilePickerResultEvent):
            selected_files2 = e.files
            print("-----🤯----- The selected_files path is: %s " % selected_files2)

            page.session.set("selected_files2", selected_files2)

         file_picker2 = ft.FilePicker(on_result=pick_files_result2)
         page.overlay.append(file_picker2)




         def handle_manage_shop(e):
            selected_files = page.session.get("selected_files")
            selected_files2 = page.session.get("selected_files2")

            print("Printing the other images:", selected_files2)

            name.error_text = ""
            description.error_text = ""
            phone.error_text = ""
            map_link.error_text = ""
            if not name.value:
               name.error_text = "missing email..."
               page.update()
            elif not description.value:
               description.error_text = "missing password..."
               page.update()
            elif not phone.value:
               phone.error_text = "missing password..."
               page.update()
            elif not map_link.value:
               map_link.error_text = "missing password..."
               page.update()

            else:

               ###new code
               try:
                  import base64
                  with open(selected_files[0].path, 'rb') as file:
                     logo_file = base64.b64encode(file.read()).decode("utf-8")
               except:
                  logo_file = None

               other_images = []
               for item in selected_files2:
                  with open(item.path, 'rb') as file:
                     item_file = base64.b64encode(file.read()).decode("utf-8")
                     other_images.append(item_file)

               try:
                  other_images[0]
               except:
                  other_images[0] = None

               try:
                  other_images[1]
               except:
                  other_images[1] = None

               try:
                  other_images[2]
               except:
                  other_images.append(None)
               
               try:
                  other_images[3]
               except:
                  other_images.append(None)

               try:
                  other_images[4]
               except:
                  other_images.append(None)

               print(other_images)
            
               import urllib.request
               import urllib.parse
               import json

               

               data = {'logo_64': logo_file, 'image1_64': other_images[0], 'image2_64': other_images[1], 
                       'image3_64': other_images[2], 'image4_64': other_images[3], "app_id":page.session.get("id"), "name":name.value, 
                       "description":description.value, "phone":phone.value, "map_link":map_link.value
                       }
               
               encoded_data = urllib.parse.urlencode(data).encode('utf-8')
               request = urllib.request.Request("https://shopowner.app/api/add-shop/post/", data=encoded_data)
               
               print(" ")
               print(" ")
               print(" ")
               print("-----⏳")
               print("-----⏳")
               print("-----⏳")
               print("-----😃----- ✅✅✅✅✅✅✅✅✅✅✅✅ .....")
               print("-----🤯----- The handle_add_shop request reponse is (%s) ....." % request)

               with urllib.request.urlopen(request) as response:
                  if response.getcode() == 200:
                     req = "Success!"
                     response_data = response.read()
                     json_response = json.loads(response_data)
                     print("JSON Response:", json_response)

                  else:
                     req = None

               ###end of new code

               if req == "Success!":
                  page.go("/dash")
                  page.update()

               else:
                  notify("An error occurred.")


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
                        
                     ft.Text("Edit your Shop", weight="bold", theme_style="titleLarge", color=ft.colors.GREY_700),
                     ft.Text("Make changes to your account.", text_align="center", color=ft.colors.GREY),

                     ft.Container(height=5),
                     name, 
                     ft.Container(height=5),
                     description,
                     ft.Container(height=5),
                     phone,
                     ft.Container(height=5),
                     map_link,
                     ft.Container(height=5),
                     ft.Text("(Optional) Upload a logo or Images.", text_align="center", color=ft.colors.GREY_700, size="9"),
                     ft.Row([
                           ft.ElevatedButton("Logo", on_click=lambda _: file_picker.pick_files()), 
                           ft.ElevatedButton("Images", on_click=lambda _: file_picker2.pick_files(allow_multiple=True))
                        ], alignment="center"),
                     
                     ft.Container(height=5),
                     ft.ElevatedButton("Update", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=handle_manage_shop),
                     
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
            page.launch_url(shop["locator"])

         bs = ft.BottomSheet(
            ft.Container(
               content=ft.Column(
                  [  
                     ft.Container(height=25),  
                     ft.Row(
                              [  
                                 ft.Text("Location", weight="bold", theme_style="titleLarge", color=ft.colors.GREY_700),
                                 ft.Icon(name=ft.icons.LOCATION_ON, color=ft.colors.AMBER_500),
                                 
                              ]
                        ),
                     
                     ft.Text(shop["google_map"], text_align="center", color=ft.colors.GREY),
                     ft.Container(height=5),  
                     ft.ElevatedButton("Launch Map", bgcolor="#FFC100", color="#161515", width="200", height="50", on_click=launch_direction),
                     
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
         
         if shop["logo_64"] == "None":
            header = ft.Container(
                        image_src="https://shopowner.app" + shop["logo"] + "/",
                        image_fit="cover",
                        height=150,
                        border_radius=5,
                        padding=0,
                     )
            image_controls = [
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

            
         else:
            header = ft.Container(
                        image_src_base64=shop["logo_64"],
                        image_fit="cover",
                        height=150,
                        border_radius=5,
                        padding=0,
                     )
         
            image_controls = [
                           ft.Image(
                                    src_base64=shop["image1_64"],
                                    width=55,
                                    height=55,
                                    fit=ft.ImageFit.CONTAIN,
                                    border_radius=ft.border_radius.all(15),
                                 ),

                           ft.Image(
                                    src_base64=shop["image2_64"],
                                    width=55,
                                    height=55,
                                    fit=ft.ImageFit.CONTAIN,
                                    border_radius=ft.border_radius.all(15),
                                 ),   
                           ft.Image(
                                    src_base64=shop["image3_64"],
                                    width=55,
                                    height=55,
                                    fit=ft.ImageFit.CONTAIN,
                                    border_radius=ft.border_radius.all(15),
                                 ),   

                           ft.Image(
                                    src_base64=shop["image4_64"],
                                    width=55,
                                    height=55,
                                    fit=ft.ImageFit.CONTAIN,
                                    border_radius=ft.border_radius.all(15),
                                 ),    

            ]
            
         page.views.append(
            ft.View(
               "/detail",
               [
                     ft.Container(
                           content=back,
                           alignment=ft.alignment.top_left,
                        ),

                     


                     header,
               


                     ft.Container(height=1),  

                     ft.Row(scroll="always", 
                        controls=image_controls
                     ),
                     

                     ft.Container(height=10),

                     ft.Text(shop["name"], weight="bold", theme_style="titleLarge", color=ft.colors.GREY_700),
                     ft.Row(controls=[ft.Icon(ft.icons.STAR, color=ft.colors.YELLOW_600), ft.Icon(ft.icons.STAR, color=ft.colors.YELLOW_600), ft.Icon(ft.icons.STAR, color=ft.colors.YELLOW_600)], alignment="center", ),
                     
                     ft.Text(shop["description"], text_align="center", width=350, color=ft.colors.GREY),
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
                        selected_index = 0,
                        on_change=changetab,
                        destinations=[
                           ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                           ft.NavigationDestination(icon=ft.icons.BUSINESS_CENTER, label="My Business"),
                           ft.NavigationDestination(icon=ft.icons.HELP, label="Help"), 
                           ft.NavigationDestination(icon=ft.icons.LOGOUT, label="Logout"), 
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
