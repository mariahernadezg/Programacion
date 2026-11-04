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
    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    def __init__(self):
        """
        Incializa los atributos a 0.
        Es el único método que se le pasa parámetros como ejemplo
        """
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.__time_format = 0
        Time.time_count += 1

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
        time_format = time_format.upper() #Convertimos la cadena a mayúsculas para poder comparar
        if time_format in self.TIME_FORMATS:  #Comprobamos si el formato se encuentra dentro de los defnidos en TIME_FORMATS
            self.__time_format = time_format
            return True
        else:
            return False

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

    def _is_valid_time(self)->bool:
        """         
        Comprueba si la hora es correcta según el formato.          
         
        Devuelve:             
            True si la hora es correcta, False en caso contrario.         
        """ 
        if self.__is_24hour_format():
            if 0 <= self.__hours <= 23:
                return True
        else:
            if 1 <= self.__hours <= 12:
                return True
            else:
                return False
            
    
        