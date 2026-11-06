from matriz import MatrizFloat

from utils import *

def main():
    opciones = ["1. Construir matriz 1D",
                "2. Construir matriz 2D",
                "3. Construir matriz identidad",
                "4. Introducir matriz",
                "5. Mostrar matriz",
                "6. Operaciones con matrices",
                "7. Terminar"]
    sub_menu = ["1. Sumar matrices",
                "2. Restar matrices",
                "3. Volver al menú principal"]
    op = 0
    matriz_actual = MatrizFloat()
    while op!=7:
        op = crear_menu(opciones)
        match op:
            case 1:
                print("CONSTRUIR MATRIZ 1D")
                nEl = leer_int("Introduzca el numero de elementos de la matriz: ")
                matriz_actual = matriz_actual.crear_matriz1D(nEl)
            case 2:
                print("CONSTRUIR MATRIZ 2D")
                nFil = leer_int("Introduzca el numero de filas de la matriz: ")
                nCol = leer_int("Introduzca el numero de columnas de la matriz: ")
                matriz_actual = matriz_actual.crear_matriz2D(nFil, nCol)
            case 3:
                print("CONSTRUIR MATRIZ IDENTIDAD")
                tam = leer_int("Introduzca el tamaño de la matriz: ")
                matriz_actual = matriz_actual.matriz_identidad(tam)
            case 4:
                print("INTRODUCIR MATRIZ")
                matriz_actual = matriz_actual.introducir()
            case 5:
                print("MOSTRAR MATRIZ")
                matriz_actual.mostrar()
            case 6:
                print("OPERACIONES CON MATRICES")
                sub_op = 0
                while sub_op!=3:
                    sub_op = crear_menu(sub_menu)
                    match sub_op:
                        case 1:
                            print("SUMA DE MATRICES")
                            nFil = leer_int("Introduzca el numero de filas de la segunda matriz: ")
                            nCol = leer_int("Introduzca el numero de columnas de la segunda matriz: ")
                            m_sum = MatrizFloat.crear_matriz2D(nFil, nCol)
                            m_sum.introducir()

                            resultado = matriz_actual.sumar_matrices(m_sum)
                            if resultado is not None:
                                print("La suma de las dos matrices es: ")
                                resultado.mostrar()
                            

                        case 2:
                            print("RESTA DE MATRICES")
                            nFil = leer_int("Introduzca el numero de filas de la segunda matriz: ")
                            nCol = leer_int("Introduzca el numero de columnas de la segunda matriz: ")
                            m_res = MatrizFloat.crear_matriz2D(nFil, nCol)
                            m_res.introducir()

                            resultado = matriz_actual.restar_matrices(m_res)
                            if resultado is not None:
                                print("La resta de las dos matrices es: ")
                                resultado.mostrar()
                        case 3:
                            print("Volviendo al programa original")
                
            case 7:
                print("Programa terminado")
if __name__ == "__main__":
    main()