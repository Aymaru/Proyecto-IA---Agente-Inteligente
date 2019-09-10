import random
import math 
import Nodo
import GrafoMemoria

#Clase del agente la cual contiene la ubicación del mismo como atributos y un metodo caminar.
class Agente:
    ubicacion = []
    memoria = GrafoMemoria.Grafo()
    objetivos = []
    volveracasa = False
    casa = []

    #constructor encargado de ubicar el agente en el mapa.
    def __init__(self, posicion,bichito):
        self.ubicacion = Nodo.Nodo(posicion[0],posicion[1],bichito)
        self.casa = self.ubicacion

    def calcular_distancia(self, inicio, destino):

        return math.sqrt((destino.columna-inicio.columna)**2+(destino.fila-inicio.fila)**2)
    
    #Método encargado de mover al agente por el mapa, al igual que mirar a su alrededor.

    def volver_casa()

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
                    self.memoria.add_nodo(temp)

        else:
            recuerdo.contador+=1

            if(self.memoria.get_arista(recuerdo)==[]):
                for i in vista:
                    if(i.objeto in {' ', '  ', '@'}):
                        temp = Nodo.Nodo(i.fila, i.columna, i.objeto)
                        self.memoria.add_arista(recuerdo, temp)
                        self.memoria.add_nodo(temp)

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

            for i in vista:
                if(i.objeto=='@' and i not in self.objetivos):
                    movimiento=i
                    break

            if(movimiento.objeto in {' ', '    ', '@'} and opciones[rand]==menor):
                self.ubicacion.fila = movimiento.fila
                self.ubicacion.columna = movimiento.columna
                if(movimiento.objeto=='@' and movimiento not in self.objetivos):
                    self.objetivos.append(movimiento)
                    opcion=int(input("¿Desea volver a  casa? 1- si 2- no: "))
                    if opcion==1:
                        self.volveracasa = True 
                return self.volveracasa
            
            while(self.volveracasa):

                opciones = []

                for i in vista:
                    opciones.append(self.calcular_distancia(self.ubicacion, self.casa))

                menor = min(opciones)


        #----------------------------------------