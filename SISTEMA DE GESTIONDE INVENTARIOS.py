# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio
# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not self.buscar_producto_id(producto.get_id()):
            self.productos.append(producto)
        else:
            print("El ID del producto ya existe.")

    def eliminar_producto(self, id):
        producto = self.buscar_producto_id(id)
        if producto:
            self.productos.remove(producto)
        else:
            print("No se encontró el producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_producto_id(id)
        if producto:
            if cantidad:
                producto.set_cantidad(cantidad)
            if precio:
                producto.set_precio(precio)
        else:
            print("No se encontró el producto con ese ID.")

    def buscar_producto_nombre(self, nombre):
        return [producto for producto in self.productos if producto.get_nombre().lower() == nombre.lower()]
    def mostrar_productos(self):
        for producto in self.productos:
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

    def buscar_producto_id(self, id):
        return next((producto for producto in self.productos if producto.get_id() == id), None)


# Interfaz de Usuario en la Consola
def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            precio = float(input("Ingrese el nuevo precio del producto: "))
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_producto_nombre(nombre)
            if productos:
                for producto in productos:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
