'''
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

    Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
    Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
    Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
    Mostrar si todos los nombres de primaria están incluidos en secundaria.
'''

def pedir_nombre(msj) -> str:
    '''Pedir nombre al usuario por consola

    Args:
        msj (str): mensaje para el input

    Return:
        str: nombre dado por el usuario
    '''
    nombre = input(msj)

    while nombre.isdecimal() == True:
        print('**ERROR** - NO INTRODUZCAS VALORES NÚMERICOS')
        nombre = input(msj)

    return nombre.title()


def main():
    # ENTRADA

    # nombres de los alumnos de primaria
    primaria = []
    nombre = ''
    while nombre != 'X':
        nombre = pedir_nombre('Introduce un nombre de un alumno de primaria o una x para terminar: ')
        if nombre != 'X':
            primaria.append(nombre)

    print('\n')

    # nombres de los alumnos de secundaria
    secundaria = []
    nombre = ''
    while nombre != 'X':
        nombre = pedir_nombre('Introduce un nombre de un alumno de secundaria o una x para terminar: ')
        if nombre != 'X':
            secundaria.append(nombre)

    # PROCESO y SALIDA

    # Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
    print('\nTodos los nombres sin que se repitan:')
    print(set(primaria) | set(secundaria))

    # Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
    print('\nLos nombres que se repiten entre primaria y secundaria')
    print(set(primaria) & set(secundaria))

    # Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
    print('\nNombre de primaria que no se repiten en secundaria')
    print(set(primaria) - set(secundaria))

    # Mostrar si todos los nombres de primaria están incluidos en secundaria.
    print('\nSi los nombres de primaria se incluyen en secundaria')
    if set(primaria) <= set(secundaria) == True:
        print('Todos los nombres de primaria están incluidos en secundaria')
    else:
        print('Todos los nombre de primaria no están incluidos en secundaria')


if __name__ == '__main__':
    main()