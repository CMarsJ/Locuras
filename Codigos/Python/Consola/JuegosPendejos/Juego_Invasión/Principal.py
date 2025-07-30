#Librerias
import pygame
import random
import math

#Inicializar pygame
pygame.init()

#Carga de Archivos
Icono = pygame.image.load("Ovni.png")
Fondo = pygame.image.load("Fondo.png")
Jugador = pygame.image.load("Nave.png")
Enemigo1 = pygame.image.load("Enemigo.png")
Bala = pygame.image.load("Bala.png")

#Creacion de pantalla
Pantalla = pygame.display.set_mode((800, 600))
#Titulo de la ventana y Icono
pygame.display.set_caption("Invasión Espacial")
pygame.display.set_icon(Icono)

#Variables
#Jugador 
JugadorX = 380
JugadorY = 532
Jugador_X_Cambio = 0
Velocidad_Jugador = 0.6
#Enemigo1 
Enemigo1X = random.randint(0, 736)
Enemigo1Y = 500
Enemigo1_X_Cambio = 0.5
Enemigo1_Y_Cambio = 80
#Bala
bala_x = 0
bala_y = 532
bala_Y_Cambio = 2
Bala_Visible = False
#Otras
Puntaje = 0
Vidas = 3

#Funciones
# De Posicionamiento
#Posicion del jugador
def JugadorPosicion(X,Y):
    Pantalla.blit(Jugador, (X, Y))

#Posicion del enemigo1
def Enemigo1Posicion(X,Y):
    Pantalla.blit(Enemigo1, (X, Y))

#Disparar bala
def BalaPosicion(X, Y):
    global Bala_Visible
    Bala_Visible = True
    Pantalla.blit(Bala, (X + 16, Y + 10))

#Colision
def Colision(Objeto1X, Objeto1Y, Objeto2X, Objeto2Y):
    distancia = math.sqrt(math.pow(Objeto1X - Objeto2X, 2) + math.pow(Objeto1Y - Objeto2Y, 2))
    if distancia < 27:
        return True
    else:
        return False

#Bucle principal
Activa = True
while Activa:
    # Fondo de la pantalla  
    Pantalla.blit(Fondo, (0, 0))
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
            #Si se presiona la tecla de disparo
            if evento.key == pygame.K_SPACE:
                if not Bala_Visible:
                    bala_x = JugadorX
                    BalaPosicion(bala_x, bala_y)
        #Si se suelta una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                Jugador_X_Cambio = 0

    # Actualizar la posición
    JugadorX += Jugador_X_Cambio #Jugador
    Enemigo1X += Enemigo1_X_Cambio #Enemigo1

    #Limitar el movimiento 
    #Jugador
    if JugadorX <= 0: 
        JugadorX = 0
    elif JugadorX >= 736:
        JugadorX = 736
    #Enemigo1
    if Enemigo1X <= 0: 
        Enemigo1_X_Cambio = 0.5
        Enemigo1Y += Enemigo1_Y_Cambio
    elif Enemigo1X >= 736:
        Enemigo1_X_Cambio = -0.5
        Enemigo1Y += Enemigo1_Y_Cambio
    # Bala
    if Bala_Visible:
        BalaPosicion(bala_x, bala_y)
        bala_y -= bala_Y_Cambio
        if bala_y <= -32:
            bala_y = 532
            Bala_Visible = False
    # Colision
    if Colision(Enemigo1X, Enemigo1Y, bala_x, bala_y):
        bala_y = 532
        Bala_Visible = False
        Enemigo1X = random.randint(0, 736)
        Enemigo1Y = 100
        Puntaje += 1

    # Si el enemigo llega al jugador
    if Enemigo1Y > 532:
        Enemigo1Y = 100
        Enemigo1X = random.randint(0, 736)
        Vidas -= 1
        if Vidas == 0:
            Pantalla.blit("Game Over", (320, 250))
            Pantalla.blit("Puntaje Final: " + str(Puntaje), (320, 300))
    
    # Mostrar el puntaje y vidas
    fuente = pygame.font.Font(None, 36)
    texto_puntaje = fuente.render(f"Puntaje: {Puntaje}", True, (255, 255, 255))
    texto_vidas = fuente.render(f"Vidas: {Vidas}", True, (255, 255, 255))
    Pantalla.blit(texto_puntaje, (10, 10))
    Pantalla.blit(texto_vidas, (10, 50))

    # Dibujar al jugador y Enemigo1
    JugadorPosicion(JugadorX, JugadorY)
    Enemigo1Posicion(Enemigo1X, Enemigo1Y)

    # Actualizar la pantalla    
    pygame.display.update() 

