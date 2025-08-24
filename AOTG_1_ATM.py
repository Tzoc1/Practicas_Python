PIN=1234
intentos=3
saldo=1000

def consultar_saldo(saldo):
    print("Su saldo es: ", saldo)

def retirar_dinero(saldo):

    print("Ingrese la cantidad a retirar:")
    cantidad = int(input())
    if cantidad <= saldo:
        saldo -= cantidad
        print("Retirando:", cantidad)
    else:
        print("Fondos insuficientes.")
    return saldo

def depositar_dinero(saldo):
    print("Ingrese la cantidad a depositar:")
    cantidad = int(input())
    if cantidad > 0:
        saldo += cantidad
        print("Depositando:", cantidad)
    else:
        print("La cantidad no es válida.")
    return saldo

while intentos > 0:
    print("Esto es un ATM\n")
    print("Ingrese su PIN:")
    intento_print=int(input())
    if intento_print==PIN:
        print("PIN correcto. Acceso concedido.")

        while True:
            print("\nSeleccione una opción:")
            print("1. Consultar saldo")
            print("2. Retirar dinero")
            print("3. Depositar dinero")
            print("4. Salir")

            opc = int(input())

            match opc:
                case 1:
                    consultar_saldo(saldo)
                case 2:
                    saldo = retirar_dinero(saldo)
                case 3:
                    saldo = depositar_dinero(saldo)
                case 4:
                    print("Saliendo...")
                    break
    else:
        intentos-=1
        print("PIN incorrecto. Intentos restantes:", intentos)
        if intentos == 0:
            print("Demasiados intentos fallidos.\n Cuenta bloqueada.")
            break