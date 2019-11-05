def checkNumeros(sudoku):
    # Hacemos un if, ya que se considera que una lista vacía no es un número
    if sudoku == [[]]:
        return False
    else:
        for fila in sudoku:
            for numero in fila:
                if not isinstance(numero, int):
                    return False
        return True

# Importo los test para comprobar la funcionalidad de Números


def check_sudoku(sudoku):
    return checkNumeros(sudoku)


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
