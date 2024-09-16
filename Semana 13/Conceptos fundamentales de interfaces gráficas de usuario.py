#Diseño de la Interfaz

#La ventana principal tendrá un título descriptivo y contendrá los siguientes componentes:

#- Etiqueta (Label) con el texto "Agregar información"
#- Campo de texto (Entry) para ingresar la información
#- Botón (Button) "Agregar" para agregar la información a la lista
#- Lista (Listbox) para mostrar la información agregada
#- Botón (Button) "Limpiar" para borrar la información ingresada o seleccionada


import tkinter as tk

class AplicacionGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación GUI")

        # Etiqueta y campo de texto
        self.etiqueta = tk.Label(self.ventana, text="Agregar información")
        self.etiqueta.pack()
        self.campo_texto = tk.Entry(self.ventana)
        self.campo_texto.pack()

        # Botón Agregar
        self.boton_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_informacion)
        self.boton_agregar.pack()

        # Lista
        self.lista = tk.Listbox(self.ventana)
        self.lista.pack()

        # Botón Limpiar
        self.boton_limpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.pack()

    def agregar_informacion(self):
        informacion = self.campo_texto.get()
        self.lista.insert(tk.END, informacion)
        self.campo_texto.delete(0, tk.END)

    def limpiar(self):
        self.lista.delete(0, tk.END)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = AplicacionGUI()
    app.run()
