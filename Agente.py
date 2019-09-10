import random
import Nodo

#Clase del agente la cual contiene la ubicación del mismo como atributos y un metodo caminar.
class Agente:
    ubicacion = Nodo.Nodo()

    #constructor encargado de ubicar el agente en el mapa.
    def __init__(self, posicion,bichito):
        self.ubicacion.fila = posicion[0]
        self.ubicacion.columna = posicion[1]
        self.ubicacion.objeto = bichito

        

    #Método encargado de mover al agente por el mapa, al igual que mirar a su alrededor.
    def caminar(self, vista):

        while(True):

            movimiento = vista[random.randint(0,len(vista)-1)]

            if(movimiento.objeto in {' ', '    ', '@'}):
                self.ubicacion.fila = movimiento.fila
                self.ubicacion.columna = movimiento.columna
                return 0