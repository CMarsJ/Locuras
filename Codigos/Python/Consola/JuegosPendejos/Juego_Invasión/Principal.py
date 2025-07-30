#Librerias
import pygame
import random


#Inicializar pygame
pygame.init()

#Creacion de pantalla
Pantalla = pygame.display.set_mode((800, 600))
#Titulo de la ventana y Icono
pygame.display.set_caption("Invasión Espacial")
Icono = pygame.image.load("Ovni.png")
pygame.display.set_icon(Icono)

#Jugador y sus variables
Jugador = pygame.image.load("Nave.png")
JugadorX = 380
JugadorY = 532
Jugador_X_Cambio = 0
Velocidad_Jugador = 0.2

#Enemigo1 y sus variables
Enemigo1 = pygame.image.load("Enemigo.png")
Enemigo1X = random.randint(0, 736)
Enemigo1Y = 100
Enemigo1_X_Cambio = 0.15
Enemigo1_Y_Cambio = 30

#Posicion del jugador
def JugadorPosicion(X,Y):
    Pantalla.blit(Jugador, (X, Y))

#Posicion del enemigo1
def Enemigo1Posicion(X,Y):
    Pantalla.blit(Enemigo1, (X, Y))

Activa = True
#Bucle principal
while Activa:
    # Rellenar la pantalla
    Pantalla.fill((0, 144, 210))  
    #Revisar eventos
    for evento in pygame.event.get():
        #Si se cierra la ventana
        if evento.type == pygame.QUIT:
            Activa = False
        #Si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                Jugador_X_Cambio = -Velocidad_Jugador
            if evento.key == pygame.K_d:
                Jugador_X_Cambio = Velocidad_Jugador
        #Si se suelta una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                Jugador_X_Cambio = 0
        

    # Actualizar la posición del jugador
    JugadorX += Jugador_X_Cambio
    #Limitar el movimiento del jugador
    if JugadorX <= 0:
        JugadorX = 0
    elif JugadorX >= 736:
        JugadorX = 736

    # Actualizar la posición del jugador
    Enemigo1X += Enemigo1_X_Cambio
    #Limitar el movimiento del Enemigo1
    if Enemigo1X <= 0:
        Enemigo1_X_Cambio = 0.15
        Enemigo1Y += Enemigo1_Y_Cambio
    elif Enemigo1X >= 736:
        Enemigo1_X_Cambio = -0.15
        Enemigo1Y += Enemigo1_Y_Cambio
    
    # Dibujar al jugador
    JugadorPosicion(JugadorX, JugadorY)
    # Dibujar enemigo1
    Enemigo1Posicion(Enemigo1X, Enemigo1Y)

    # Actualizar la pantalla    
    pygame.display.update() 

