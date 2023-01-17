#Creamos la clase animales con el meto hablar vacia pero con pass para que no genere error
class Animal:
    def hablar(self):
        pass
#Creamos la clase perro con herencia de Animal
class Perro(Animal):
    #Usamos polimorfismo para utilizar el metodo hablar y modificarlo para imprimir como hablaria el perro
    def hablar(self):
        print("Guau")
#Hacemos lo mismo pero con gato
class Gato(Animal):
    def hablar(self):
        print("Miau")
#Inicializamos el programa iterando animal con perro y gato, ejecutando el metodo hablar
if __name__ == '__main__':
    for animal in Perro(), Gato():
        animal.hablar()