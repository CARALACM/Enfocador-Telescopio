from machine import Pin
import time

bIR=machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
bIM=machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
bIL=machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)

bDR=machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
bDM=machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
bDL=machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)

bP1=machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
bP2=machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
bP3=machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)

bP0I=machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
bP0D=machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

led=Pin(0, Pin.OUT)
led.value(0)

salida=[
    Pin(21, Pin.OUT),
    Pin(20, Pin.OUT),
    Pin(19, Pin.OUT),
    Pin(18, Pin.OUT),
]

sD=[
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]
sI=[
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]
]

vuelta=1000 #360º = 512

posicion=0

try:
    archivo=open('posiciones.txt', 'r')
    p1=int(archivo.readline())
    p2=int(archivo.readline())
    p3=int(archivo.readline())
    archivo.close()
except:
    archivo=open('posiciones', 'w')
    archivo.write("0\n0\n0")
    archivo.close()
    p1=0
    p2=0
    p3=0

def encendido_led():
    led.value(1)
    time.sleep(1)
    led.value(0)

def guardado_posiciones():
    archivo=open('posiciones.txt', 'w')
    archivo.write(f"{p1}\n")
    archivo.write(f"{p2}\n")
    archivo.write(f"{p3}\n")
    archivo.close()

def estado_botones():
    return bIR.value()+bIM.value()+bIL.value()+bDR.value()+bDM.value()+bDL.value()+bP1.value()+bP2.value()+bP3.value()+bP0I.value()+bP0D.value() == 1

def velocidad(velocidad_giro):
    if(velocidad_giro=='r'):
        return 0.001
    elif(velocidad_giro=='m'):
        return 0.01
    elif(velocidad_giro=='l'):
        return 0.1

def giro(saltos, velocidad_giro, direccion, restriccion=True):
    global posicion
    print(posicion)
    
    if(restriccion):
        if(direccion=='d' and posicion<=vuelta-1):
            for w in range(saltos):
                posicion+=1
                for paso in sD:
                    for i in range(len(salida)):
                        salida[i].value(paso[i])
                        time.sleep(velocidad(velocidad_giro))
        elif(direccion=='i' and posicion>=1):
            for w in range(saltos):
                posicion-=1
                for paso in sI:
                    for i in range(len(salida)):
                        salida[i].value(paso[i])
                        time.sleep(velocidad(velocidad_giro))
    else:
        if(direccion=='d'):
            posicion=0
            for w in range(saltos):
                for paso in sD:
                    for i in range(len(salida)):
                        salida[i].value(paso[i])
                        time.sleep(velocidad(velocidad_giro))
        elif(direccion=='i'):
            posicion=0
            for w in range(saltos):
                for paso in sI:
                    for i in range(len(salida)):
                        salida[i].value(paso[i])
                        time.sleep(velocidad(velocidad_giro))
    
    salida[0].value(0)
    salida[1].value(0)
    salida[2].value(0)
    salida[3].value(0)




while(True):
    
    if(estado_botones()):
        
        if(bIR.value()==1):
            giro(1, 'r', 'd')
        elif(bIM.value()==1):
            giro(1, 'm', 'd')
        elif(bIL.value()==1):
            giro(1, 'l', 'd')
        elif(bDR.value()==1):
            giro(1, 'r', 'i')
        elif(bDM.value()==1):
            giro(1, 'm', 'i')
        elif(bDL.value()==1):
            giro(1, 'l', 'i')

        elif(bP1.value()==1):
            crono=0
            while(bP1.value()==1):
                time.sleep(0.0001)
                crono+=0.0001
            if(crono>=10):
                p1=posicion
                guardado_posiciones()
                encendido_led()
            else:
                if(p1>posicion):
                    giro(p1-posicion, 'r', 'd')
                elif(p1<posicion):
                    giro(posicion-p1, 'r', 'i')
        elif(bP2.value()==1):
            crono=0
            while(bP2.value()==1):
                time.sleep(0.0001)
                crono+=0.0001
            if(crono>=10):
                p2=posicion
                guardado_posiciones()
                encendido_led()
            else:
                if(p2>posicion):
                    giro(p2-posicion, 'r', 'd')
                elif(p2<posicion):
                    giro(posicion-p2, 'r', 'i')
        elif(bP3.value()==1):
            crono=0
            while(bP3.value()==1):
                time.sleep(0.0001)
                crono+=0.0001
            if(crono>=10):
                p3=posicion
                guardado_posiciones()
                encendido_led()
            else:
                if(p3>posicion):
                    giro(p3-posicion, 'r', 'd')
                elif(p3<posicion):
                    giro(posicion-p3, 'r', 'i')

        elif(bP0D.value()==1):
            led.value(1)
            giro(1, 'r', 'd', False)
            led.value(0)
        elif(bP0I.value()==1):
            led.value(1)
            giro(1, 'r', 'i', False)
            led.value(0)

