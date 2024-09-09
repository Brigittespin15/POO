class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Inicializa los atributos del libro: título, autor, categoría e ISBN.
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        # Devuelve una representación en formato cadena del libro.
        return f"{self.titulo} por {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        # Inicializa los atributos del usuario: nombre e ID.
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar los libros que tiene prestados el usuario.
        self.libros_prestados = []

    def prestar_libro(self, libro):
        # Agrega el libro a la lista de libros prestados.
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        # Si el libro está prestado al usuario, lo quita de la lista de libros prestados.
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        # Devuelve una representación en cadena del usuario, incluyendo los libros prestados.
        libros = ", ".join([libro.titulo for libro in self.libros_prestados]) or "Ninguno"
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {libros}"


class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar los libros, con el ISBN como clave.
        self.libros = {}
        # Conjunto para garantizar que los ID de los usuarios sean únicos.
        self.usuarios = set()
        # Diccionario para almacenar objetos Usuario, con el ID del usuario como clave.
        self.usuarios_objetos = {}

    def añadir_libro(self, libro):
        # Añade un libro al diccionario si el ISBN no está registrado.
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
        else:
            print("Este ISBN ya está registrado.")

    def quitar_libro(self, isbn):
        # Elimina un libro del diccionario si existe.
        if isbn in self.libros:
            del self.libros[isbn]
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        # Añade un usuario si su ID no está registrado.
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.usuarios_objetos[usuario.id_usuario] = usuario
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        # Elimina a un usuario registrado de la biblioteca.
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_objetos[id_usuario]
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, isbn, id_usuario):
        # Presta un libro si el usuario está registrado y el libro está disponible.
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios_objetos[id_usuario]
            usuario.prestar_libro(libro)
            del self.libros[isbn]  # El libro se elimina de la lista de disponibles.
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, id_usuario):
        # El usuario devuelve un libro prestado, se vuelve a añadir a la biblioteca.
        if id_usuario in self.usuarios:
            usuario = self.usuarios_objetos[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    self.libros[isbn] = libro  # El libro vuelve a estar disponible.
                    usuario.devolver_libro(libro)
                    break
            else:
                print("El libro no está prestado a este usuario.")
        else:
            print("Usuario no registrado.")

    def buscar_libro(self, criterio, valor):
        # Busca libros que coincidan con el criterio especificado (título, autor o categoría).
        resultados = []
        for libro in self.libros.values():
            if getattr(libro, criterio) == valor:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        # Devuelve la lista de libros prestados de un usuario.
        if id_usuario in self.usuarios:
            usuario = self.usuarios_objetos[id_usuario]
            return usuario.libros_prestados
        return []

    def mostrar_estado(self):
        # Muestra los libros disponibles y los usuarios registrados.
        print("\n--- Estado actual de la biblioteca ---")
        if self.libros:
            print("\nLibros disponibles:")
            for libro in self.libros.values():
                print(libro)
        else:
            print("No hay libros disponibles.")

        if self.usuarios_objetos:
            print("\nUsuarios registrados:")
            for usuario in self.usuarios_objetos.values():
                print(usuario)
        else:
            print("No hay usuarios registrados.")

    def __str__(self):
        # Representación en cadena de los libros disponibles en la biblioteca.
        libros = ", ".join([str(libro) for libro in self.libros.values()])
        return f"Libros en biblioteca: {libros}"


def mostrar_menu():
    # Imprime el menú y pide al usuario que seleccione una opción.
    print("\n--- Menú Biblioteca ---")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Mostrar estado")
    print("10. Salir")
    return input("Selecciona una opción: ")


def main():
    # Función principal que controla el sistema de biblioteca.
    biblioteca = Biblioteca()

    while True:
        # Bucle para mostrar el menú y ejecutar las opciones seleccionadas.
        opcion = mostrar_menu()

        if opcion == "1":
            # Añadir un libro a la biblioteca.
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)
            print("Libro añadido con éxito.")

        elif opcion == "2":
            # Quitar un libro de la biblioteca.
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            # Registrar un nuevo usuario.
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
            print("Usuario registrado con éxito.")

        elif opcion == "4":
            # Dar de baja a un usuario.
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
            print("Usuario dado de baja con éxito.")

        elif opcion == "5":
            # Prestar un libro.
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario que recibe el libro: ")
            biblioteca.prestar_libro(isbn, id_usuario)
            print("Libro prestado con éxito.")

        elif opcion == "6":
            # Devolver un libro.
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario que devuelve el libro: ")
            biblioteca.devolver_libro(isbn, id_usuario)
            print("Libro devuelto con éxito.")

        elif opcion == "7":
            # Buscar un libro por título, autor o categoría.
            criterio = input("Criterio de búsqueda (titulo/autor/categoria): ")
            valor = input(f"Valor del criterio ({criterio}): ")
            if criterio in ['titulo', 'autor', 'categoria']:
                resultados = biblioteca.buscar_libro(criterio, valor)
                if resultados:
                    print("\n--- Libros encontrados ---")
                    for libro in resultados:
                        print(libro)
                else:
                    print(f"No se encontraron libros con {criterio}: {valor}")
            else:
                print("Criterio inválido. Debe ser 'titulo', 'autor' o 'categoria'.")

        elif opcion == "8":
            # Listar libros prestados a un usuario.
            id_usuario = input("ID del usuario para listar libros prestados: ")
            libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
            if libros_prestados:
                print(f"\nLibros prestados a {id_usuario}:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print(f"No hay libros prestados para el usuario con ID {id_usuario}")

        elif opcion == "9":
            # Mostrar el estado actual de la biblioteca.
            biblioteca.mostrar_estado()

        elif opcion == "10":
            # Salir del programa.
            print("Saliendo del programa.")
            break

        else:
            # Opción inválida.
            print("Opción inválida. Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    main()