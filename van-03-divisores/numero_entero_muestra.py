class NumeroNegativoException(Exception):
    pass

class NumeroNatural():
    def validarTipo(self):
        while True:
            try:
                self._numeroNatural = int(input("Ingrese un número natural: "))
                if self._numeroNatural < 0 :
                    raise NumeroNegativoException
                break
            except ValueError as err:
                print("Oops!  Ingrese un número natural.  Intente otra vez...")
            except NumeroNegativoException as err:
                print("Oops!  Ingrese un número entero y positivo.  Intente otra vez...")
        return self._numeroNatural

    @property #getter
    def numeroNatural(self):
        return self._numeroNatural

    @numeroNatural.setter  # setter
    def numeroNatural(self, value):
        self.self._numeroNatural = value

    def divisores(self):
        numero = self._numeroNatural
        contador = 0
        for divisor in range(1, numero + 1):
            if (numero % divisor) == 0:
                print(divisor, "es divisor")
                contador += 1
        print("el numero ", numero, " tiene ", contador, " divisores")

    def MCD(self, a, b):  # algoritmo de Euclides
        if b > a: a, b = b, a  # para que a sea el mayor
        while a % b != 0:
            b, a = a % b, b
        return b

if __name__ == '__main__':
    numero = NumeroNatural()
    numero.validarTipo()
    numero.divisores()

    numero1 = NumeroNatural()
    numero2 = NumeroNatural()
    numero1.validarTipo()
    numero2.validarTipo()

    print(f"MCD({numero1.numeroNatural}, {numero2.numeroNatural}) = "
          f"{numero.MCD(numero1.numeroNatural,numero2.numeroNatural)}")

