class Time:
    """ Clase que representa una hora en formato AM/PM o 24 horas. 
    Atributos de clase: TIME_FORMATS    # p. ej.: "AM", "PM", "24 HOURS" 
    time_count = 0  # Cuenta el número de objetos Time creados 
    Atributos: 
    # Los atributos deben ser privados y exponerse mediante  
    # property 
    hours       # Guarda las horas 
                # (1 a 12 en AM/PM, 0 a 23 en 24 HOURS) 
    minutes     # Guarda los minutos (0 a 59) 
    seconds     # Guarda los segundos (0 a 59) 
    time_format # Guarda el formato: "AM", "PM" o "24 HOURS"  
    """
    TIME_FORMATS = ("AM", "PM", "24 HOURS") #tupla para que sea inmutable
    time_count = 0

    # Método de instancia: Inicializa los atributos del objeto concreto.
    def __init__(self):
        """
        Incializa los atributos a 0, __time_format a una cadena vacía.
        Es el único método que se le pasa parámetros como ejemplo
        """
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.__time_format = ""
        Time.time_count += 1

    # Propiedades (métodos de instancia): Permiten el acceso de lectura a los atributos privados.
    @property
    def hours(self) -> int:
        """Devuelve el valor de las horas."""
        return self.__hours

    @property
    def minutes(self) -> int:
        """Devuelve el valor de los minutos."""
        return self.__minutes

    @property
    def seconds(self) -> int:
        """Devuelve el valor de los segundos."""
        return self.__seconds

    @property
    def time_format(self) -> str:
        """Devuelve el formato de hora."""
        return self.__time_format

    # Método de instancia (privado): Opera sobre los atributos privados de la instancia.
    def __assign_format(self, time_format: str)->bool:
        """         
        Comprueba que time_format tiene un valor correcto y lo          
        asigna al atributo correspondiente.          
        Lo convierte a mayúsculas para evitar problemas de          
        capitalización.          
        Args:             
            time_format: cadena con el formato de hora                          
                        ("AM", "PM" o "24 HOURS").
        Devuelve:             
            True si el formato es correcto, False en caso              
            contrario.         
        """      
        if not isinstance(time_format, str): #Comprobamos si es una cadena
            return False   
        time_format = time_format.upper() #Convertimos la cadena a mayúsculas para poder comparar
        if time_format in Time.TIME_FORMATS:  #Comprobamos si el formato se encuentra dentro de los defnidos en TIME_FORMATS
            self.__time_format = time_format
            return True
        else:
            return False
    # Método de instancia (privado): Comprueba __time_format
    def __is_24hour_format(self)->bool:
        """
        Comprueba si el formato de la hora es "24 HOURS".
        Devuelve:
            True si formato es "24 HOURS", False en caso contrario.
        """
        if self.__time_format == "24 HOURS":
            return True
        else:
            return False
    # Método de instancia (protegido): Comprueba la validez de los valores almacenados en la instancia.
    def _is_valid_time(self)->bool:
        """         
        Comprueba si la hora es correcta según el formato.          
         
        Devuelve:             
            True si la hora es correcta, False en caso contrario.         
        """
        
        if not (0 <= self.__minutes <= 59 and 0 <= self.__seconds <= 59):
            return False
            
        if self.__is_24hour_format():
            return 0 <= self.__hours <= 23
        else:  # Formatos "AM" o "PM"
            return 1 <= self.__hours <= 12
       
            
    # Método de instancia: Modifica los atributos de la instancia tras validar.
    def set_time(self, hours: int, minutes: int, seconds: int, time_format: str)->bool:
        """         
        Asigna una hora.
        Args:
            hours: horas (1 a 12 en AM/PM, 0 a 23 en 24 HOURS).
            minutes: minutos (0 a 59).
            seconds: segundos (0 a 59).
            time_format: formato ("AM", "PM" o "24 HOURS"). 

        Devuelve:
            True si la hora se pudo asignar correctamente,
            False en caso contrario
        """
        if not (isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int) and isinstance(time_format, str)):
            return False
         #Almacenamos los valores antiguos de forma temporal por si los nuevos no son válidos
        old_hours = self.__hours
        old_minutes = self.__minutes
        old_seconds = self.__seconds
        old_format = self.__time_format 
        if not self.__assign_format(time_format):
            return False

        #Asignamos los valores temporalmente
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

        #Si no es válido, restauramos los datos antiguos
        if not self._is_valid_time():
            self.__hours = old_hours
            self.__minutes = old_minutes
            self.__seconds = old_seconds
            self.__time_format = old_format
            return False

        return True
    # Método de instancia: Devuelve la representación formateada de la instancia
    def get_time(self)->str:
        """
        Devuelve la hora actual del objeto
        Devuelve:
            str: Cadena formateada con dos dígitos para horas, minutos y segundos.
        """
        tiempo = f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d} {self.__time_format}" #Un numero entero de minimo dos carcteres, q1 caracter de relleno
        return tiempo
    
    # Método de clase: Actúa como constructor alternativo para instanciar la clase desde un string.
    @classmethod
    def from_string(cls, time_string:str)->"Time | None":
        """
        Crea una nueva instancia de Time a partir de una cadena.

        Args:
             time_string: cadena con la hora en el formato
                "HH:MM:SS FORMATO", donde FORMATO es AM, PM o
                 24 HOURS.

        Devuelve: 
            Una instancia de Time con la hora leída.
            Si la cadena no es válida, muestra un mensaje. 
        """
        import re
        patron = r"^(\d{1,2}):(\d{2}):(\d{2})\s+(AM|PM|24 HOURS)$"
        match = re.match(patron, time_string.strip(), re.IGNORECASE)

        if match:
    
            hours = int(match.group(1))
            minutes = int(match.group(2))
            seconds = int(match.group(3))
            time_format = match.group(4).upper()
    

            new_time = cls()
            if new_time.set_time(hours, minutes, seconds, time_format):
                return new_time
            else:
                # Si los valores numéricos están fuera del rango permitido
                Time.time_count -= 1  # Decremntar el contador de objetos
                print("Error. Los valores de la hora no son válidos.")
                return None
        else:
            print(
                f"Error. La cadena '{time_string}' no tiene un formato de hora válido."
            )
            return None
    # Método estático: No necesita acceder ni a la instancia ni a la clase para validar el formato
    @staticmethod
    def is_valid_format(time_format: str)->bool:
        """
        Comprueba si un formato de hora dado es
        válido.
        Args:
            time_format: cadena con el formato de hora a comprobar.
        Devuelve:
            True si el formato es válido (AM, PM o 24 HOURS),
            False en caso contrario.
        """
        if not isinstance(time_format, str):
            return False
        return time_format.upper() in Time.TIME_FORMATS
    # Método de clase: Accede al atributo de clase 'time_count'
    @classmethod
    def get_time_count(cls)->int:
        """
        Devuelve el número de objetos de la clase que se han
        creado.
        Devuelve:
            Un número entero de objetos Time creados.
        """
        return cls.time_count

#Funcion fuera de la clase:
def hour_format(time_obj: Time) ->str:
    # Leemos los valores mediante las propiedades públicas (@property)
    h = time_obj.hours
    m = time_obj.minutes
    s = time_obj.seconds
    tf = time_obj.time_format

    return f"{h:02d}:{m:02d}:{s:02d} {tf}"
def mostrar_menu()->str:
    """Muestra el menú de opciones en consola y lee la elección del usuario.

    Devuelve: La opción seleccionada como cadena de texto.
    """
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Introducir una nueva hora")
    print("2. Visualizar hora")
    print("3. Crear una hora a partir de una cadena (“HH:MM:SS FORMATO”)")
    print("4. Terminar")
    return input("Selecciona una opción (1-4): ").strip()

def main():
    opcion = ""
    hora = Time() #Creamos la instancia para trabajar con ella
    while opcion != "4":
        opcion = mostrar_menu()
        match opcion:
            case "1":
                try:
                    h = int(input("Introduzca las horas: "))
                    minutos = int(input("Introduzca los minutos: "))
                    s = int(input("Introduzca los segundos: "))
                    fmt = input(
                        "Ingrese formato (AM, PM, 24 HOURS): "
                    ).strip()

                    if hora.set_time(h, minutos, s, fmt):
                        print("La hora se ha asignado de forma correcta.")
                    else:
                        print("Error. Los datos ingresados no son válidos.")
                except ValueError:
                    print(
                        "Error. Las horas, minutos y segundos deben ser números enteros."
                    )
                
            case "2":
                t_form = hour_format(hora)
                print(f"Hora actual: {t_form}")
            case "3":
                cadena = input("Ingrese LA HORA (“HH:MM:SS FORMATO”):")
                hora_cad = Time.from_string(cadena)
                if hora_cad:
                    hora = hora_cad
                    print(f"La hora ha sido actualizada correctamente")
            case "4":
                print("Fin del programa")
            case _:
                print("Opción no válida")

if __name__ == "__main__":
    main()
            