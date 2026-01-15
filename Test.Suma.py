def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'No se puede dividir entre cero.'

while True:
    print('Seleccione la operación que desea realizar:')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Salir')
    operacion = int(input('Ingrese la operación (1-5): '))
    
    if operacion != 5:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
    
    if operacion == 1:
        print(suma(num1, num2))
    elif operacion == 2:
        print(resta(num1, num2))
    elif operacion == 3:
        print(multiplicacion(num1, num2))
    elif operacion == 4:
        print(division(num1, num2))
    elif operacion == 5:
        break

