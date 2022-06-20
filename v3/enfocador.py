from sys import exec_prefix
from tkinter import *
from tkinter import ttk, messagebox
import os
import _thread
import time
from sender import Sender

########################################   RAICES   ########################################
raiz = Tk()
raiz.title('caralacm v3.1')
raiz.resizable(False, False)

if(os.name=='nt'):
    raiz.iconbitmap(bitmap='escudo.ico')
elif(os.name=='posix'):
    messagebox.showinfo(title='Advertencia', message='Sistema Operativo no soportado.')
    raiz.destroy()
    exit()

########################################   MARCOS   ########################################
marco1 = Frame(raiz) # CONTIENE IMAGEN FONDO
marco1.pack(fill='both', padx=5, pady=5)

marco2 = Frame(raiz) # CONTIENE BOTONES Y DESCRIPCIONES
marco2.pack(expand=True, padx=5, pady=5)

marco3 = Frame(raiz) # CONTIENE INDICADORES DE CONEXION
marco3.pack(expand=True, padx=5, pady=15)

########################################  GLOBALES  ########################################
estado_boton = False
estado_conexion = False

etiqueta_conexion = StringVar(value='Sin Conexión')

combo = ttk.Combobox(marco3, state='readonly', values=[f'COM{i}' for i in range(1, 100)], width=7)
combo.grid(row=0, column=3, sticky='ns')
combo.set('COM19')

def temperatura():
    while(True):
        if not(estado_boton):
            enviador.send(('temperatura()'))
            temperatura = float(enviador.receive())
            print(temperatura)
            if(temperatura > 40):
                messagebox.showerror(title='Advertencia', message='Temperatura muy alta.')
                raiz.destroy()
                exit()
        time.sleep(1)

def conectar():
    global enviador, estado_conexion
    try:
        enviador = Sender(combo.get())
        _thread.start_new_thread(temperatura, ())
    except:
        messagebox.showerror(title='Error conexión', message='No se ha podido conectar.\nIntente nuevamente o cambie de puerto COM.')
        etiqueta_conexion.set('Sin Conexión')
        estado_conexion = False
    else:
        etiqueta_conexion.set(f'{combo.get()} conectado.')
        estado_conexion = True

def derecha():
    if(estado_conexion):
        while(estado_boton):
            enviador.send('pro_horario(0.01, 5)')
    else:
        messagebox.showwarning(title='Falta conectar', message='Primero debe conectarse a un dispositivo.')
def izquierda():
    if(estado_conexion):
        while(estado_boton):
            enviador.send('con_horario(0.01, 5)')
    else:
        messagebox.showwarning(title='Falta conectar', message='Primero debe conectarse a un dispositivo.')

########################################  ETIQUETAS ########################################
imagen = PhotoImage(file="fondo.png")
etiqueta1 = Label(marco1, image=imagen)
etiqueta1.pack()

etiqueta2 = Label(marco2, text="Movimiento Detallado")
etiqueta2.grid(row=0, column=0, columnspan=2, sticky='we')

etiqueta3 = Label(marco2, text="Movimiento Continuo")
etiqueta3.grid(row=2, column=0, columnspan=2, sticky='we')

etiqueta5 = Label(marco3, textvariable=etiqueta_conexion, width=30)
etiqueta5.grid(row=0, column=0, columnspan=3, sticky='we')

########################################  ENTRADAS  ########################################
# combo = ttk.Combobox(marco3, state='readonly', values=[f'COM{i}' for i in range(1, 100)], width=7)
# combo.grid(row=0, column=3, sticky='ns')
# combo.set('COM19')

########################################   BOTONES  ########################################
def codigo_conectar():
    conectar()
boton_conectar = Button(marco3, text="Conectar", command=codigo_conectar, cursor='hand1')
boton_conectar.grid(row=0, column=4, sticky='e')


def codigo_IR():
    global estado_boton
    if(estado_conexion):
        estado_boton = True
        enviador.send('con_horario(0.01, 5)')
        estado_boton = False
    else:
        messagebox.showwarning(title='Falta conectar', message='Primero debe conectarse a un dispositivo.')
boton_IR = Button(marco2, text='<', command=codigo_IR, cursor='hand1', width=10)
boton_IR.grid(row=1, column=0)

def codigo_IN(event):
    global estado_boton
    estado_boton = True
    _thread.start_new_thread(izquierda, ())
def codigo_IN_1(event):
    global estado_boton
    estado_boton = False
boton_IN = Button(marco2, text='<', cursor='hand1', width=10)
boton_IN.grid(row=3, column=0)
boton_IN.bind('<ButtonPress-1>', codigo_IN)
boton_IN.bind('<ButtonRelease-1>', codigo_IN_1)


def codigo_DR():
    global estado_boton
    if(estado_conexion):
        estado_boton = True
        enviador.send('pro_horario(0.01, 5)')
        estado_boton = False
    else:
        messagebox.showwarning(title='Falta conectar', message='Primero debe conectarse a un dispositivo.')
boton_DR = Button(marco2, text='>', command=codigo_DR, cursor='hand1', width=10)
boton_DR.grid(row=1, column=1)

def codigo_DN(event):
    global estado_boton
    estado_boton = True
    _thread.start_new_thread(derecha, ())
def codigo_DN_1(event):
    global estado_boton
    estado_boton = False
boton_DN = Button(marco2, text='>', cursor='hand1', width=10)
boton_DN.grid(row=3, column=1)
boton_DN.bind('<ButtonPress-1>', codigo_DN)
boton_DN.bind('<ButtonRelease-1>', codigo_DN_1)



raiz.mainloop()