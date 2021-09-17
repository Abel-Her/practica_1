mov = []
import time
def generar_sol(partida, llegada):
    mov.append(['Mover de la torre', partida, 'a la torre', llegada])

def hanoi(n,partida,pivote,llegada):
    if n == 1:
        generar_sol(partida, llegada)
    else:
        hanoi(n-1,partida,llegada,pivote)
        hanoi(1,partida,pivote,llegada)
        hanoi(n-1,pivote,partida,llegada)

def simulacion():
    hanoi(n,'A','B','C')
    k = 1
    for i in mov:
        i = " ".join(i)
        time.sleep(t)
        print('Paso', k ,':',i)
        k+=1


print('Bienvenido')

On = True
n = 3
t = 0
op = 0

while On:
    if op == 0:
        print('_______________________________________________________________')
        if t == 0:
            print('Simulación lista con', n,'Discos')
        else:
            print('Simulación lista con', n,'Discos','y',t,'s por movimiento')
        print('¿Qué desea hacer?')
        print('_______________________________________________________________')
        print('[1] Cambiar el número de discos')
        print('[2] Cambiar el tiempo entre movimientos')
        print('[3] Iniciar simulación')
        print('[4] Salir')
        print('_______________________________________________________________')
        mov=[]
        try:
            op = int(input('Seleccione una opción: '))
        except ValueError:
            pass
    if op == 1:
        try:
            n = int(input('Ingrese el número de discos: '))
        except ValueError:
            pass
    if op == 2:
        try:
            t = input('Ingrese el número de segundos: ')
        except ValueError:
            pass
    if op == 3:
        print('_________________________Simulación____________________________')
        simulacion()
        print('_______________________________________________________________')
        print('')
        print('¿Desea regresar al menu?','[1] Si','[0] No')
        try:
            op = input()
            op = int(op)-1
        except ValueError:
            pass
    if op == 4:
        On = False
        print('¡Vuelva pronto!')
    if op == -1:
        On = False
        print('¡Vuelva pronto!')
    op = 0
