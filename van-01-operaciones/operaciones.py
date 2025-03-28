""" CS - Sem1
Implementa las operaciones matemáticas básicas
"""


def suma(a, b):
    return a+b


def resta(a, b):
    return a-b


def multi(a, b):
    return a*b


def div(a, b):
    if b == 0:
        raise ValueError('No se puede dividir por 0')
    return a/b


while True:
    print('\nIngrese una operación:')
    print('\n[1]: Suma')
    print('[2]: Resta')
    print('[3]: Multiplicación')
    print('[4]: División')
    print('[5]: Salir')

    opcion = input('\nElige una opción: ') 
    
    if opcion == '5':
        print('Saliendo de la calculadora.')
        break

    try:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))

        if opcion == '1':
            print(f'Resultado: {suma(num1, num2)}')
        elif opcion == '2':
            print(f'Resultado: {resta(num1, num2)}')
        elif opcion == '3':
            print(f'Resultado: {multi(num1, num2)}')
        elif opcion == '4':
            print(f'Resultado: {div(num1, num2)}')
        else:
            print('Opción no válida prro')

    except ValueError as e:
        print(f'Error: {e}')
