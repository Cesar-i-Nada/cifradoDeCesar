from Cifrado import CifradoCesar

def mostrar_menu():
    print("=== MENÚ PRINCIPAL DEL CIFRADOR ===")
    print("I. Iniciar cifrado")
    print("X. Salir")
    print("======================")

def main():
    nombre = input("Ingresa tu nombre y accede al menú principal: ")
    acifrar = CifradoCesar(nombre)
    valor=True
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "I":
            acifrar.iniciar_presentacion()
        elif opcion == "X":
            acifrar.salir()
            valor=False
        else:
            print("Opción inválida. Intenta de nuevo.")

main()
