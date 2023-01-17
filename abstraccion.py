class Lavadora:

    #Este es un constructor, dejamo un passya que no tendra cuerpo
    def __init__(self):
        pass
    #En este metodo nosotros dejamos como default la temperatura como caliente y llamamos a los demas metodos
    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadiendo_jabon()
        self._lavar()
        self._centrifugar()
    #A partir de aqui estan los metodos que manda a llamar lavar con el orden que es requerido
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua{temperatura}')

    def _anadiendo_jabon(self):
        print('Añadiendo jabon a la lavadora')

    def _lavar(self):
        print('La lavadora empieza a lavar')
    
    def _centrifugar(self):
        print('Centrifugando la lavadora')


#Este if sirve para hacer referencia a como debe de iniciar el codigo
if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()