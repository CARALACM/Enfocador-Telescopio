from machine import Pin
import time

boton_rapido_i=machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_medio_i=machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_lento_i=machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)

boton_rapido_d=machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_medio_d=machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_lento_d=machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)

boton_posicion1=machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_posicion2=machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_posicion3=machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)

boton_posicion0i=machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_posicion0d=machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

led=Pin(0, Pin.OUT)

pins= [
     Pin (21, Pin.OUT), # IN1
     Pin (20, Pin.OUT), # IN2
     Pin (19, Pin.OUT), # IN3
     Pin (18, Pin.OUT)  # IN4
     ]
secuencia = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
    ]
secuencia2 = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]
    ]

vuelta=512
posicion=0
posicion1=100
posicion2=200
posicion3=300

while(True):
    if(boton_rapido_d.value()+boton_medio_d.value()+boton_lento_d.value()+boton_rapido_i.value()+boton_medio_i.value()+boton_lento_i.value()+boton_posicion1.value()+boton_posicion2.value()+boton_posicion3.value()+boton_posicion0d.value()+boton_posicion0i.value()    ==1):
        
        if(boton_rapido_i.value()==1):
            if(posicion>=1):
                posicion-=1
                for paso in secuencia2:
                    for i in range(len(pins)):
                        pins[i].value(paso[i])
                        time.sleep(0.001)
        elif(boton_medio_i.value()==1):
            if(posicion>=1):
                posicion-=1
                for paso in secuencia2:
                    for i in range(len(pins)):
                        pins[i].value(paso[i])
                        time.sleep(0.01)
        elif(boton_lento_i.value()==1):
            if(posicion>=1):
                posicion-=1
                for paso in secuencia2:
                    for i in range(len(pins)):
                        pins[i].value(paso[i])
                        time.sleep(0.1)

        elif(boton_rapido_d.value()==1):
            if(posicion<=vuelta-1):
                posicion+=1
                for paso in secuencia:
                    for i in range(len(pins)):
                        pins[i].value(paso[i])
                        time.sleep(0.001)
        elif(boton_medio_d.value()==1):
            if(posicion<=vuelta-1):
                posicion+=1
                for paso in secuencia:
                    for i in range(len(pins)):
                        pins[i].value(paso[i])
                        time.sleep(0.01)
        elif(boton_lento_d.value()==1):
            if(posicion<=vuelta-1):
                posicion+=1
                for paso in secuencia:
                    for i in range(len(pins)):
                        pins[i].value(paso[i])
                        time.sleep(0.1)

        elif(boton_posicion1.value()==1):
            crono=0
            while(boton_posicion1.value()==1):
                time.sleep(0.0001)
                crono+=0.0001
            if(crono>=10):
                posicion1=posicion
            else:
                if(posicion1>posicion):
                    for j in range(posicion1-posicion):
                        posicion+=1
                        for paso in secuencia:
                            for i in range(len(pins)):
                                pins[i].value(paso[i])
                                time.sleep(0.001)
                elif(posicion1<posicion):
                    for j in range(posicion-posicion1):
                        posicion-=1
                        for paso in secuencia2:
                            for i in range(len(pins)):
                                pins[i].value(paso[i])
                                time.sleep(0.001)

        elif(boton_posicion2.value()==1):
            crono=0
            while(boton_posicion2.value()==1):
                time.sleep(0.0001)
                crono+=0.0001
            if(crono>=10):
                posicion2=posicion
            else:
                if(posicion2>posicion):
                    for j in range(posicion2-posicion):
                        posicion+=1
                        for paso in secuencia:
                            for i in range(len(pins)):
                                pins[i].value(paso[i])
                                time.sleep(0.001)
                elif(posicion2<posicion):
                    for j in range(posicion-posicion2):
                        posicion-=1
                        for paso in secuencia2:
                            for i in range(len(pins)):
                                pins[i].value(paso[i])
                                time.sleep(0.001)
        
        elif(boton_posicion3.value()==1):
            crono=0
            while(boton_posicion3.value()==1):
                time.sleep(0.0001)
                crono+=0.0001
            if(crono>=10):
                posicion3=posicion
            else:
                if(posicion3>posicion):
                    for j in range(posicion3-posicion):
                        posicion+=1
                        for paso in secuencia:
                            for i in range(len(pins)):
                                pins[i].value(paso[i])
                                time.sleep(0.001)
                elif(posicion3<posicion):
                    for j in range(posicion-posicion3):
                        posicion-=1
                        for paso in secuencia2:
                            for i in range(len(pins)):
                                pins[i].value(paso[i])
                                time.sleep(0.001)

        if(boton_posicion0d.value()==1):
            posicion=0
            for paso in secuencia:
                for i in range(len(pins)):
                    pins[i].value(paso[i])
                    time.sleep(0.001)

        if(boton_posicion0i.value()==1):
            posicion=0
            for paso in secuencia2:
                for i in range(len(pins)):
                    pins[i].value(paso[i])
                    time.sleep(0.001)



