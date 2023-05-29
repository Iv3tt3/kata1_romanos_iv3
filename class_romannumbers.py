'''from romannumbers import *

class RomanNumber:
    def __init__(self, input):
        if type(input) == int:
            #cuando pones _ delante es como una regla legible para todo el mundo
            self._numero = input
            self._simbolo = entero_a_romano(input)
        elif isinstance (input, str):
            self._numero = Romano_a_Entero(input)
            self._simbolo = input
        else:
            raise RomanNumberError("Se debe introducir un entero o romano valido")
    
    @property
    def num(self):
        return self._numero
    
    @num.setter
    def num(self, input):
        self._numero = input
        self._simbolo = entero_a_romano(input)

    @property
    def simbol(self):
        return self._simbolo
    
    @simbol.setter
    def simbol(self, input):
        self._numero = Romano_a_Entero(input)
        self._simbolo = input
    
''' 
from romannumbers import *

class RomanNumber:
    def __init__(self, entrada):
        if type(entrada) == int:
            #cuando pones un _ delante estas diciendo que no los usen
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif isinstance (entrada, str):
            self._numero = Romano_a_Entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError("Se debe introducir un entero o romano valido")
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)

    @property
    def simbolo(self):
        return self._simbolo
    
    @simbolo.setter
    def simbolo(self, entrada):
        self._numero = Romano_a_Entero(entrada)
        self._simbolo = entrada

    #Metodos magicos para aritmetica

    def __eq__(self, other):
        #Este metodo es necesario para comparar instancias, es decir, el resultado de numero * otro numero saca una instancia y se compara con otra instancia guardada en otro espacio de memoria. Aunque sea iguales, python no los ve iguales. Por eso es necesario este metodo.
        return self.numero == other.numero

    def __mul__(self, otro):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        resultado = self.numero * otro.numero
        return RomanNumber(resultado)
    
    def __rmul__(self, otro):
        return self.__mul__(otro)
    
    def __repr__(self):
        return f"{self.numero} [{self.simbolo}]"
    
    def __str__(self):
        return self.__repr__()