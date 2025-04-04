class NumeroEntero:
    def __init__(self, numero = 0):
        self._numero = numero

    @property # getter
    def numero(self):
        return self._numero

    @numero.setter # setter
    def numero(self, value):
        self._numero = value

    def es_primo(self):

        flag_primo = True

        for div in range(2, self.numero):
            if self.numero % div == 0:
                flag_primo = False
        return flag_primo


if __name__ == "__main__":
    num = NumeroEntero()
    num.numero = int(input("Ingrese un número natural: "))

    if num.es_primo():
        print(f"El número {num.numero} es primo")
    else:
        print(f"El número {num.numero} no es primo")
