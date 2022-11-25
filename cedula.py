import re
import sys

#sys.tracebacklimit = 0


class Cedula:

    """
    El numero de una cédula de identidad tiene exactamente 7 dígitos al cual se le adiciona
     un dígito verificador.

    Es así que un número valido debe respetar el siguiente formato:

    a.bcd.efg-h

    El dígito posterior al guión (h) es también llamado dígito verificador.

    Para obtener h debemos:

    Multiplicar a,b,c,d,e,f,g por las siguientes constantes:
            (a; b; c; d; e; f; g) .* (2; 9; 8; 7; 6; 3; 4)

    El resultado de la suma s = 2*a + 9*b + 8*c + 7*d + 6*e + 3*f + 4*g es dividido por 10 
    quedándonos con resto (M = s modulo 10)

    Finalmente h = (10 - M) % 10

    Ejemplo practico:
    Si la CI es 1.234.567:

    s = 2*1 + 9*2 + 8*3 + 7*4 + 6*5 + 3*6 + 4*7 = 148
    M = 148 % 10 = 8
    h = (10 - 8) % 10 = 2
    Obteniendo que 1.234.567-2 es un número de CI valido.
    """
    SEQUENCE = (2, 9, 8, 7, 6, 3, 4)

    def __init__(self, numero):
        """ Inicializa la clase
        Asigna un numero de cedula a la propiedad publica numero

        Args:
            numero: un numero de cedula entre 6 y 7 digitos, puede ser int o string
        """
        self.numero = numero
        self._verifier = ""

    @property
    def numero(self):
        """ propiedad de lectura

        Returns:
            _numero: la propiedad privada de numero de cedula ya normalizada
        """
        return self._numero

    @numero.setter
    def numero(self, val):
        """ asigna a la propiedad privada el numero de cedula asignado a numero, 
            lo normaliza y valida
        Args:
            val (int o string): el numero de cedula

        """
        try:
            if isinstance(val, str):
                # si la cedula es un string, le saco el formato (puntos y guiones)
                numUpdated = re.sub(r"[\.|\-]", "", val)
                self._numero = numUpdated
            else:
                self._numero = str(val)

            if not self._numero.isnumeric():
                sys.exit("cedula should be only numbers")

            if (len(self._numero) < 6 or len(self._numero) > 7):
                sys.exit("invalid cedula length...")

        except:
            sys.exit(
                "Cedula conversion error, check cedula length, value or format.")

    @property
    def verifier(self):
        """propiedad de lectura del digito verificador

        Returns:
            int: digito verificador
        """
        return self._verifier

    def __acumSequence(self, seq, index):
        """ funcion recursiva privada que suma los digitos de una cedula

        Args:
            seq: el numero en la constante SEQUENCE
            index (int): la posicion en ambos arrays (secuencia y cedula)
                    Deben matchear en posicion
            
            ** NOTA: como la correspondencia debe ser 1:1 seq y _numero, en caso de ser 
            una cedula de 6 digitos se podia haber agregado un 0 al inicio de _numero para comenzar
            con el mismo largo (7 digitos), pero asi es mas divertido :D

        Returns:
            int: la acumulacion de la suma de digito de self._numero * digito de secuencia
        """
        if index < (len(seq) - 1):
            return (seq[index] * int(self._numero[index])) + self.__acumSequence(seq, index + 1)
        return seq[index] * int(self._numero[index])

    def getVerifierDigit(self):
        """ calculo de digito verificador

        Returns:
            int: digito verificador
        """
        try:
            digit_diff = (len(self.SEQUENCE) - len(self._numero))
            if digit_diff >= 0:
                acum = 0
                acum = self.__acumSequence(self.SEQUENCE[digit_diff:], 0)
                mod = (acum % 10)
                verifier = ((10 - mod) % 10)
                self._verifier = str(verifier)
            return verifier
        except:
            print("ERROR: unknown error, check params!")

    def formatCedula(self):
        """ formatea un numero de cedula al formato de puntos y guion
        ej: 12345678 => 1.234.567-8

        Returns:
            string: el numero de cedula completo y formateado
        """
        self.getVerifierDigit()
        if len(self.numero) == 6:
            return self.numero[:3] + '.' + self.numero[3:] + '-' + self.verifier
        return self.numero[:1] + '.' + self.numero[1:4] + '.' + self.numero[4:] + '-' + self.verifier
