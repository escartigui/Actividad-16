class Biblioteca:
    def __init__(self, titulo, autor, anpubli,codigo):
        self.titulo = titulo
        self.autor = autor
        self.anpubli = anpubli
        self.codigo = codigo
    def mostrarlibros(self):
        return f"Titulo{self.titulo}, Autor{self.autor}, Año de Publicación {self.anpubli}, Codigo {self.codigo}"
class Resgistrobiblioteca:
    def __init__(self):
        self.lista_libros = []

    def agregar(self):
        try:
            while True:
             codigo = int(input("Digite el codigo de la libro: "))
             if codigo in self.lista_libros:
                    print("El libro ya existe")
             titulo = input("Digite el titulo del libro: ")
             autor = input("Digite el autor del libro: ")
             anpubli = input("Digite el año de publicación del libro: ")
             self.lista_libros.append(Biblioteca(titulo, autor, anpubli, codigo))
             print("Estudiante Agregado")
        except ValueError:
            print("porfavor verifica lo ingresados")

    def mostrar(self):
        if not self.lista_libros:
            print("No hay libros")
        else:
            print("Lista de libros: ")
            for i, lib in enumerate(self.lista_libros,start=1):
                print(f"{i}. {lib.mostrarlibros()}")

    def Eliminar(self):
        buscado = input("Ingrese el codigo del libro")
        for est in self.lista_libros:
            if est.codigo == buscado:
                self.lista_libros.remove(est)
                print("Se elimino")
                return
        print("No existe el libro")

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

registrolib = Resgistrobiblioteca()

