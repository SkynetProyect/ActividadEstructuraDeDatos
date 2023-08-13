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


lista: list[dict]
lista_objetos: list[Student]


def agregar_lista(diccionario: dict):
    lista.append(diccionario)


def diccionario_crear(estudiante: Student):
    diccionario: dict = {estudiante.name: {estudiante.age, estudiante.grades}}
    agregar_lista(diccionario)

