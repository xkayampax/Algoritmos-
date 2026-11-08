import datetime

class Libro:
    def __init__(self, codigo, titulo, autor, año_publicacion, disponible=True):
        self.codigo = codigo 
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
        self.año_publicacion = año_publicacion

class Socio:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.prestamos_activos = 0 

class Prestamo:
    def __init__(self, libro, socio):
        self.libro = libro
        self.socio = socio
        self.fecha_prestamo = None
        self.fecha_devolucion = None

    def esta_disponible(self):
        return self.libro.disponible

    def prestar(self):
        if not self.esta_disponible():
            print(f"Error: El libro '{self.libro.titulo}' no está disponible.")
            return False
            
        if self.socio.prestamos_activos >= 3:
            print(f"Error: El socio {self.socio.nombre} ya alcanzó el máximo de 3 préstamos activos.")
            return False

        self.fecha_prestamo = datetime.date.today()
        self.libro.disponible = False
        self.socio.prestamos_activos += 1
        print(f"Préstamo exitoso: '{self.libro.titulo}' entregado a {self.socio.nombre}.")
        return True

    def devolver(self):
        if self.fecha_prestamo is not None and self.fecha_devolucion is None:
            self.fecha_devolucion = datetime.date.today()
            self.libro.disponible = True
            self.socio.prestamos_activos -= 1
            print(f"Devolución exitosa: '{self.libro.titulo}' devuelto por {self.socio.nombre}.")
        else:
            print("Error: Este préstamo ya fue devuelto o nunca se realizó.")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.socios = []
        self.historial_prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro registrado: {libro.titulo}")

    def registrar_socio(self, socio):
        self.socios.append(socio)
        print(f"Socio registrado: {socio.nombre}")

    def realizar_prestamo(self, libro, socio):
        nuevo_prestamo = Prestamo(libro, socio)
        if nuevo_prestamo.prestar():
            self.historial_prestamos.append(nuevo_prestamo)
        return nuevo_prestamo

if __name__ == "__main__":

    mi_biblioteca = Biblioteca()

    libro1 = Libro("L01", "El Señor de los Anillos", "J.R.R. Tolkien", 1954)
    libro2 = Libro("L02", "Cien Años de Soledad", "Gabriel García Márquez", 1967)
    libro3 = Libro("L03", "1984", "George Orwell", 1949)
    libro4 = Libro("L04", "Don Quijote", "Miguel de Cervantes", 1605)
    
    mi_biblioteca.registrar_libro(libro1)
    mi_biblioteca.registrar_libro(libro2)
    mi_biblioteca.registrar_libro(libro3)
    mi_biblioteca.registrar_libro(libro4)

    socio1 = Socio("S01", "Ana Pérez")
    mi_biblioteca.registrar_socio(socio1)

    print("\n--- Iniciando Préstamos ---")

    p1 = mi_biblioteca.realizar_prestamo(libro1, socio1)
    p2 = mi_biblioteca.realizar_prestamo(libro2, socio1)
    p3 = mi_biblioteca.realizar_prestamo(libro3, socio1)

    p4 = mi_biblioteca.realizar_prestamo(libro4, socio1)

    print("\n--- Devolviendo un libro ---")
    p1.devolver()

    print("\n--- Intentando de nuevo el 4to libro ---")

    p4 = mi_biblioteca.realizar_prestamo(libro4, socio1)