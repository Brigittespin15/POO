import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.inventario = self.cargar_inventario()

    def cargar_inventario(self):
        inventario = {}
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        id, nombre = linea.strip().split('|', 1)
                        inventario[id] = nombre
            return inventario
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error al cargar inventario: {e}")
            return {}

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for id, nombre in self.inventario.items():
                    file.write(f"{id}|{nombre}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("No tiene permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def agregar_producto(self, id, nombre):
        self.inventario[id] = nombre
        self.guardar_inventario()

    def actualizar_producto(self, id, nombre):
        if id in self.inventario:
            self.inventario[id] = nombre
            self.guardar_inventario()
        else:
            print("ID de producto no encontrado.")

    def eliminar_producto(self, id):
        if id in self.inventario:
            del self.inventario[id]
            self.guardar_inventario()
        else:
            print("ID de producto no encontrado.")

def main():
    inventario = Inventario()
    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            inventario.agregar_producto(id, nombre)
        elif opcion == '2':
            id = input("Ingrese el ID del producto a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del producto: ")
            inventario.actualizar_producto(id, nombre)
        elif opcion == '3':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '4':
            print("Inventario:")
            for id, nombre in inventario.inventario.items():
                print(f"ID: {id}, Nombre: {nombre}")
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")


main()
