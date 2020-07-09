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
        self.assertEqual(self.k.winfo_height(), 250)
        self.assertEqual(self.k.winfo_width(), 272)
        for btn in self.k.children.values():                               #self.k es el teclado
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(self.k.children), 18)

    def test_render_roman_Ok(self):
        teclado_romano = calculator.Keyboard(self.root, 'R')  #Instancia Keyboard
        teclado_romano.pack()  #Este lo pinta
        teclado_romano.wait_visibility()  #Queremos tener nuestro teclado bien pintado, antes de pasar del set up al test, este método hace que la VISIBILIDAD DESTÁ COMPLETA
        
        self.assertEqual(teclado_romano.winfo_height(), 250)  #En vez de self.k hay que testear teclado_romano
        self.assertEqual(teclado_romano.winfo_width(), 272)
        for btn in teclado_romano.children.values():                               #self.k es el teclado
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(teclado_romano.children), 13)

        teclado_romano.update()
        teclado_romano.destroy()

    def test_change_status_keyboard():
        self.assertEqual(self.k.status, 'N')
        self.k.status = 'R'   #Al asignar status, se va a la línea 322 de calculator
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(self.k.children), 13)
        self.assertEqual(self.k.status, 'R')


if __name__ == '__main__':
    unittest.main()