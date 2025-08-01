m1 = [[0,0,0],[0,0,0],[0,0,0]]
import random
print(m1)
def maquina(li):
    n = 0
    while(n == 0):
        l = random.randint(0,2)
        l2 = random.randint(0,2)
        if(li[l][l2] == 0):
            li[l][l2] = 2
            n = 1
m = 0
v = 0
while(m == 0):
    l = 0
    while(l == 0):
        x1 = int(input("Ingrese la fila donde desea por su x :"))
        x2 = int(input("Ingrese la columna donde desea por su x :"))
        if (m1[x1][x2] == 0):
            m1[x1][x2] = 1
            l = 1
    print(m1[0])
    print(m1[1])
    print(m1[2])
    v = v + 2
    if v == 9 :
        print("Fin del juego")
        m = 1
    else:
        maquina(m1)