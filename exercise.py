lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]


def ordenar(lista_personas):
    """ El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
    return sorted([edades[3] for edades in lista_personas ])


def convertir_a_diccionario(lista_personas):
    """ Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad """
    diccionario = {}
    for dni,nombre,apellido,edad in lista_personas :
        diccionario[dni] = (nombre,apellido,edad)
    return diccionario


def devolver_edad(lista_personas, dni):
    """ Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    diccionario = convertir_a_diccionario(lista_personas)
    if dni in diccionario:
        return diccionario[dni][2]
    else:
        return "No se encontro ninguna persona con ese dni"


def eliminar_repetidos(lista_personas):
    """ El metodo debe devolver los elementos unicos """
    return list(set(lista_personas))


def separar_por_edad(lista_personas):
    """ Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    mayores_de_25 = []
    menores_de_25 = []
    for persona in lista_personas:
        if persona[3] >= 25:
            mayores_de_25.append(persona)
        else:
            menores_de_25.append(persona)
    return mayores_de_25,menores_de_25


def obtener_promedio(lista):
    """ Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    try:
        promedio = sum(lista) / len(lista)
    except ZeroDivisionError:
        return "No se puede calcular el promedio de una lista vacia"
    return promedio


def main():
    """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))

if __name__ == "__main__":
    main()