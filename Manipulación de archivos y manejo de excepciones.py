import os

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.inventario = self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                inventario = [linea.strip() for linea in file.readlines()]
            return inventario
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error al cargar inventario: {e}")
            return []

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.inventario:
                    file.write(producto + '\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("No tiene permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def agregar_producto(self, producto):
        self.inventario.append(producto)
        self.guardar_inventario()

    def actualizar_producto(self, indice, producto):
        try:
            self.inventario[indice] = producto
            self.inventario[indice] = producto
            self.guardar_inventario()
        except IndexError:
            print("Índice inválido.")

    def eliminar_producto(self, indice):
        try:
            del self.inventario[indice]
            self.guardar_inventario()
        except IndexError:
            print("Índice inválido.")


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
            producto = input("Ingrese el producto: ")
            inventario.agregar_producto(producto)
        elif opcion == '2':
            indice = int(input("Ingrese el índice del producto: "))
            producto = input("Ingrese el nuevo producto: ")
            inventario.actualizar_producto(indice, producto)
        elif opcion == '3':
            indice = int(input("Ingrese el índice del producto: "))
            inventario.eliminar_producto(indice)
        elif opcion == '4':
            print("Inventario:")
            for i, producto in enumerate(inventario.inventario):
                print(f"{i+1}. {producto}")
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
