import numpy as np 
class MatrizFloat:
    """     
    Clase que representa una matriz dinámica 1D/2D.
    Atributos de clase:         
        TIPO_DATO  #Tipo de dato por defecto (np.float32)
    Atributos de instancia (protegidos):         
    matriz   # Almacena la matriz (utilice numpy)         
    nfil     # Almacena número de filas de la matriz (int)         
    ncol     # Almacena número de columnas de la matriz (int)     
    """ 
    TIPO_DATO = np.float32

    def __init__(self):
       """Inicializador de la clase MatrizFloat.

        No recibe parámetros adicionales. Inicializa _matriz a None,
        y los atributos _nfil y _ncol a 0.
        """
       self._matriz: np.ndarray | None = None
       self._nfil = 0
       self._ncol = 0
    @classmethod
    def matriz_identidad(cls, n:int)-> "MatrizFloat":
        """           
        Método de clase que crea y devuelve una nueva            
        instancia de MatrizFloat configurada como matriz              
        identidad de tamaño n x n          
        Parámetros:             
            El tamaño n de la matriz
        Devuelve:             
            Nueva instancia con matriz identidad creada              
            (MatrizFloat)         
        """
        inst = MatrizFloat()
        inst._nfil = n
        inst._ncol = n
        inst._matriz = np.eye(n, dtype=cls.TIPO_DATO)
        return inst
    @staticmethod #Recibe dos matrices distintas 
    def mismas_dimensiones(m1 : "MatrizFloat", m2: "MatrizFloat")->bool:
        """         
        Método para comparar dimensiones.          
        Parámetros:             
            m1   #Primera matriz a comparar (MatrizFloat)             
            m2   #Segunda matriz a comparar (MatrizFloat)          
        Devuelve:             
            bool:   True si ambas matrices tienen el mismo número de                    
                    filas y columnas, y False en caso contrario                    
                    (o si alguna no está creada)         
        """
        if m1._matriz is None or m2._matriz is None:
            return False
        return m1._nfil == m2._nfil and m1._ncol == m2._ncol
    
    @classmethod
    def crear_matriz2D(cls, nFil: int, nCol: int)->"MatrizFloat":
        """         
        Método para crear una matriz bidimensional de ceros.         
        Asigna valores de filas y columnas según parámetros.   
        Parámetros:
            nFil:   Número de filas (int)             
            nCol:   Número de columnas (int)         
        """
        m_2D = cls()
        m_2D._nfil = nFil
        m_2D._ncol = nCol
        m_2D._matriz = np.zeros((nFil, nCol), dtype=cls.TIPO_DATO)
        return m_2D
    
    @classmethod #Actúa como constructor alternativo
    def crear_matriz1D(cls, nElementos: int)->"MatrizFloat":         
        """         
        Método para crear una matriz unidimensional de ceros.         
        Usa crear_matriz2D para asignar 1 fila y n columnas.         
        Parámetros:             nElementos:  Número de elementos de la fila (int)         
        """ 
        m_1D = cls.crear_matriz2D(1, nElementos)
        return m_1D
    
    def existe(self)->bool:
        """
        Método que verifica si matriz está creada y no está vacía         
        Devuelve:             
            True si existe, de lo contrario False         
        """
        if self._matriz is not None:
            if self._nfil > 0 and self._ncol>0:
                return True
        return False

    def introducir(self)->"MatrizFloat":
        """         
        Método que solicita por consola el valor numérico decimal         
        para cada posición (i, j) de la matriz.    
        Da error si se intenta introducir datos sin haber creado la          
        matriz previamente.         
        """
        if self.existe():
            for i in range(self._nfil):
                for j in range (self._ncol):
                    valor_valido = False
                    while not valor_valido:
                        try:
                            val = input(f"Introduzca el valor numérico para la posición ({i},{j}): ")
                            val = self.TIPO_DATO(val)
                            self._matriz[i,j] = val
                            valor_valido = True
                        except ValueError:
                            print("Debe introducir un numero decimal valido")
            return self
        else:
            print("Error. No puede introducir datos de una matriz que no existe")
            return self

    def mostrar(self):
        """         
        Método para mostrar las dimensiones y los elementos de la          
        matriz. Si la matriz no existe (existe() == False), muestra          
        un mensaje advirtiéndolo         
        """
        if self.existe():
            print(f"Dimensiones de la matriz: {self._nfil} x {self._ncol}")
            print(f"Elementos de la matriz:\n{self._matriz}")
        else:
            print("Error. La matriz no existe")

    #OPERACIONES ALGEBRAICAS
    def sumar_matrices(self, otra_matriz: "MatrizFloat")->"MatrizFloat":
        """         
        Método que suma la matriz actual con otra matriz.                  
        Parámetros:            
            otra_matriz: objeto de MatrizFloat con la matriz a sumar          
        Devuelve:            
            Un nuevo objeto MatrizFloat con la matriz resultante de            
            la suma.               
        """
        if self.mismas_dimensiones(otra_matriz):
            suma = MatrizFloat()
            suma._nfil = self._nfil
            suma._ncol = self._ncol
            suma._matriz = np.add(self._matriz, otra_matriz._matriz)
            return suma
        else:
            print("Las matrices a sumar deben tener las mimsa dimensiones")
            return None

    def restar_matrices(self, otra_matriz: "MatrizFloat")->"MatrizFloat":
        """
        Método que resta la matriz actual con otra matriz.                  
        Parámetros:            
            otra_matriz: objeto de MatrizFloat con la matriz a restar          
        Devuelve:            
            Un nuevo objeto MatrizFloat con la matriz resultante de            
            la resta.               
        """
        if self.mismas_dimensiones(otra_matriz):
            resta = MatrizFloat()
            resta._nfil = self._nfil
            resta._ncol = self._ncol
            resta._matriz = np.subtract(self._matriz, otra_matriz._matriz)
            return resta
        else:
            print("Las matrices a sumar deben tener las mimsa dimensiones")
            return None 