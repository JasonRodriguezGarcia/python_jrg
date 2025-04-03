# uso de funciones
# que están en otro módulo
import matematicas

# main program -----------------
if __name__ == "__main__":
    while True:
        print ("\nAPLICACION DE MATEMATICAS")
        print ("1- Sumar")
        print ("2- Restar")
        print ("3- Multiplicar")
        print ("4- Dividir")
        opcion = int(input("Selecciona opcion: "))
        print ("Introduce 2 numeros")
        num1 = float(input ("nº 1: "))
        num2 = float(input("nº 2: "))
        match opcion:
            case 1:
                print(f"Resultado {matematicas.sumar(num1, num2)}")
            case 2:
                print(f"Resultado {matematicas.restar(num1, num2)}")
            case 3:
                print(f"Resultado: {matematicas.calcula(3, num1, num2)}")
            case 4:
                print(f"Resultado: {matematicas.calcula(4, num1, num2)}")
