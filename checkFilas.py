def checkFilas(sudoku):
    for fila in sudoku:
        # Comparo la longitud de la lista con la longitud de la
        # lista(diccionario) sin duplicados SET(). Si la longitud es la misma
        # significa que no hay duplicados.
        if len(fila) != len(set(fila)):
            return False
    return True

# Casos test


def check_sudoku(sudoku):
    return checkFilas(sudoku)


if __name__ == '__main__':

    import casosTestSudoku

    for attr in sorted(casosTestSudoku.__dict__):
        # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
        # Asi podemos añadir todos los casos que queramos
        # en la unidad cassTestSudoku sin modificar este codigo
        if attr.startswith('__'):
            pass
            # Skip atributo
        else:
            print(attr, " => ", check_sudoku(casosTestSudoku.__dict__[attr]))
            # mismo codigo que getattr(module, attr)
            # es necesario añadir el espacio de nombres del modulo:
            # casosTestSudoku.irregular
