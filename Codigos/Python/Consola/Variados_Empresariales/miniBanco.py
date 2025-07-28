#Codigo mini Banquito

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cuenta(Persona):
    def __init__(self, nombre, apellido, saldo=0):
        super().__init__(nombre, apellido)
        self.saldo = saldo

    def __str__(self):
        return f"Cuenta de {self.nombre} {self.apellido} con saldo: {self.saldo}"

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Retiro fallido. Verifique el monto o saldo insuficiente.")
def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    return Cuenta(nombre, apellido)
def main():
    cliente = crear_cliente()
    print(cliente)
    while True:
        accion = input("¿Desea depositar (d), retirar (r) o salir (s)? ").lower()
        if accion == 'd':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cliente.depositar(cantidad)
        elif accion == 'r':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(cantidad)
        elif accion == 's':
            print("Gracias por usar el mini Banquito. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
main()