""" CS - Sem2
Determina el mayor de tres números ingresados por el teclado
"""


class OrdenarTresNumeros:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0

    def intercambiar_valores(self, num_a, num_b):
        temp = num_a
        num_a = num_b
        num_b = temp
        return num_a, num_b

    def ingresar_numeros(self):
        self.num1 = int(input("Ingrese el primer número: "))
        self.num2 = int(input("Ingrese el segundo número: "))
        self.num3 = int(input("Ingrese el tercer número: "))

    def ordenar_numeros(self):

        if self.num1 > self.num2:
            self.num1, self.num2 = self.intercambiar_valores(self.num1, self.num2)

        if self.num2 > self.num3:
            self.num2, self.num3 = self.intercambiar_valores(self.num2, self.num3)

        if self.num1 > self.num2:
            self.num1, self.num2 = self.intercambiar_valores(self.num1, self.num2)

    def imprimir_numeros(self):
        print(f"Los numeros son: {self.num1} - {self.num2} - {self.num3}")

    def imprimir_mayor(self):
        print(f"EL mayor número es: {self.num3}")


if __name__ == "__main__":

    numeros = OrdenarTresNumeros()
    numeros.ingresar_numeros()
    print("\nNúmeros desordenados")
    numeros.imprimir_numeros()
    numeros.ordenar_numeros()
    print("\nNúmeros ordenados")
    numeros.imprimir_numeros()
    numeros.imprimir_mayor()
