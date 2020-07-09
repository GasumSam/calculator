from tkinter import *
from tkinter import ttk

normal_buttons = [
    {
        'text': '1',
        'col': 0,
        'row': 4
    },
    {
        'text': '2',
        'col': 1,
        'row': 4
    },
    {
        'text': '3',
        'col': 2,
        'row': 4
    },
    {
        'text': '+',
        'col': 3,
        'row': 4
    },
    {
        'text': '4',
        'col': 0,
        'row': 3
    },
    {
        'text': '5',
        'col': 1,
        'row': 3
    },
    {
        'text': '6',
        'col': 2,
        'row': 3
    },
    {
        'text': '-',
        'col': 3,
        'row': 3
    },
    {
        'text': '7',
        'col': 0,
        'row': 2
    },
    {
        'text': '8',
        'col': 1,
        'row': 2
    },
    {
        "text": '9',
        'col': 2,
        'row': 2
    },
    {
        'text': 'x',
        'col': 3,
        'row': 2
    },
    {
        'text': 'C',
        'col': 1,
        'row': 1
    },
    {
        'text': '+/-',
        'col': 2,
        'row': 1
    },
    {
        'text': '÷',
        'col': 3,
        'row': 1
    },
    {
        'text': '0',
        'col': 0,
        'row': 5,
        'W': 2
    },
    {
        'text': ',',
        'col': 2,
        'row': 5
    },
    {
        'text': '=',
        'col': 3,
        'row': 5
   
    }
]

roman_buttons = [
 {
        'text': '=',
        'col': 0,
        'row': 5,
        'W': 4
    },
    {
        'text': 'I',
        'col': 0,
        'row': 5
    },
    {
        'text': 'V',
        'col': 1,
        'row': 5
    },
    {
        'text': 'X',
        'col': 0,
        'row': 3
    },
    {
        'text': 'L',
        'col': 1,
        'row': 2
    },
    {
        'text': 'C',
        'col': 0,
        'row': 2
    },
    {
        'text': 'D',
        'col': 1,
        'row': 2
    },    
    {
        'text': 'M',
        'col': 2,
        'row': 2,
        'W': 3
    },
    {
        'text': 'AC',
        'col': 1,
        'row': 1,
        'W': 2
    },
    {
        'text': '÷',
        'col': 3,
        'row': 1
    },
    {
        'text': 'x',
        'col': 3,
        'row': 2
    },
    {
        'text': '-',
        'col': 3,
        'row': 3
    },
    {
        'text': '+',
        'col': 3,
        'row': 4
    }
]

def pinta(cls, valor):
    print(valor)
    return valor

class Controlator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=300)  #(self, parent, width=272, height=300) Podemos eliminar las medidas, ya que hemos especificado en MainApp fill=BOTH
        self.reset() #Evitamos crear los cuatro atributos 18 veces, una para cada botón. Ahora invocamos self.reset() cada vez

        self.display = Display(self)
        self.display.grid(column=0, row=0)

        self.keyboard = Keyboard(self, 'R')
        self.keyboard.grid(column=0, row=1)
        
        for properties in dbuttons:
            btn = CalcButton(self, properties['text'], self.set_operation, properties.get('W', 1), properties.get('H', 1))  #Self heredado es ttk.Frame(padre), #De CalcButton: (self, parent, value, command, width=1, heigth=1)
            btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get('W', 1), rowspan=properties.get('H', 1))  

    def reset(self): #Generamos la función para que sea invocada y no tener que poner los cuatro atributos 18 veces
        self.op1 = None        # 0 PUede ser un valor ambíguo, por lo que probamos NADA...PONEMOS EL OPERADOR A VACÍO
        self.op2 = None
        self.operation = ''
        self.dispValue = '0'
        self.signo_recien_pulsado = False 

    def to_float(self, valor):
        return float(valor.replace(',', '.'))

    def to_str(self, valor):
        return str(valor).replace('.', ',')

        #@classmethod
        #def pinta(cls, valor):
         #   print(valor)
          #  return valor

    def calculate(self):
        if self.operation == '+':
            return self.op1 + self.op2
        elif self.operation == '-':
            return self.op1 - self.op2
        elif self.operation == 'x':
            return self.op1 * self.op2
        elif self.operation == '÷':
            return self.op1 / self.op2

        return self.op2

    def set_operation(self, algo):
        if algo.isdigit():  # permite ir dibujando los números en el display y que se acumulen
            if self.dispValue == '0' or self.signo_recien_pulsado:
                self.op1 = self.to_float(self.dispValue)
                self.op2 = None
                self.dispValue = algo
            else:            
                self.dispValue += str(algo) #Acumulamos el valor en el display cada vez que pulsamos una tecla

        if algo == 'C':
            self.reset() #Ahorramos poner los cuatro atributos 18 veces invocando a la función que ya los contempla

        if algo == '+/-' and self.dispValue != '0':
            if self.dispValue[0] == '-':
                self.dispValue = self.dispValue[1:]
            else:
                self.dispValue = '-' + self.dispValue

        if algo == ',' and not ',' in self.dispValue:
            self.dispValue += str(algo)

        if algo == '+' or algo == '-' or algo == 'x' or algo == '÷':
            if self.op1 == None:
                self.op1 = self.to_float(self.dispValue)
                self.operation = algo 
            elif self.op2 == None:
                self.op2 = self.to_float(self.dispValue)
                res = self.calculate()
                self.dispValue = self.to_str(res)
                self.operation = algo 
            else:
                self.op1 = self.to_float(self.dispValue)
                self.op2 = None
                self.operation = algo
            self.signo_recien_pulsado = True 
        else:
            self.signo_recien_pulsado = False 

        if algo == '=':
            if self.op1 != None and self.op2 == None:
                self.op2 = self.to_float(self.dispValue)
                res = self.calculate()
                self.dispValue = self.to_str(res)

            elif self.op1 != None and self.op2 != None:
                self.op1 = self.to_float(self.dispValue)
                res = self.calculate()
                self.dispValue = self.to_str(res)

        self.display.paint(self.dispValue)

class Display(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=50)
        self.pack_propagate(0)
    
        self.value = '0' #Podemos situar value (sin self.) fuera de la función init (en la línea 120, por ejemplo)

        s = ttk.Style()  #Crea una instancia de un estilo
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 36', background='black', foreground='white')

        self.lbl = ttk.Label(self, text=self.value, anchor=E, style='my.TLabel') #E = East/Derecha
        self.lbl.pack(side=TOP, fill=BOTH, expand=True) #Los atributos son las variables globales de mi instancia

    def paint(self, algo):
        self.value = algo #Aquí pintamos en el display los valores de Self_Operations
        self.lbl.config(text=algo)

class Selector(ttk.Frame):
    def __init__(self, parent, status='N'):
        ttk.Frame.__init__(self, parent, width = 68, height = 50)
        self.status = status
        self.__value = StringVar()  #Asignamos variable de control a self.value
        self.__value.set(self.status)  #inicializo la variable self.value con el valor de self.status tras crear la variable de control StringVar

        radiob1 = ttk.Radiobutton(self, text='N', value='N', name='rbtn_normal', variable = self.__value, command=self.__click)
        radiob1.place(x=0, y=5)
        radiob2 = ttk.Radiobutton(self, text='R', value='R', name='rbtn_romano', variable = self.__value, command=self.__click)
        radiob2.place(x=0, y=30)

    def click(self):
        self.status = self.__value.get() 

class Keyboard(ttk.Frame):
    def __init__(self, parent, status='N'): 
        ttk.Frame.__init__(self, parent, height=250, width=272)
        self.__status = status
        self.listaBRomanos = []
        self.listaBNormales = []

        if self.__status == 'N':
            self.pintaNormal()
        else:
            self.pintaRomano()

    @property               #Transforma status (Atributo), en un atributo con personalidad
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, valor):   #Actúa como SETTER, un método que permite asignar un valor a la clase
        self.__status = valor
        if valor == 'N':
            self.pintaNormal()
        else:
            self.pintaRomano()

    def pintaNormal(self):
        if len(self.listaBNormales) == 0:
            for properties in normal_buttons:  
                btn = CalcButton(self, properties['text'], None, properties.get('W', 1), properties.get('H', 1))  #Self heredado es ttk.Frame(padre), #De CalcButton: (self, parent, value, command, width=1, heigth=1)
                self.listaBNormales.append((btn, properties))
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get('W', 1), rowspan=properties.get('H', 1))   
        else:
            for btn, properties in self.listaBNormales:
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get('W', 1), rowspan=properties.get('H', 1)) 
        for borra, properties in self.listaBNormales:
            borra.grid_forget()

    def pintaRomano(self):
        if len(self.listaBRomanos) == 0:
            for properties in roman_buttons:  #Heredamos de COntrolator
                btn = CalcButton(self, properties['text'], None, properties.get('W', 1), properties.get('H', 1))
                self.listaBNormales.append((btn, properties))
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get('W', 1), rowspan=properties.get('H', 1))  
        else:
            for btn, properties in self.listaBRomanos:
                btn.grid(column=properties['col'], row=properties['row'], columnspan=properties.get('W', 1), rowspan=properties.get('H', 1))

        for borra in self.listaBRomanos: #es lo mismo que arriba, pero para poder olvidar la tupla, si no especificamos ambos elementos, especificamos abajo borrar el elemento 002
            borra[0].grid_forget()

class CalcButton(ttk.Frame):
    def __init__(self, parent, value, command, width=1, heigth=1):
        ttk.Frame.__init__(self, parent, width=68*width, height=50*heigth)  #68 es 272/4
        self.pack_propagate(0)  #el pack_propagate(0) determina que el ancho se mantenga fijo

        btn = ttk.Button(self, text=value, command=lambda: command(value))    #creamos la instancia Button   #el valor del texto es value, heredado del __init__
        btn.pack(side=TOP, fill=BOTH, expand=True)  #Empaquetate arriba, rellena ambas dimensiones y expándete



