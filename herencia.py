
class Rectangulo:
    #inicializamos con el Constructor
    def __init__(self, base, altura):
        #vairables de Instancias de base de altura
        self.base = base
        self.altura = altura
    #Metodo que calcula el area multiplicando base por altura
    def area(self):
        return self.base * self.altura

#Aqui heredamos el corpontamiento de rectangulo sinedo rectangulo la super clase
#La clase cuadrado extiende rectangulo
class Cuadrado(Rectangulo):
    #Constructor
    def __init__(self, lado):
        #Super nos permite obtener una referencia directa de la super clase
        #Que en este caso es el rectangulo y llamamos a su constructor
        #Aqui llamamos a super, que nos da acceso a la super clase y llamamos
        #al metodo __init__ que es su constructor y le dimos ambos lados del cuadrado
        #Osea que base = lado, y altura = lado
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    #heredamos el metodo area de la clase y obtenemos lado*lado
    print(cuadrado.area())