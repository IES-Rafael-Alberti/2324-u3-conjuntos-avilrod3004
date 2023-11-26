'''
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]


1. Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
2. Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
3. Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
4. Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
'''

def main():
    # ENTRADA
    fruta1 = ['manzana', 'pera', 'naranje', 'plátano', 'uva']
    fruta2 = ['manzana', 'pera', 'durazno', 'sandía', 'uva']
    set_fruta1 = set(fruta1)
    set_fruta2 = set(fruta2)

    #PROCESO
    frutas_comunes = set_fruta1 & set_fruta2
    frutas_solo_en_frutas1 = set_fruta1 - set_fruta2
    frutas_solo_en_frutas2 = set_fruta2 - set_fruta1

    # SALIDA
    print(f'Frutas comunes => {frutas_comunes}')
    print(f'Frutas que están en frutas 1, pero no en frutas2 => {frutas_solo_en_frutas1}')
    print(f'Frutas que están en frutas2, pero no en frutas1 => {frutas_solo_en_frutas2}')


if __name__ == '__main__':
    main()