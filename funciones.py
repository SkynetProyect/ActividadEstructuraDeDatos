from StudentClass import Student


# Crear una lista de diccionarios donde cada diccionario contiene la información de un estudiante.

def crear_lista(_nombre: str, _edad:int, _lista: list):
    _diccionario = {_nombre: [_edad]}
    _lista.append(_diccionario)
    return _lista


# Usar un list comprehension para crear una lista de objetos de la clase Student a partir de la lista de diccionarios.


def list_student_dic(_lista: list):
    lista = [Student(i, _lista[i][0]) for i in _lista]
    return lista


# Usar otro list comprehension para filtrar los estudiantes, excluyendo los que tienen una nota promedio menor que un
# umbral dado.


def filtro_nota_nombre(_lista: list, promedio: float):
    filtrado = [i for i in _lista if i.average_grade() > promedio]
    return filtrado


# Usar un dictionary comprehension para crear un diccionario de estudiantes que tienen una nota promedio por encima
# de un umbral dado, con los nombres de los estudiantes como claves y el objeto Student como valor.


def diccionario_promedio(_lista: list, promedio: float):
    _filtrado = filtro_nota_nombre(_lista, promedio)
    diccionario_filtrado = {i.name: i for i in _filtrado}
    return diccionario_filtrado

""" Puntos a realizar

Generar llamadas y entradas para poder testear las funciones
Asegurar que los for si retornen claves y valores en vez de diccionarios
Hacer pruebas de funcionamiento con la info
"""