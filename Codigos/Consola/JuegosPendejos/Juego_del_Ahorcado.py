#Juego del Ahorcado
#Librería para el juego del ahorcado
from random import choice
#Bases Para el juego del ahorcado
Palabras = ["python", "java", "javascript", "csharp", "ruby", "php", "swift", "kotlin", "typescript", "golang"]
Letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Vidas = 7
Palabra = ""
Actual = ""
Letras_adivinadas = []
Letras_incorrectas = []
letra_actual = ""
#Función para elegir una palabra aleatoria
def elegir_palabra(Palabras):
    Palabra = choice(Palabras)
    return Palabra
#Función Solicitar letra al usuario
def solicitar_letra(Letras):
    letra = input("Introduce una letra: ").strip()
    while len(letra) != 1 or letra not in Letras:
        print("Entrada inválida. Debes introducir una sola letra.")
        letra = input("Introduce una letra: ").strip()
    return letra.lower()
#Función para general texto de bienvenida y reglas del juego
def mostrar_bienvenida():
    print("¡Bienvenido al juego del Ahorcado!")
    print("Reglas:")
    print("1. Debes adivinar la palabra oculta letra por letra.")
    print("2. Tienes un total de 7 vidas.")
    print("3. Si adivinas una letra correcta, se mostrará en la palabra.")
    print("4. Si adivinas una letra incorrecta, perderás una vida.")
    print("5. El juego termina cuando adivinas la palabra o pierdes todas tus vidas.")
#Función para verificar y mostrar el estado del juego
def mostrar_estado(Palabra, Letras_adivinadas, Vidas):
    print("┌───────┐")
    print("│       │")
    if Vidas == 6:
        print("│       O   ")
    elif Vidas == 5:
        print("│       O   ")
        print("│       |  ")
    elif Vidas == 4:
        print("│       O   ")
        print("│      /|  ")
    elif Vidas == 3:
        print("│       O   ")
        print("│      /|\  ")
    elif Vidas == 2:
        print("│       O   ")
        print("│      /|\  ")
        print("│      /    ")
    elif Vidas == 0:
        print("│       O   ")
        print("│      /|\  ")
        print("│      / \   ")
    print("│               ")
    print("└──────────────┘")
    print("Palabra:", end=" ")
    for letra in Palabra:
        if letra in Letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\nVidas restantes:", Vidas)
#Función principal del juego
def jugar():
    mostrar_bienvenida()
    Palabra = elegir_palabra(Palabras)
    Actual = "_" * len(Palabra)
    Letras_adivinadas = []
    Letras_incorrectas = []
    Vidas = 7

    while Vidas > 0 and Actual != Palabra:
        mostrar_estado(Palabra, Letras_adivinadas, Vidas)
        letra_actual = solicitar_letra(Letras)
        
        if letra_actual in Letras_adivinadas or letra_actual in Letras_incorrectas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue
        
        if letra_actual in Palabra:
            Letras_adivinadas.append(letra_actual)
            Actual = "".join([letra if letra in Letras_adivinadas else "_" for letra in Palabra])
        else:
            Letras_incorrectas.append(letra_actual)
            Vidas -= 1
        
    if Actual == Palabra:
        print("¡Felicidades! Has adivinado la palabra:", Palabra)
    else:
        print("Has perdido. La palabra era:", Palabra)

jugar()