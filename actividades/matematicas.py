# módulo matematicas

def sumar(x=0 , y=0): # valor por defecto
    # función para sumar 2 números
    return x + y

def restar(x, y):
    # función para restar 2 números
    return x - y

def multiplicar(x, y):
    # función para restar 2 números
    return x * y

def dividir(x, y):
    # función para restar 2 números
    return x / y

def calcula(operacion, x=0, y=0):
    match operacion:
        case 1:
            return x + y
        case 2:
            return x - y
        case 3:
            return x * y
        case 4:
            return x / y
