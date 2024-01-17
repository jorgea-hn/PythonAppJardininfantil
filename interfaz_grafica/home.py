import flet as ft
# apertura del programa 
def main(page: ft.Page):

    page.window_width=1366+15
    page.window_height=768-25

    page.window_center()
    page.window_resizable=False
    page.window_maximizable=False
    page.window_minimizable=True
    

    page.padding=0
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.title = "JARDIN HAPPY FACE"


    

    colores=("#D5EAF8","#FC2D2B","#A3A3A3","#D9D9D9")
    #0(azul claro), 1(rojo), 2(gris),3(gris claro)   
    
#-----------------Funciones--------------------------------
    def validacion(usuario,Contraseña):
        if usuario.value=="" and Contraseña.value=="":
            print("si funciona")
            page.go("/principal")

            
        else:
            print("no valido")

    
    def llamar_datos_matricula(self):

        # estudiante=[nombre_estudiante.value,fecha_nacimiento.value,edad.value,documento.value,tipo_documento.value,grado.value,tipo_sangre.value,alergia.value,eps.value,numero_emergencia.value]
        # padre=[nombre_padre.value,profesion_padre.value,cedula_padre.value,direccion_padre.value]
        # madre=[nombre_madre.value,profesion_madre.value,cedula_madre.value,direccion_madre.value]
        # acudiente=[nombre_acudiente.value,profesion_acudiente.value,cedula_acudiente.value,direccion_acudiente.value]
        
        # matricula_value=[estudiante,padre,madre,acudiente]
        # matriculados.append(matricula_value)


        estudiante=[nombre_estudiante,fecha_nacimiento,edad,documento,tipo_documento,grado,tipo_sangre,alergia,eps,numero_emergencia]
        padre=[nombre_padre,profesion_padre,cedula_padre,direccion_padre]
        madre=[nombre_madre,profesion_madre,cedula_madre,direccion_madre]
        acudiente=[nombre_acudiente,profesion_acudiente,cedula_acudiente,direccion_acudiente]
        
        matricula_obj=[estudiante,padre,madre,acudiente]

        nombre_estudiante.value

        mensaje_maticula_correcta.title=ft.Text(
            f"El estudiante {nombre_estudiante.value} se a matriculado correctamente",
            font_family="Alice"
            )
        mensaje_maticula_correcta.open=True
        

        matricula_value=[]
        for i in range (len(matricula_obj)):
            
            if i==3:
                matriculados.append(matricula_value)
                
            for j in range (len(matricula_obj[i])):
                datos=matricula_obj[i][j].value
                matricula_value.append(datos)

                matricula_obj[i][j].value=""

        print(matriculados)

        page.update()

        


        
        




    #------------- PAGINA PRINCIPAL -------------
    
    #-----------------Contenido-------------------
            
    imagen = ft.Container(
            
            content = ft.Image(src="img/logo.png",width=450,height=500,expand=True),
            alignment=ft.alignment.center,
            expand=True,
            width=500
        )
    
    usuario=ft.TextField(
                        label="Username",width=380,bgcolor="White",border_color="transparent",autofocus=True,text_style=ft.TextStyle(size=20,font_family="Alice"),label_style=ft.TextStyle(size=24,font_family="Alice",color=ft.colors.with_opacity(0.4,"black"),weight=ft.FontWeight.BOLD)
                        )
    
    Contraseña= ft.TextField(
                        label="Password",width=380,password=True,can_reveal_password=True,bgcolor="White",border_color="transparent",text_style=ft.TextStyle(size=20,font_family="Alice"),label_style=ft.TextStyle(size=24,font_family="Alice",color=ft.colors.with_opacity(0.4,"black"),weight=ft.FontWeight.BOLD)
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
                    ft.Container(width=20,height=10),

                    ft.Text(
                        "SING IN",width=380,text_align=ft.TextAlign.CENTER,size=50,weight=ft.FontWeight.BOLD,color=colores[1], font_family="Alice"
                        ),
                    
                    ft.Container(width=20,height=30),

                    usuario,

                    ft.Container(width=20,height=30),

                    Contraseña,

                    ft.Container(width=20,height=30),

                    ft.ElevatedButton(
                        "LOGIN",height=50,width=380,bgcolor=colores[1],color="White",
                        

                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=0),
                            
                            
                        ),
                        on_click=lambda _: validacion(usuario,Contraseña)
                        ),
                    

                ]
            )            
        )
    
    

    login = ft.Container(
        margin=ft.margin.only(left=40,top=40,right=80,bottom=0),
        content=ft.Row(

            controls=[imagen,user]),
    )       
    

# ---------------General-----------------
    nav_button_style=ft.ButtonStyle(

        shape=ft.RoundedRectangleBorder(radius=0),
        bgcolor=ft.colors.TRANSPARENT,
        color="Black",
        
        )

    barra_navegacion = ft.AppBar(

        leading=ft.Container(

            ft.Image(
                src="img/logo1.png",width=150,
                height=100
            ),
            margin=ft.margin.only(left=31,top=0,right=0,bottom=0)
        ),

        leading_width=180,
        bgcolor=colores[3],
        toolbar_height=110,

        actions=[ft.Container(
            
            ft.TextButton(
                
                "Matriculas",
                width=160,
                height=60,
                style=nav_button_style,
                on_click=lambda _: page.go("/Matricula")
                ),

            margin=ft.margin.only(right=30),
            ),
            
            ft.Container(

                ft.TextButton(

                    "Boletines",
                    width=160,
                    height=60,
                    style=nav_button_style, 
                    on_click=lambda _: page.go("/Boletines")
                    ), 
                margin=ft.margin.only(right=30)
                ),
                            
                ft.Container(

                    ft.TextButton(
                        
                        "Mensualidades",
                        width=160,
                        height=60,
                        style=nav_button_style,
                        on_click=lambda _: page.go("/Mensualidad")
                        ), 
                    margin=ft.margin.only(right=80)
                    ),

                ft.Container(

                    ft.TextButton(
                        
                        "Salir",
                        width=160,
                        height=60,
                        style=nav_button_style,
                        on_click=lambda _: page.go("/")
                        ), 
                    
                    margin=ft.margin.only(right=70)
                    ),
        ]
        
    )

# ---------------Bienvenido-----------------
    imagen_bienvenida=ft.Container(
            
            content = ft.Image(src="img/welcome.png",width=300,height=300),
            alignment=ft.alignment.center
        )
    
    bienvenida = ft.Container(
        
        content=ft.Column(
                controls=[
                    ft.Text(

                        "Bienvenido al sistema de gestion Jardin Happy face",
                        text_align=ft.TextAlign.CENTER,
                        font_family="Alice",
                        color=ft.colors.with_opacity(0.45,"Black"),
                        size=25,
                        weight="BOLD"
                        
                        ),

                imagen_bienvenida
            ],

            width=380,
            
    ),
    
    alignment=ft.alignment.center,
    height=500,
    margin=ft.margin.only(top=90)
    

    )

# ---------------Matriculas-----------------

    #-------------------------Estudiante----------------------
    nombre_estudiante=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=450
    )

    fecha_nacimiento=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20,
        text_style=ft.TextStyle(font_family="Alice"),
        width=320
    )

    edad=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=130
    )



    datos_estudiante_fila1=ft.Container(

        margin=ft.margin.only(left=20,right=20),
                                        
        content=ft.Row([

            ft.Container(

                margin=ft.margin.only(right=20),
                content=ft.Row([

                    ft.Text("Nombre: ",font_family="Alice",size=20),
                    nombre_estudiante,
                ])),

            ft.Container(

                margin=ft.margin.only(right=20),
                content=ft.Row([

                    ft.Text("Fecha de nacimiento: ",font_family="Alice",size=20),
                    fecha_nacimiento,
                ])),
            
            ft.Container(

                margin=ft.margin.only(right=20),

                content=ft.Row([

                    ft.Text("Edad: ",font_family="Alice",size=20),
                    edad,
                ])),
        ])
    )


    documento=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=417
    )

    tipo_documento=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=320
    )

    grado=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=130
    )



    datos_estudiante_fila2=ft.Container(

        margin=ft.margin.only(left=20,right=20),

        content=ft.Row([

            ft.Container(

                margin=ft.margin.only(right=20),
                content=ft.Row([

                    ft.Text("Documento: ",font_family="Alice",size=20),
                    documento,
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),

                content=ft.Row([

                    ft.Text("Tipo de documento:   ",font_family="Alice",size=20),
                    tipo_documento,
                ])),
            
            ft.Container(

                margin=ft.margin.only(right=20),

                content=ft.Row([
                    ft.Text("Grado: ",font_family="Alice",size=20),
                    grado,
                ])),
        ])
    )


    tipo_sangre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=70)

    alergia=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=205)

    eps=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=245)

    numero_emergencia=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=190)

    datos_estudiante_fila3=ft.Container(

        margin=ft.margin.only(left=20,right=20),

        content=ft.Row([

            ft.Container(

                margin=ft.margin.only(right=20),
                content=ft.Row([

                    ft.Text("Tipo de sangre: ",font_family="Alice",size=20),tipo_sangre,
                
                ])),

            ft.Container(

                margin=ft.margin.only(right=20),

                content=ft.Row([

                    ft.Text("Alergia: ",font_family="Alice",size=20),alergia,
                
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),

                content=ft.Row([

                    ft.Text("EPS:   ",font_family="Alice",size=20),eps,
                
                ])),
            
            ft.Container(

                margin=ft.margin.only(right=20),

                content=ft.Row([

                    ft.Text("Numero de emergencia: ",font_family="Alice",size=20),numero_emergencia,
                
                ])),
        ])
    )
    
    
    botones_matricula_matriculados= ft.Container(content=ft.Row([

        ft.TextButton(
            text="Matriculas",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),
                bgcolor=colores[2],
                color="Black",
                ),
                height=60, width=160,on_click=lambda _: page.go("/Matricula")),

        ft.TextButton(text="Matriculados",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=0),
                        bgcolor=colores[3],
                        color="Black",  
                    ),height=60,width=160,on_click=lambda _: page.go("/Matriculados"))
    ]),

    margin=ft.margin.only(top=50)
    )

    datos_estudiante=ft.Container(
        content=ft.Column([ft.Column([

            botones_matricula_matriculados,

            ft.Container(
                ft.Text("   Estudiante",font_family="Alice",size=25),
                alignment=ft.alignment.center_left,
                bgcolor=colores[2],
                margin=ft.margin.only(bottom=5)
                )
        ],spacing=0),

            datos_estudiante_fila1,
            datos_estudiante_fila2,
            datos_estudiante_fila3
        ])
    )
    #--------------------Padre----------------------

    nombre_padre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=500
    )

    profesion_padre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20,
        text_style=ft.TextStyle(font_family="Alice"),
        width=480
        )

    datos_padre_fila1=ft.Container(

        margin=ft.margin.only(left=20,right=20),
        content=ft.Row([

            ft.Container(

                margin=ft.margin.only(right=20),
                content=ft.Row([

                    ft.Text("Nombre: ",font_family="Alice",size=20),
                    nombre_padre,
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),
                content=ft.Row([

                    ft.Text("Profesion:   ",font_family="Alice",size=20),
                    
                    profesion_padre,
                ])),
            
        ])
    )
    
    cedula_padre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=260
        )

    telefono_padre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=260
        )


    direccion_padre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20,
        text_style=ft.TextStyle(font_family="Alice"),
        width=332
        )

    datos_padre_fila2=ft.Container(margin=ft.margin.only(left=20,right=20),
        content=ft.Row([

            ft.Container(

                margin=ft.margin.only(right=20),
                content=ft.Row([

                    ft.Text("Cedula:   ",font_family="Alice",size=20),
                    cedula_padre,
                
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),
                content=ft.Row([

                    ft.Text("Telefono:   ",font_family="Alice",size=20),
                    telefono_padre,
                
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),
                content=ft.Row([

                    ft.Text("Direccion:   ",font_family="Alice",size=20),
                    direccion_padre,
                
                ])),
            
        ])
    )
    
    datos_padre=ft.Container(
        content=ft.Column([

            ft.Container(

                ft.Text("   Padre",font_family="Alice",size=25),
                alignment=ft.alignment.center_left,
                bgcolor=colores[2],
                margin=ft.margin.only(bottom=5)
                ),

            datos_padre_fila1,
            datos_padre_fila2
            
        ])
    )
    #--------------------Madre---------------------
    nombre_madre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=500
    )

    profesion_madre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20,
        text_style=ft.TextStyle(font_family="Alice"),
        width=480
        )

    datos_madre_fila1=ft.Container(

        margin=ft.margin.only(left=20,right=20),
        content=ft.Row([

            ft.Container(

                margin=ft.margin.only(right=20),
                content=ft.Row([

                    ft.Text("Nombre: ",font_family="Alice",size=20),
                    nombre_madre,
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),
                content=ft.Row([

                    ft.Text("Profesion:   ",font_family="Alice",size=20),
                    
                    profesion_madre,
                ])),
            
        ])
    )
    
    cedula_madre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=260
        )

    telefono_madre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=260
        )


    direccion_madre=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20,
        text_style=ft.TextStyle(font_family="Alice"),
        width=332
        )

    datos_madre_fila2=ft.Container(
        margin=ft.margin.only(left=20,right=20),

        content=ft.Row([

            ft.Container(

                margin=ft.margin.only(right=20),

                content=ft.Row([

                    ft.Text("Cedula:   ",font_family="Alice",size=20),cedula_madre,
                
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),

                content=ft.Row([

                    ft.Text("Telefono:   ",font_family="Alice",size=20),telefono_madre,
                
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),

                content=ft.Row([

                    ft.Text("Direccion:   ",font_family="Alice",size=20),direccion_madre,
                
                ])),
            
        ])
    )
    
    datos_madre=ft.Container(

        content=ft.Column([

            ft.Container(

                ft.Text("   Madre",font_family="Alice",size=25),
                alignment=ft.alignment.center_left,
                bgcolor=colores[2],
                margin=ft.margin.only(bottom=5)
                ),

            datos_madre_fila1,
            datos_madre_fila2
            
        ])
    )

    #--------------------Acudiente---------------------
    nombre_acudiente=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=500
    )

    profesion_acudiente=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20,
        text_style=ft.TextStyle(font_family="Alice"),
        width=480
        )

    datos_acudiente_fila1=ft.Container(

        margin=ft.margin.only(left=20,right=20),
        content=ft.Row([

            ft.Container(

                margin=ft.margin.only(right=20),
                content=ft.Row([

                    ft.Text("Nombre: ",font_family="Alice",size=20),
                    nombre_acudiente,
                ])),

            ft.Container(

                margin=ft.margin.only(right=10),
                content=ft.Row([

                    ft.Text("Profesion:   ",font_family="Alice",size=20),
                    
                    profesion_acudiente,
                ])),
            
        ])
    )
    
    cedula_acudiente=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=260
        )

    telefono_acudiente=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,content_padding=5,
        text_size=20, 
        text_style=ft.TextStyle(font_family="Alice"),
        width=260
        )


    direccion_acudiente=ft.TextField(

        bgcolor=colores[3],
        border_color=ft.colors.TRANSPARENT,
        height=35,
        content_padding=5,
        text_size=20,
        text_style=ft.TextStyle(font_family="Alice"),
        width=332
        )

    datos_acudiente_fila2=ft.Container(margin=ft.margin.only(left=20,right=20),
        content=ft.Row([
            ft.Container(
                margin=ft.margin.only(right=20),
                content=ft.Row([
                    ft.Text("Cedula:   ",font_family="Alice",size=20),cedula_acudiente,
                
                ])),

            ft.Container(
                margin=ft.margin.only(right=10),
                content=ft.Row([
                    ft.Text("Telefono:   ",font_family="Alice",size=20),telefono_acudiente,
                
                ])),

            ft.Container(
                margin=ft.margin.only(right=10),
                content=ft.Row([
                    ft.Text("Direccion:   ",font_family="Alice",size=20),direccion_acudiente,
                
                ])),
            
        ])
    )
    
    datos_acudiente=ft.Container(
        content=ft.Column([

            ft.Container(
                ft.Text("   Acudiente",font_family="Alice",size=25),
                alignment=ft.alignment.center_left,
                bgcolor=colores[2],
                margin=ft.margin.only(bottom=5)
                ),

            datos_acudiente_fila1,
            datos_acudiente_fila2
            
        ])
    )


    # ---------------------------------------------------
    matriculados=[]


    mensaje_maticula_correcta=ft.AlertDialog()

    vista_matriculas=ft.Container(

        content=ft.Column([

            datos_estudiante,
            datos_padre,
            datos_madre,
            datos_acudiente,

            ft.Container(
                ft.TextButton(
                    "Matricular",
                    height=40,

                    width=196,
                    on_click=llamar_datos_matricula,

                    style=ft.ButtonStyle(
                                            
                        shape=ft.RoundedRectangleBorder(radius=0),
                        bgcolor="#7ED957",
                        color="Black",
                    ),
                    

                ),
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=10,bottom=20)),
                mensaje_maticula_correcta
                


                

        ],
        height=600,
        scroll=ft.ScrollMode.ALWAYS)
    )

    
    


#-----------------------------Matriculados----------------------
    

    encabezado=ft.Column([

            botones_matricula_matriculados,

            ft.Container(
                ft.Text("   Estudiante",font_family="Alice",size=25),
                alignment=ft.alignment.center_left,
                bgcolor=colores[2],
                margin=ft.margin.only(bottom=5)
                )
        ],spacing=0)
    
    alumno=ft.Column()

    def mostrar(self):
        print(matriculados)
        alumno.clean()
        for i in range(len(matriculados)):
                
                alumno.controls.append(ft.Row([
                    ft.Text(f"nombre estudiante: {matriculados[i][0]}  "),
                    ft.Text(f"grado: {matriculados[i][5]}")
                    
                ]
                    ))
                
                
                page.update()

    vista_matriculados=ft.Container(

        content=ft.Column([
            encabezado,
            ft.ElevatedButton("prueba",on_click=mostrar),
            alumno
                

        ],
        height=600,
        scroll=ft.ScrollMode.ALWAYS)
    )
    
    # page.add(barra_navegacion,vista_matriculados)
    
        
# ---------------Enrutado-----------------
    
    def route_change(route):
        vista1=ft.View(
                "/",
                [
                    login
                ],
            )
        page.views.clear()
        page.views.append(  vista1  )
        
        
        if page.route == "/principal":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/principal",
                    [

                        bienvenida
                    ],appbar=barra_navegacion

                )
            )
        


        if page.route == "/Matricula":
            
            page.views.clear()
            page.scroll="always"
            page.views.append(
                ft.View(
                    "/Matricula",
                    
                    [
                        vista_matriculas 
                    ],
                    appbar=barra_navegacion,
                    padding=0,
                    
                    
                )
            )
        
        if page.route == "/Matriculados":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/Matriculados",
                    [
                        vista_matriculados
                    ],appbar=barra_navegacion
                )
            )
            

        if page.route == "/Boletines":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/Boletines",
                    [
                        ft.Text("Boletines")
                    ],appbar=barra_navegacion
                )
            )
        

        if page.route == "/Mensualidad":
            page.views.clear()
            page.views.append(
                ft.View(
                    "/Mensualidad",
                    [
                        ft.Text("mensualidad")
                    ],appbar=barra_navegacion
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



