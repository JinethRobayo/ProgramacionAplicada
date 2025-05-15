# Este es un programa para hacer operaciones matemáticas básicas

#Inicialización Constructor
class Calculadora1:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: División por cero"

    def modulo(self, a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return "Error: División por cero"

# Uso del objeto Calculadora1
if __name__ == "__main__":
    my_calculadora1 = Calculadora1()
    print(my_calculadora1.add(5, 7))
    print(my_calculadora1.subtract(45, 11))
    print(my_calculadora1.multiply(3, 2))
    print(my_calculadora1.divide(10, 4))
    print(my_calculadora1.modulo(10, 3))
    # Aquí probamos con 0 para ver el manejo de error
    print(my_calculadora1.divide(8, 0))  # Intento de dividir por cero
    print(my_calculadora1.modulo(10, 0))  # Intento de módulo por cero
