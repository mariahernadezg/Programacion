from matriz import MatrizFloat
#Funciones para implementar en prácticas futuras
def leer_int(mensaje: str = "Introduce un número entero: ")->int:     
    """     
    Función auxiliar que lee un número entero del teclado.     
    Si se introduce un valor no válido, se solicita de nuevo.
        Parámetros:         
            mensaje # El mensaje que se muestra al usuario                    
                    # solicitando la entrada (str). Por defecto                           
                    # "Introduce un número entero: "      
        Devuelve:         
            int: El valor entero introducido por el usuario.
    """
    num_val = False
    while not num_val:
        try:
            num = int(input(mensaje))
            num_val = True
            return num
        except ValueError:
            print("El valor introducido no es valido")

def leer_float(mensaje: str = "Introduce un número decimal: ")->float:
    """     
    Función auxiliar que lee un número decimal del teclado.     
    Si se introduce un valor no válido, se solicita de nuevo.
        Parámetros:         
            mensaje # El mensaje que se muestra al usuario                    
                    # solicitando la entrada (str). Por defecto                           
                    # "Introduce un número decimal: "      
        Devuelve:         
            El valor entero introducido por el usuario (float)
    """
    num_val = False
    while not num_val:
        try:
            num = float(input(mensaje))
            num_val = True
            return num
        except ValueError:
            print("El valor introducido no es valido")

def crear_menu(opciones_menu: list)->int:
    """ 
    Función que muestra un menú de opciones y solicita al usuario   
    que seleccione una opción válida. 
    Parámetros: 
        opciones_menu   # lista de opciones a mostrar en el menú  
                        # (list) 
    Devuelve: 
        El número de opción seleccionado por el usuario (int) 
    """
    print("MENÚ DE OPCIONES")
    for i in range(len(opciones_menu)):
        print(f"Opción {i+1}: {opciones_menu[i]}")
    total = len(opciones_menu)
    op = ""
    while True:
        op = leer_int(f"Seleccione una opción (1-{total}): ")
        if 1<=op<=total:
            return op
        else:
            print(f"Error. Debe introducir un numero entre 1 y {total}")