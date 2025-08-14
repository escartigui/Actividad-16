class Biblioteca:
    def __init__(self, titulo, autor, anpubli,codigo):
        self.titulo = titulo
        self.autor = autor
        self.anpubli = anpubli
        self.codigo = codigo
    def __str__(self):
        return f"Titulo{self.titulo}, Autor{self.autor}, Año de Publicación {self.anpubli}, Codigo {self.codigo}"

class Registrous:
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


