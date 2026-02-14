# Clase encargada de gestionar los productos

from modelos.producto import Producto


class Inventario:
    def __init__(self):
        # Lista donde se almacenan los productos
        self.productos = []

    def agregar_producto(self, producto):
        # Validar que el ID no esté repetido
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return

        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:

                if cantidad is not None:
                    p.set_cantidad(cantidad)

                if precio is not None:
                    p.set_precio(precio)

                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Búsqueda parcial por nombre
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
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for p in self.productos:
                print(p)
