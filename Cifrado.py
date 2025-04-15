class CifradoCesar:
    def __init__(self, nombre):
      
        self.nombre = nombre
        self.cifrando = False

    def iniciar_presentacion(self):
        self.cifrando = True
        print(f"¡Bienvenido al cifrador, {self.nombre}!")
        print("El cifrado ha comenzado..")
        print("Introduce el texto que deseas cifrar.")
        
        texto = input("Texto: ")
        if texto == texto.upper():
            abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            abc = "abcdefghijklmnopqrstuvwxyz"
            
            k = int(input("Valor de desplazamiento: "))
            acifrar = ""
            
            for letra in texto:
                if letra in abc:
                    acifrar += abc[abc.index(letra) + k%(len(abc))]
                else:
                    acifrar += letra
                    
                    print("texto cifrado: ", acifrar)

        print("¡Gracias por cifrar!")

    def salir(self):
        print(f"Hasta luego, {self.nombre}. ¡Vuelve pronto!")


  
    


