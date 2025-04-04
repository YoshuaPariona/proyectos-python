""" CS - Sem3
Crea un script que encyentra los divisores de un número
"""


class ExceptionNumberNotNatural(Exception):
    """Excepción para rechazar los número no naturales"""


def calcular_divisores(num):
    """Función para calcular los divisores"""
    divisores = []
    for div in range(1, num+1):
        if num % div == 0:
            divisores.append(div)
    return divisores


def validar_ingreso():
    """Función para pedir los valores hasta que se digiten correctamente"""
    while True:
        try:
            num = int(input("\nIngrese un número: "))
            if num <= 0:
                raise ExceptionNumberNotNatural
            break
        except ExceptionNumberNotNatural:
            print("Ingrese un número natural")
    return num


number = validar_ingreso()
print(calcular_divisores(number))
