#Recetario
#Librerias
from pathlib import Path
from os import system

#Funcion NumeroRecetas
def Numero_Recetas(DireccionRecetas):
    N = 0
    for carpeta in DireccionRecetas.iterdir():
        if carpeta.is_dir():
            N += len(list(carpeta.glob("*.txt")))
    return N

#Funcion Mirar_Categorias
def Mirar_Categorias(DireccionRecetas):
    categorias = []
    for carpeta in DireccionRecetas.iterdir():
        if carpeta.is_dir():
            categorias.append(carpeta.name)
    return categorias

#Funcion Elegir_Categoria
def Elegir_Categoria(categorias):
    Eleccion_Categoria = " "
    # Elegir categoria
    while Eleccion_Categoria not in categorias:
        print(f"Categorias Disponibles: {', '.join(categorias)}")
        Eleccion_Categoria = input("Elija una categoria: ")
        if Eleccion_Categoria in categorias:
            print(f"Has elegido la categoria: {Eleccion_Categoria}")
        else:
            print("Categoria no valida. Por favor, intente de nuevo.")
    DireccionRecetas = Path("Recetas") / Eleccion_Categoria
    return Eleccion_Categoria, DireccionRecetas

#Funcion mirar_recetas
def mirar_recetas(DireccionRecetas):
    system("cls")
    print("Recetas Disponibles:")
    recetas = []
    for archivo in DireccionRecetas.glob("*.txt"):
        recetas.append(archivo.stem)
    print(f"Recetas encontradas: {', '.join(recetas)}")
    return recetas

#Funcion leer_recetas
def leer_recetas(categorias):
    system("cls")
    print("Bienvenido al Recetario")
    Eleccion_Categoria, DireccionRecetas = Elegir_Categoria(categorias)
    Eleccion_Receta = " "
    # Mostrar recetas de la categoria elegida
    
    Recetas_Disponibles = mirar_recetas(DireccionRecetas)
   
    #Ver receta especifica
    while Eleccion_Receta not in Recetas_Disponibles:
        Eleccion_Receta = input("Ingrese el nombre de la receta que desea ver (sin .txt): ")
        if Eleccion_Receta in Recetas_Disponibles:
            Receta_Path = DireccionRecetas / f"{Eleccion_Receta}.txt"
            with open(Receta_Path, 'r', encoding='utf-8') as file:
                contenido = file.read()
                print(f"Contenido de la receta {Eleccion_Receta}:\n{contenido}")
        else:
            print("Receta no valida. Por favor, intente de nuevo.")

#Funcion crear_receta
def crear_receta(categorias):
    system("cls")
    print("Crear Receta")
    Eleccion_Categoria, DireccionRecetas = Elegir_Categoria(categorias)
    nombre_receta = input("Ingrese el nombre de la receta (sin espacios): ")
    Contenido = input("Ingrese el contenido de la receta: ")
    with open(f"Recetas/{Eleccion_Categoria}/{nombre_receta}.txt", "w") as archivo:
       N = False
       while N == False:
            Contenido = input("Ingrese el contenido: ")
            if Contenido.strip() == "":
                print("El contenido no puede estar vacio. Por favor, intente de nuevo.")
            else:
                archivo.write(f"{Contenido}\n")
                P = input("Desea agregar mas contenido? (S/N): ").strip().upper()
                if P == "N":
                    N = True
    print(f"Receta '{nombre_receta}' creada exitosamente.")

#Funcion crear_categoria
def crear_categoria(categorias):
    system("cls")
    print("Crear Categoria")
    nueva_categoria = input("Ingrese el nombre de la nueva categoria: ")
    if nueva_categoria not in categorias:
        DireccionRecetas = Path("Recetas") / nueva_categoria
        DireccionRecetas.mkdir(parents=True, exist_ok=True)
        print(f"Categoria '{nueva_categoria}' creada exitosamente.")
    else:
        print(f"La categoria '{nueva_categoria}' ya existe.")

#Funcion eliminar_receta
def eliminar_receta(categorias):
    system("cls")
    print("Eliminar Receta")
    Eleccion_Categoria, DireccionRecetas = Elegir_Categoria(categorias)
    Recetas_Disponibles = mirar_recetas(DireccionRecetas)
    Eleccion_Receta = input("Ingrese el nombre de la receta que desea eliminar (sin .txt): ")
    if Eleccion_Receta in Recetas_Disponibles:
        Receta_Path = DireccionRecetas / f"{Eleccion_Receta}.txt"
        Receta_Path.unlink()
        print(f"Receta '{Eleccion_Receta}' eliminada exitosamente.")
    else:
        print("Receta no encontrada.")

#Funcion eliminar_categoria
def eliminar_categoria(categorias):
    system("cls")
    print("Eliminar Categoria")
    Eleccion_Categoria,DireccionRecetas = Elegir_Categoria(categorias)
    DireccionRecetas.rmdir()
    print(f"Categoria '{Eleccion_Categoria}' eliminada exitosamente.")
    

#Funcion Menu
def Menu(DireccionRecetas,NumeroRecetas, categorias):
    print("Bienvenido al Recetario")
    print(f"Las recetas estan guardadas en {DireccionRecetas}")
    print(f"Tienes {NumeroRecetas} recetas guardadas")
    print("1. Ver Recetas")
    print("2. Crear Receta")
    print("3. Crear Categoria")
    print("4. Eliminar Receta")
    print("5. Eliminar Categoria")
    print("6. Finalizar Programa")
    opcion = input("Seleccione el numero de la opcion  a realizar(1 a 6): ")
    while opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("Opcion no valida, intente de nuevo.")
        opcion = input("Seleccione el numero de la opcion a realizar: ")
    if opcion == "1":
        leer_recetas(categorias)
    elif opcion == "2":
        crear_receta(categorias)
    elif opcion == "3":
        crear_categoria(categorias)
    elif opcion == "4":
        eliminar_receta(categorias)
    elif opcion == "5":
        eliminar_categoria(categorias)
    elif opcion == "6":
        system("cls")
        print("Gracias por usar el Recetario")
        exit()
    print("----------------------------------")
#Funcion Main
def Main():
    # Definir la ruta de las recetas
    DireccionRecetas = Path("Recetas")
    # Verificar si la carpeta de recetas existe, si no, crearla
    if not DireccionRecetas.exists():
        DireccionRecetas.mkdir()
    while True:
        # Contar el numero de recetas en la carpeta
        NumeroRecetas = Numero_Recetas(DireccionRecetas)
        # Mirar las categorias disponibles
        categorias = Mirar_Categorias(DireccionRecetas)
        # Mostrar el menu
        Menu(DireccionRecetas, NumeroRecetas, categorias)

Main()