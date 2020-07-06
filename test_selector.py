import unittest
import calculator

from tkinter import *
from tkinter import ttk

class TestDisplay(unittest.TestCase):
    def test_render_OK(self):
        root = Tk()
        root.wait_visibility()

        d = calculator.Display(root)
        d.pack()
        d.wait_visibility()   # Aguanta hasta que el widget se dibuje completamente

        self.assertEqual(d.winfo_height(), 50)
        self.assertEqual(d.winfo_width(), 272)
        self.assertEqual(d.value, '0')

        d.update()
        d.destroy()
        root.update()
        root.destroy()

    def test_paint_change_value(self):
        root = Tk()
        root.wait_visibility()

        d = calculator.Display(root)
        d.pack()
        d.wait_visibility()

        d.paint(20)
        self.assertEqual(d.value, 20)

        d.update()
        d.destroy()
        root.update()
        root.destroy()


if __name__ == '__main__':
    unittest.main()

