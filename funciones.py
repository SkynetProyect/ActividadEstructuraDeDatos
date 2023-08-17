from StudentClass import Student


# Crear una lista de diccionarios donde cada diccionario contiene la información de un estudiante.

def crear_lista(_objeto: Student, _lista: list):
    objeto = _objeto
    _diccionario = {objeto.name: [objeto.age, objeto.grades, objeto.average_grade()]}
    _lista.append(_diccionario)

# Usar un list comprehension para crear una lista de objetos de la clase Student a partir de la lista de diccionarios.


def list_student_dic(_lista: list):
    lista = [Student(i, _lista[i][0]) for i in _lista]
    return lista

# Usar otro list comprehension para filtrar los estudiantes, excluyendo los que tienen una nota promedio menor que un
# umbral dado.


def filtro_nota_nombre(_lista: list, promedio: float):
    filtrado = [i.name for i in _lista if i.average_grade() > promedio]
    return filtrado

# Usar un dictionary comprehension para crear un diccionario de estudiantes que tienen una nota promedio por encima
# de un umbral dado, con los nombres de los estudiantes como claves y el objeto Student como valor.


def diccionario_promedio(  ):
    pass