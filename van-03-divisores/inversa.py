""" CS - Sem3
Crea un script que calcula la inversa de un número
"""


class ExceptionNumeroCero(Exception):
    """Excepción para el 0"""
    print("Error. El número debe ser diferente de 0")


try:
    x = float(input("Numero: "))
    if x == 0:
        raise ExceptionNumeroCero
    inversa = 1/x
    print(f"Numero = {x} su inversa es {inversa}")
except ValueError:
    print("Error. Debe ingresar un número")
except ExceptionNumeroCero:
    print("Error. El número debe ser diferente de 0")
else:
    print("aver")
finally:
    print("Fin del script")
