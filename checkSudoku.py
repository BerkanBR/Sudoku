from checkCuadrado import checkCuadrado
from checkNumeros import checkNumeros
from checkFilas import checkFilas
from checkColumnas import checkColumnas


def check_sudoku(sudoku):

    return checkCuadrado(sudoku) and checkNumeros(sudoku) \
        and checkFilas(sudoku) and checkColumnas(sudoku)


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
