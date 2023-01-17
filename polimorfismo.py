
class Persona:
    #Inicialisamos el constructor que recibe una variable nombre
    def __init__(self, nombre):
        #Instanciamos la variable nombre
        self.nombre = nombre
    #Creamos la variable avanza la cual imprime el nombre con un texto
    def avanza(self):
        print(f'El {self.nombre} anda en el mobi')


        
#Creamos la clase motociclista que hereda de la clase persona
class Motoclista(Persona):
    #Inicializamos el constructor que recibe nombre
    def __init__(self, nombre):
        #iniciamos y referenciamos a la super clase persona y referenciamos al constructor utilizando super, al cual le enviamos nombre
        super().__init__(nombre)
    #Utilizamos el polimorfismo para modificar el metodo avanza e imprimir algo diferente
    def avanza(self):
        print(f'El {self.nombre} anda en la virago')



#Creamos una clase main para instanciar y ejecutar
class main():
    #Instanciamos persona y le damos un valor a nombre
    persona = Persona(nombre = "Angel")
    #ejecutamos persona y el metodo avanza
    persona.avanza()

    #Instanciamos motociclista y le damos un valor a nombre
    motoclista = Motoclista(nombre = 'Padiyon')
    #Ejecutamos persona y el metodo avanza
    motoclista.avanza()

#Ejecutamos el programa y a la clase principal main
if __name__ == '__main__':
    main()