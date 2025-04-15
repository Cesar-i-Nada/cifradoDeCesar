class CifradoCesar:
    def __init__(self, nombre):
      
        self.nombre = nombre
        self.cifrando = False

    def iniciar_cifrado(self):
        self.cifrando = True
        print(f"\n¡Bienvenido al cifrador, {self.nombre}!")
        print("El cifrado ha comenzado..")
        print("Introduce el texto que deseas cifrar.")
        
        texto = input("texto: ")
        if texto == texto.upper():
            abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            abc = "abcdefghijklmnopqrstuvwxyz"
            
            k = int(input("Valor de desplazamiento (k):"))
            cifrado = ""
            
            for letra in texto:
                if letra in abc:
                    cifrado += abc[abc.index(letra) + k%(len(abc))]
                else:
                    cifrado += letra
                    
                    print("texto cifrado: ", cifrado)

        print("¡Gracias por cifrar!\n")

    def salir(self):
        print(f"\nHasta luego, {self.nombre}. ¡Vuelve pronto!")


  
    


