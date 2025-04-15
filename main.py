from Cifrado import CifradoCesar

def mostrar_menu():
    print("=== MENÚ PRINCIPAL DEL CIFRADOR ===")
    print("1. Iniciar cifrado")
    print("2. Salir")
    print("======================")

def main():
    nombre = input("Ingresa tu nombre y accede al menú principal: ")
    cifrado = CifradoCesar(nombre)
    valor=True
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cifrado.iniciar_cifrado()
        elif opcion == "2":
            cifrado.salir()
            valor=False
        else:
            print("Opción inválida. Intenta de nuevo.\n")

main()
