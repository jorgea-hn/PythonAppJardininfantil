import flet as ft

def main(page: ft.Page):

    page.window_maximized=True
    page.window_center()
    page.window_resizable=True
    page.window_maximizable=True
    page.window_minimizable=False

    page.padding=0
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.title = "JARDIN HAPPY FACE"


    colores=("#D5EAF8","#FC2D2B","#A3B1BB")
    #0(azul claro), 1(rojo), 2(gris)   
    
#-----------------Funciones--------------------------------
    def validacion(usuario,Contraseña):
        if usuario.value=="admin" and Contraseña.value=="admin1234":
            print("si funciona")
            page.go("/principal")
        
        else:
            print("no valido")


    #------------- PAGINA PRINCIPAL -------------
    
    #-----------------Contenido-------------------
            
    imagen = ft.Container(
            
            content = ft.Image(src="img/logo.png",width=450,height=500,expand=True),
            # border=ft.border.all(3,"red"),
            # bgcolor=ft.colors.BLACK,
            alignment=ft.alignment.center,
            expand=True,
            width=500
            
            
        )
    usuario=ft.TextField(
                        label="Usuario",width=380,bgcolor="White",border_color="transparent"
                    )
    
    Contraseña= ft.TextField(
                        label="Contraseña",width=380,password=True,can_reveal_password=True,bgcolor="White",border_color="transparent"
                    )
    user = ft.Container(
            alignment=ft.alignment.center,
            width=450,
            height=550,
            border_radius=30,
            bgcolor=colores[0],
            padding=20,
            margin=20,
            content = ft.Column(

                controls=[
                    
                    ft.Text(
                        "SING IN",width=380,text_align=ft.TextAlign.CENTER,size=30,weight=ft.FontWeight.BOLD,color=colores[1]
                        ),
                    
                    ft.Container(width=20,height=40),

                    usuario,

                    ft.Container(width=20,height=20),

                    Contraseña,

                    ft.Container(width=20,height=40),

                    ft.ElevatedButton(
                        "LOGIN",height=50,width=380,bgcolor=colores[1],color="White",

                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=0)
                        ),
                        on_click=lambda _: validacion(usuario,Contraseña)#page.go("/")
                        ),
                    

                ]
            )            
        )
    
    

    login = ft.Container(

        margin=50,

        content=ft.Row(

            
            controls=[imagen,user]),
        
        
    )       
    
# ---------------Enrutado-----------------
    
    def route_change(route):
        vista1=ft.View(
                "/",
                [
                    login
                ],
            )
        page.views.clear()
        page.views.append(  vista1          
            
        )
        if page.route == "/principal":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/principal",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),ft.Image(src="../img/logo.png",width=100,height=100)
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change= route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    

ft.app(target=main) # para visualizar en escritorio

# ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550) # para visualizar en navegador



