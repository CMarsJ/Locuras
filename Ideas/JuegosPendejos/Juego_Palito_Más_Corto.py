#Código Juego del palito más corto
#Librerias
from random import shuffle

#Lista
Palitos = ["-","--","---","----"]
#Mescla
def mescla(lista):
    shuffle(lista)
    return lista

#Eleción
def probar_suerte():
    intento = " "
    while intento not in ["1","2","3","4"]:
        intento = input("Ingre un numero del 1 al 4 :")
    return int(intento)

#Comprobación
def chequear_intento(lista,intento):
    if lista[intento-1] == "-":
        print("A lavar los platos")
    else:
        print("Te has salvado")
    print(f"Te ha tocado {lista[intento-1]}")

palisto_mesclados = mescla(Palitos)
Seleccion = probar_suerte()
Chequeo = chequear_intento(Palitos,Seleccion)
