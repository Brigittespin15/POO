import pickle

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
        else:
            print("Producto no encontrado")
    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.nombre == nombre:
                return producto
        return None

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

def guardar_inventario(inventario, archivo):
    with open(archivo, "wb") as f:
        pickle.dump(inventario.productos, f)

def cargar_inventario(archivo):
    try:
        with open(archivo, "rb") as f:
            productos = pickle.load(f)
            inventario = Inventario()
            for id, producto in productos.items():
                inventario.agregar_producto(producto)
            return inventario
    except FileNotFoundError:
        return Inventario()

def main():
    archivo = "inventario.dat"
    inventario = cargar_inventario(archivo)

    while True:
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar productos")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            id = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = input("Ingrese ID: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese ID: ")
            cantidad = input("Ingrese nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Ingrese nombre: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            guardar_inventario(inventario, archivo)
            break


if __name__ == "__main__":
    main()

