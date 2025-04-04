""" CS - Sem3
Crea un script que calcula em máximo común divisor
"""


class MaximoComunDivisor:

    def __init__(self, numero1=0, numero2=0):
        self._num1 = numero1
        self._num2 = numero2

    @property  # getter
    def num1(self):
        return self._num1

    @property  # getter
    def num2(self):
        return self._num2

    @num1.setter  # setter
    def num1(self, value):
        self._num1 = value

    @num2.setter  # setter
    def num2(self, value):
        self._num2 = value

    def calcular_mcd(self):
        """
        Calcula el Máximo Común Divisor (MCD) de dos números enteros positivos utilizando el algoritmo de Euclides.
        """
        a, b = self.num1, self.num2
        while b != 0:
            a, b = b, a % b
        return a

    def validar_numero(numero):
        try:
            num = int(numero)
            if num <= 0:
                print("Por favor, ingrese un número entero positivo.")
                return False, None
            return True, num
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            return False, None

    def solicitar_numero(self, mensaje):
        """
        Solicita entrada de usuario para un número entero positivo.
        """
        while True:
            num = input(mensaje)
            valido, num = MaximoComunDivisor.validar_numero(num)
            if valido:
                return num


mcd = MaximoComunDivisor()

# Solicitar entrada de usuario y guardar en atributos
mcd.num1 = mcd.solicitar_numero("Ingrese el primer número entero positivo: ")
mcd.num2 = mcd.solicitar_numero("Ingrese el segundo número entero positivo: ")

# Calcular y mostrar el MCD
print(f"El Máximo Común Divisor de {mcd.num1} y {mcd.num2} es: {mcd.calcular_mcd()}")
