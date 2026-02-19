# Clase encargada de gestionar los productos
# Esta versión incluye almacenamiento en archivo
# y manejo de excepciones para lectura y escritura.

from modelos.producto import Producto


class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.

        Inicializa la lista de productos en memoria,
        define el archivo donde se almacenará la información
        y carga los datos existentes si el archivo ya existe.
        """
        self.productos = []
        self.archivo = "inventario.txt"
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """
        Carga los productos desde el archivo inventario.txt.

        Si el archivo no existe, se crea automáticamente.
        Se manejan excepciones para evitar que el programa
        se detenga por errores relacionados con archivos.
        """
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(";")

                    # Validar que la línea tenga el formato correcto
                    if len(datos) == 4:
                        id_producto = int(datos[0])
                        nombre = datos[1]
                        cantidad = int(datos[2])
                        precio = float(datos[3])

                        producto = Producto(id_producto, nombre, cantidad, precio)
                        self.productos.append(producto)

        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo.")
            open(self.archivo, "w").close()

        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

    def guardar_en_archivo(self):
        """
        Guarda todos los productos actuales en el archivo.

        El archivo se sobrescribe completamente cada vez
        que se realiza un cambio para mantener consistencia.
        """
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    linea = f"{p.get_id()};{p.get_nombre()};{p.get_cantidad()};{p.get_precio()}\n"
                    f.write(linea)

            print("Cambios guardados correctamente en el archivo.")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.

        Valida que el ID no esté repetido.
        Si se agrega correctamente, se guarda en el archivo.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario según su ID.
        Si se elimina correctamente, se actualiza el archivo.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto.

        Solo se modifican los valores que se proporcionen.
        Después de actualizar, se guardan los cambios.
        """
        for p in self.productos:
            if p.get_id() == id_producto:

                if cantidad is not None:
                    p.set_cantidad(cantidad)

                if precio is not None:
                    p.set_precio(precio)

                self.guardar_en_archivo()
                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca productos por coincidencia parcial en el nombre.
        """
        encontrados = [
            p for p in self.productos
            if nombre.lower() in p.get_nombre().lower()
        ]

        if encontrados:
            print("\nProductos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos registrados en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for p in self.productos:
                print(p)