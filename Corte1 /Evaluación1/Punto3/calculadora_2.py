class Calculadora2:
    def __init__(self):
        pass 

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: División por cero"

    def modulo(self, a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return "Error: División por cero"

    def pedir_numeros(self):
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            return a, b

    def iniciar(self):
        while True:
            print("\n--- Menú de la Calculadora ---")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Módulo")
            print("6. Salir")

            opcion = input("Elige una opción (1-6): ")

            if opcion == "6":
                print("👋 Gracias por usar la calculadora.")
                break

            a, b = self.pedir_numeros()
            #if a is None or b is None:
            #    continue  # Si hubo error al ingresar números, vuelve al menú

            if opcion == "1":
                print("Resultado:", self.sumar(a, b))
            elif opcion == "2":
                print("Resultado:", self.restar(a, b))
            elif opcion == "3":
                print("Resultado:", self.multiplicar(a, b))
            elif opcion == "4":
                print("Resultado:", self.dividir(a, b))
            elif opcion == "5":
                print("Resultado:", self.modulo(a, b))
            else:
                print("❌ Opción no válida.")


        
    