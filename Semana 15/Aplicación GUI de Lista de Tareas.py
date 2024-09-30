'''Desarrollar una aplicación GUI simple para gestionar una lista de tareas, permitiendo al usuario añadir nuevas tareas, marcarlas como completadas y eliminarlas. La aplicación deberá responder adecuadamente a los eventos del usuario, como clics del ratón y pulsaciones del teclado.'''
import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.config(bg="#F0F8FF")  # Fondo en color azul claro

        # Lista de Tareas
        self.tasks = []

        # Campo de entrada con borde
        self.entry = tk.Entry(root, width=40, borderwidth=3, relief="ridge")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Añadir tarea al presionar Enter
        self.entry.config(fg="black", bg="#E6E6FA")  # Texto negro, fondo lavanda

        # Botones
        self.add_button = tk.Button(root, text="Agregar Tarea", command=self.add_task, bg="#00FA9A", fg="black",
                                    font=("Helvetica", 12, "bold"))
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task, bg="#FFD700",
                                         fg="black", font=("Helvetica", 12, "bold"))
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task, bg="#FF6347", fg="black",
                                       font=("Helvetica", 12, "bold"))
        self.delete_button.pack(pady=5)

        # Lista de Tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, bg="#FFFACD", fg="black",
                                       font=("Helvetica", 10))
        self.task_listbox.pack(pady=5)

    # Función para agregar una nueva tarea a la lista
    def add_task(self, event=None):
        task = self.entry.get().strip()  # Obtener el texto del campo de entrada
        if task:
            self.tasks.append(task)  # Añadir tarea a la lista interna
            self.update_task_listbox()  # Actualizar visualmente la lista
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada después de agregar
        else:
            # Mostrar advertencia si el campo está vacío
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    # Función para actualizar la lista de tareas en la interfaz
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Limpiar la lista actual
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Insertar las tareas actualizadas

    # Función para marcar una tarea como completada
    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice seleccionado
            completed_task = self.tasks[selected_index] + " (Completada)"  # Añadir texto "Completada"
            self.tasks[selected_index] = completed_task  # Actualizar el estado de la tarea
            self.update_task_listbox()  # Refrescar la lista de tareas
        except IndexError:
            # Mostrar advertencia si no se selecciona ninguna tarea
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    # Función para eliminar una tarea seleccionada
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener el índice de la tarea seleccionada
            del self.tasks[selected_index]  # Eliminar la tarea de la lista interna
            self.update_task_listbox()  # Actualizar visualmente la lista
        except IndexError:
            # Mostrar advertencia si no se selecciona ninguna tarea
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = TaskManager(root)  # Instanciar el gestor de tareas
    root.mainloop()
    # Iniciar el bucle principal de Tkinter