class Biblioteca:
    def __init__(self, titulo, autor, anpubli,codigo):
        self.titulo = titulo
        self.autor = autor
        self.anpubli = anpubli
        self.codigo = codigo
    def __str__(self):
        return f"Titulo{self.titulo}, Autor{self.autor}, Año de Publicación {self.anpubli}, Codigo {self.codigo}"
class Resgistrobiblioteca:
    def __init__(self):
        self.lista_libros = []

    def agregar(self):
        try:
            codigo = int(input("Digite el codigo de la libro: "))
            titulo = input("Ingresa el titulo del libro: ")
            autor = input("Ingresa el autor del libro: ")
            anpubli = input("Ingresa el año de publicación del libro: ")
        except ValueError:
            print("porfavor verifica lo ingresados")

class Usuarios:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
    def __str__(self):
        return f"Nombre{self.nombre}, Carnet{self.carnet}, Carrera{self.carrera}"

class Gestiones:
    def __init__(self, prestamo,devoluciones):
        self.prestamo = prestamo
        self.devoluciones = devoluciones
    def __str__(self):
        return f"libro prestado{self.prestamo}, devoluciones {self.devoluciones}"


