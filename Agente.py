import random
import time
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
    def caminar(self, mapa):

        direcciones=[]

        for i in range(self.ubicacion.fila-1, self.ubicacion.fila+2):
            for j in range(self.ubicacion.columna-1, self.ubicacion.columna+2):
                try:
                    if(mapa[i][j] in {' ', '    '}):
                        direcciones.append([i,j])
                    else:
                        direcciones.append(0)
                except:
                    direcciones.append(0)
        
        print("")
        print("Sensores: "+str(direcciones))

        #Algoritmo de busqueda random
        while(True):
            movimiento = direcciones[random.randint(0, 8)]
        
        #Algoritmo de busqueda hacia derecha
#        for i in range(9):
#            movimiento = direcciones[i]

        #Algoritmo de busqueda hacia izquierda
#        for i in range(8,0,-1):
#            movimiento = direcciones[i]

            if(movimiento!=0):
                mapa[self.ubicacion.fila][self.ubicacion.columna]=' '
                mapa[movimiento[0]][movimiento[1]]='0'
                self.ubicacion.fila=movimiento[0]
                self.ubicacion.columna=movimiento[1]

                print("Seleccionado: "+str([self.ubicacion.fila,self.ubicacion.columna]))

                time.sleep(2)

                return mapa