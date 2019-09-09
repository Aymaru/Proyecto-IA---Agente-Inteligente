import random
import time
import Nodo

#Clase del agente la cual contiene la ubicación del mismo como atributos y un metodo caminar.
class Agente:
    i=0
    j=0

    #constructor encargado de ubicar el agente en el mapa.
    def __init__(self, mapa):

        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j]=='0':
                    self.i=i
                    self.j=j

    #Método encargado de mover al agente por el mapa, al igual que mirar a su alrededor.
    def caminar(self, mapa):

        direcciones=[]

        for i in range(self.i-1, self.i+2):
            for j in range(self.j-1, self.j+2):
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
                mapa[self.i][self.j]=' '
                mapa[movimiento[0]][movimiento[1]]='0'
                self.i=movimiento[0]
                self.j=movimiento[1]

                print("Seleccionado: "+str([self.i,self.j]))

                time.sleep(2)

                return mapa