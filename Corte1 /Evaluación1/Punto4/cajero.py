class Cajero:
    def __init__(self):
        self.saldo = 0

    def ver_saldo(self):
        print(f"Saldo actual: ${self.saldo}")

    def consignar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has consignado: ${monto}")
        else:
            print("No puedes consignar un monto negativo.")

    def retirar(self, monto):
        if monto <= 0:
            print("No puedes retirar un monto negativo o cero.")
        elif monto > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"Has retirado: ${monto}")

    def pedir_monto(self):
        while True:
            entrada = input("Ingresa un monto: ")
            try:
                valor = float(entrada)
                return valor
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def iniciar(self):
        while True:
            print("\n--- Cajero Automático ---")
            print("1. Ver saldo")
            print("2. Consignar dinero")
            print("3. Retirar dinero")
            print("4. Salir")

            opcion = input("Elige una opción (1-4): ")

            if opcion == "1":
                self.ver_saldo()
            elif opcion == "2":
                monto = self.pedir_monto()
                self.consignar(monto)
            elif opcion == "3":
                monto = self.pedir_monto()
                self.retirar(monto)
            elif opcion == "4":
                print("Gracias por usar el cajero. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intenta de nuevo.")

