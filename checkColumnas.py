def checkColumnas(sudoku):

    numeroDeFilas = len(sudoku)

    indexFilaActual = 0

    for fila in sudoku:

        for numero in fila:
            indexFilaSiguiente = indexFilaActual + 1

            while indexFilaSiguiente < numeroDeFilas:

                try:
                    posicionNumeroFilaSiguiente = sudoku[
                        indexFilaSiguiente].index(numero)

                except ValueError:
                    return False

                else:
                    if posicionNumeroFilaSiguiente == fila.index(numero):
                        return False
                    else:
                        indexFilaSiguiente += 1
        indexFilaActual += 1
    return True


# Casos test

def check_sudoku(sudoku):
    return checkColumnas(sudoku)


if __name__ == '__main__':

    import casosTestSudoku

    for attr in sorted(casosTestSudoku.__dict__):
        # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
        # Asi podemos añadir todos los casos que queramos
        #  en la unidad cassTestSudoku sin modificar este codigo
        if attr.startswith('__'):
            pass
            # Skip atributo
        else:
            print(attr, " => ", checkColumnas(casosTestSudoku.__dict__[attr]))
            # mismo codigo que getattr(module, attr)
            # es necesario añadir el espacio de nombres del modulo:
            # casosTestSudoku.irregular
