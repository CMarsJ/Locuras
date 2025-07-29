from os import system

#Generador
def generarNumeros():
    n = 1
    while True:
        yield n
        n += 1

#Decorador
def decorador(func):
    def otra_funcion(Tipo, Numero):
        system("cls")
        print("------------------------------")
        print("Su turno es:")
        func(Tipo, Numero)
        print("Aguarde y sera atendido en breve")
        print("------------------------------\n")
    return otra_funcion

