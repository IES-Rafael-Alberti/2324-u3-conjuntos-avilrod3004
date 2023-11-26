'''
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

- Crea un conjunto pares que contenga los números pares del conjunto numeros.
- Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
- Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
'''
def buscar_pares(numeros: set) -> set:
    '''
    '''
    pares = set()

    for num in numeros:
        if num % 2 == 0:
            pares.add(num)

    return pares


def buscar_multiplos_de_tres(numeros: set) -> set:
    '''
    '''
    multiplos_de_tres = set()

    for num in numeros:
        if num % 3 == 0:
            multiplos_de_tres.add(num)

    return multiplos_de_tres


def main():
    # ENTRADA
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    # PROCESO
    pares = buscar_pares(numeros)
    multiplos_de_tres = buscar_multiplos_de_tres(numeros)
    pares_y_multiplos_de_tres = pares & multiplos_de_tres

    # PROCESO Y SALIDA
    print(f'Números pares => {pares}')
    print(f'Números múltiplos de tres => {multiplos_de_tres}')
    print(f'Intersección => {pares_y_multiplos_de_tres}')


if __name__ == '__main__':
    main()