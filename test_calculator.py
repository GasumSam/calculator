from tkinter import *
from tkinter import ttk
from calculator import *

root = Tk()

def mifuncion(valor):
    return(valor)

mi_boton = calculator.CalcButton(root, 'Hola', mifuncion)


controlator = calculator.Controlator(root)

controlator.event_generate('<Key-7>')
assertEqual(r, '7')

...

<test>

    r = mi_boton.event_generate('<Button-1>')
    assertEqual(r, 'Hola')