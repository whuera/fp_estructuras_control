def consultar_saldo(saldo):
    print(f"Su saldo actual es: {saldo}")

def depositar_dinero(saldo):
    deposito = float(input("Ingrese la cantidad a depositar: "))
    saldo += deposito
    print(f"Has depositado {deposito}. Nuevo saldo: {saldo}")
    return saldo

def retirar_dinero(saldo):
    retiro = float(input("Ingrese la cantidad a retirar: "))
    if retiro <= saldo:
        saldo -= retiro
        print(f"Has retirado {retiro}. Nuevo saldo: {saldo}")
    else:
        print("Error: No puedes retirar más de tu saldo disponible.")
    return saldo

def cajero_automatico():
    PIN = "1234"  # Puedes cambiar el PIN por el que desees
    intentos = 3
    saldo = 1000.0  # Saldo inicial
    
    while intentos > 0:
        ingreso_PIN = input("Ingrese su código PIN: ")
        if ingreso_PIN == PIN:
            while True:
                print("\nOpciones:")
                print("1. Consultar saldo")
                print("2. Depositar dinero")
                print("3. Retirar dinero")
                print("4. Salir")
                opcion = input("Elija una opción: ")
                
                if opcion == "1":
                    consultar_saldo(saldo)
                elif opcion == "2":
                    saldo = depositar_dinero(saldo)
                elif opcion == "3":
                    saldo = retirar_dinero(saldo)
                elif opcion == "4":
                    print("Gracias por usar el cajero automático.")
                    break
                else:
                    print("Opción no válida.")
                    
                continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
                if continuar != 's':
                    print("Gracias por usar el cajero automático.")
                    break
            break
        else:
            intentos -= 1
            print(f"PIN incorrecto. Te quedan {intentos} intentos.")
            if intentos == 0:
                print("Has agotado tus intentos. La cuenta está bloqueada.")
# main
if __name__ == "__main__":
    cajero_automatico()
    


