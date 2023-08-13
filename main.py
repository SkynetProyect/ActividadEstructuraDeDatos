import statistics


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.grades: list[int] = []

    def add_grade(self, numero: int):
        self.grades.append(numero)

    def average_grade(self):
        return statistics.mean(self.grades)


lista: list[dict] = []
lista_objetos: list[Student]


def agregar_lista(diccionario: dict):
    lista.append(diccionario)


def diccionario_crear(estudiante: Student):
    diccionario: dict = {estudiante.name: [estudiante.age, estudiante.grades]}
    agregar_lista(diccionario)


def crear_lista_objetos(lista_e: list):  # recibe la lista de diccionarios y crea una lista de objetos
    nombre: str = ""
    edad: int = 0

    for i in lista_e:
        for j in lista_e[i]:
            nombre = lista_e[i][j]
            edad = lista_e[i][j][0]
        objeto: Student = Student(nombre, edad)
        lista_objetos.append(objeto)


def filtrar_estudiantes(lista_t: list, umbral: float):  # recibe una lista de objetos y los filtra en otra lista
    umbral: float = umbral
    lista_r: list = []
    for i in lista_t:
        if i.average_grade() >= umbral:
            lista_r.append(i)
    return lista_r


def diccionario_por_promedio(lista_t: list, umbral: float):
    lista_temporal: list = filtrar_estudiantes(lista_t, umbral)
    diccionario_temporal: dict = {str: Student}
    for i in lista_temporal:
        diccionario_temporal[i.name] = i
