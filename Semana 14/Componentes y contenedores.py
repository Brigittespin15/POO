import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_entry = ttk.Frame(self.root)
        self.frame_entry.pack(pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(self.frame_entry, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entry, width=12, background='darkblue', foreground='white',
                                     borderwidth=2)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.frame_entry, text="Hora (HH:MM):").grid(row=1, column=0)
        self.hora_entry = ttk.Entry(self.frame_entry)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.frame_entry, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = ttk.Entry(self.frame_entry)
        self.desc_entry.grid(row=2, column=1)

        # Botones para acciones
        self.boton_agregar = ttk.Button(self.frame_entry, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.grid(row=3, column=0, pady=10)

        self.boton_eliminar = ttk.Button(self.frame_entry, text="Eliminar Evento Seleccionado",
                                         command=self.eliminar_evento)
        self.boton_eliminar.grid(row=3, column=1, pady=10)

        self.boton_salir = ttk.Button(self.frame_entry, text="Salir", command=self.root.quit)
        self.boton_salir.grid(row=3, column=2, pady=10)

    def agregar_evento(self):
        """ Agrega un evento a la lista. """
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.limpiar_campos()

    def eliminar_evento(self):
        """ Elimina el evento seleccionado. """
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
        if confirmacion:
            self.tree.delete(seleccion)

    def limpiar_campos(self):
        """ Limpia los campos de entrada. """
        self.fecha_entry.set_date("")
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)


if _name_ == "_main_":  # Fixed the condition
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()