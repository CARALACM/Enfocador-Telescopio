import machine
import time


reset = machine.Pin(13, machine.Pin.OUT)
step = machine.Pin(14, machine.Pin.OUT)
direction = machine.Pin(15, machine.Pin.OUT)
led = machine.Pin(25, machine.Pin.OUT)

def pro_horario(velocidad, pasos):
    reset.value(1)
    for i in range(int(pasos)):
        step.value(1)
        step.value(0)
        time.sleep(float(velocidad))
    reset.value(0)

def con_horario(velocidad, pasos):
    direction.value(1)
    reset.value(1)
    for i in range(int(pasos)):
        step.value(1)
        step.value(0)
        time.sleep(float(velocidad))
    reset.value(0)
    direction.value(0)
