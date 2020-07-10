import unittest
import tkinterTestCase
import calculator

from tkinter import *
from tkinter import ttk

class TestKeyboard(tkinterTestCase.TkTestCase):
    def setUp(self):
        self.k = calculator.Keyboard(self.root)
        self.k.pack()
        self.k.wait_visibility()

    def tearDown(self):
        self.k.update()
        self.k.destroy()

    def test_render_Ok(self):
        self.assertEqual(self.k.winfo_height(), 250)  #Aquí llegamos con el teclado self.k
        self.assertEqual(self.k.winfo_width(), 272)
        for btn in self.k.children.values():                               #self.k es el teclado  que testamos contamos su lista de botones
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(self.k.children), 18)          #Comprobamso a través de test los botones
        self.assertEqual(len(self.k.listaBNormales), 18)
        self.assertEqual(len(self.k.listaBRomanos), 0)


    def test_render_roman_Ok(self):
        teclado_romano = calculator.Keyboard(self.root, 'R')  #Instancia Keyboard como segunda variable teclado | Queremos crear un teclado romano desde CERO
        teclado_romano.pack()  #Este lo pinta
        teclado_romano.wait_visibility()  #Queremos tener nuestro teclado bien pintado, antes de pasar del set up al test, este método hace que la VISIBILIDAD DESTÁ COMPLETA
        
        self.assertEqual(teclado_romano.winfo_height(), 250)  #En vez de self.k hay que testear teclado_romano, el nuevo teclado que hemos creado | testeamos información de height
        self.assertEqual(teclado_romano.winfo_width(), 272)
        for btn in teclado_romano.children.values():                               #teclado_romano es el teclado
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(teclado_romano.children), 13)
        self.assertEqual(len(teclado_romano.listaBNormales), 0)
        self.assertEqual(len(teclado_romano.listaBRomanos), 13)


        teclado_romano.update()
        teclado_romano.destroy()

    def test_change_status_keyboard():
        self.assertEqual(self.k.status, 'N')
        self.k.status = 'R'   #Al asignar status, se va a la línea 322 de calculator
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(self.k.children), 31)
        self.assertEqual(len(self.k.listaBNormales), 18)
        self.assertEqual(len(self.k.listaBRomanos), 13)
        self.assertEqual(self.k.status, 'R')

if __name__ == '__main__':
    unittest.main()