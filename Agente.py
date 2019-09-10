import random
import Nodo
import GrafoMemoria

#Clase del agente la cual contiene la ubicación del mismo como atributos y un metodo caminar.
class Agente:
    ubicacion = []
    memoria = GrafoMemoria.Grafo()
    objetivos = []

    #constructor encargado de ubicar el agente en el mapa.
    def __init__(self, posicion,bichito):
        self.ubicacion = Nodo.Nodo(posicion[0],posicion[1],bichito)

    #Método encargado de mover al agente por el mapa, al igual que mirar a su alrededor.
    def moverse(self, vistasucia):

        #Aquí se filtra la primera parte sin objetos solidos

        vista=[]

        for i in vistasucia:
            if(i.objeto in {' ', '  ', '@'}):
                vista.append(i)

        #----------------------------------------------

        #Este segmento de código agrega a la memoria(grafo), nuevos recuerdos

        actual = Nodo.Nodo(self.ubicacion.fila, self.ubicacion.columna, ' ')
        actual.contador+=1

        recuerdo = self.memoria.is_nodo(actual)

        if(recuerdo==[]):
            self.memoria.add_nodo(actual)

            for i in vista:
                if(i.objeto in {' ', '  ', '@'}):
                    temp = Nodo.Nodo(i.fila, i.columna, i.objeto)
                    self.memoria.add_arista(actual, temp)

        else:
            recuerdo.contador+=1

        #--------------------------------------------

        #Aquí de obtienen las posibles opciones, de acuerdo a criterios de repetición y cercanía a objetivos

        opciones = []

        for i in vista:
            posible = self.memoria.is_nodo(i)
            if(posible!=[]):
                opciones.append(posible.contador)
            else:
                opciones.append(0)

        menor = min(opciones)

        #----------------------------------

        #Este es el paso final, aquí se realiza el movimiento

        while(True):

            rand=random.randint(0,len(vista)-1)

            movimiento = vista[rand]

            if(movimiento.objeto in {' ', '    ', '@'} and opciones[rand]==menor):
                self.ubicacion.fila = movimiento.fila
                self.ubicacion.columna = movimiento.columna
                return 0

        #----------------------------------------