import tkinter as tk
from tkinter import messagebox
from config import variablesensible

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Simple")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variables
        self.expresion = ""
        self.entrada_texto = tk.StringVar()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Frame para la pantalla
        frame_pantalla = tk.Frame(self.root, bd=3, relief=tk.RIDGE)
        frame_pantalla.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)
        
        # Pantalla de resultados
        pantalla = tk.Entry(frame_pantalla, textvariable=self.entrada_texto, 
                           font=('Arial', 24), bd=5, insertwidth=4, 
                           width=14, justify='right', state='readonly')
        pantalla.pack(fill=tk.BOTH, padx=5, pady=5)
        
        # Frame para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Definir los botones
        botones = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        # Crear los botones
        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                if texto == '=':
                    boton = tk.Button(frame_botones, text=texto, 
                                    font=('Arial', 18, 'bold'),
                                    bg='#4CAF50', fg='white',
                                    command=self.calcular)
                elif texto == 'C':
                    boton = tk.Button(frame_botones, text=texto, 
                                    font=('Arial', 18, 'bold'),
                                    bg='#f44336', fg='white',
                                    command=self.limpiar)
                elif texto in ['+', '-', '*', '/']:
                    boton = tk.Button(frame_botones, text=texto, 
                                    font=('Arial', 18),
                                    bg='#FF9800', fg='white',
                                    command=lambda t=texto: self.agregar_a_expresion(t))
                else:
                    boton = tk.Button(frame_botones, text=texto, 
                                    font=('Arial', 18),
                                    bg='#2196F3', fg='white',
                                    command=lambda t=texto: self.agregar_a_expresion(t))
                
                boton.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
        
        # Configurar el peso de las filas y columnas para que los botones se expandan
        for i in range(4):
            frame_botones.grid_rowconfigure(i, weight=1)
            frame_botones.grid_columnconfigure(i, weight=1)
    
    def agregar_a_expresion(self, valor):
        """Agrega un valor a la expresión"""
        self.expresion += str(valor)
        self.entrada_texto.set(self.expresion)
    
    def calcular(self):
        """Calcula el resultado de la expresión"""
        try:
            if self.expresion == "":
                return
            
            # Evaluar la expresión
            resultado = str(eval(self.expresion))
            self.entrada_texto.set(resultado)
            self.expresion = resultado
            
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")
            self.limpiar()
        except Exception as e:
            messagebox.showerror("Error", "Expresión inválida")
            self.limpiar()
    
    def limpiar(self):
        """Limpia la pantalla y la expresión"""
        self.expresion = ""
        self.entrada_texto.set("")

def main():
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()
