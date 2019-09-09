import os
import Nodo

class Mapa:
    mapa = []
    contadores = []

#Función encargada de la carga del mapa desde un text a la variable global -mapa-.
    def cargar_mapa(self):
        fila=[] #variable de uso para meter en la matriz las filas del archivo.
        tam=0 #variable de tamaño, para saber si el tamaño de la matriz es uniforme.
        fil = 0
        col = 0

        #Bloque de código encargado de la carga del archivo.
        try:

            f = open("Mapa.txt", "r")
            for linea in f.readlines():
                fila=[]
                for elemento in linea:
                    if elemento != '\n':
                        nodo = Nodo.Nodo()
                        nodo.fila = fil
                        nodo.columna = col
                        nodo.objeto = elemento
                        fila.append(nodo)
                        tam+=1
                        col += 1
                self.mapa.append(fila)
                fil += 1
                col = 0

            f.close()

            if(tam!=len(self.mapa)*len(self.mapa[0])):
                return False

        except AttributeError:
            print("Debes insertar un fichero")
        except FileNotFoundError:
            print("La ruta no es correcta o no existe el fichero")

        fila=[]

        return True

    def iniciar_contador(self):
        
        fila = []
        for i in range(len(self.mapa)):
            
            for j in range(len(self.mapa[i])):
                fila.append(0)

            self.contadores.append(fila)
            fila = []
            
    def actualizar_contador(self,nodo):
        self.contadores[nodo.fila][nodo.columna] += 1

    def ver_campos_continuos(self,nodo):
        nodos = []
        i = nodo.fila
        j = nodo.columna

        for i in range(i-1, i+2):
            for j in range(j-1, j+2):
                nodos.append(self.mapa[i][j])

        return nodos

    def print_contadores(self):
        for fila in range(len(self.contadores)):
            for columna in range(len(self.contadores[fila])):
                print(self.contadores[fila][columna])

    #Función encargada de la impresión de la matriz.
    def print_mapa(self,nodo):

        os.system ('cls')

        linea=""

        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if ( i == nodo.fila and j == nodo.columna):
                    linea+=nodo.objeto
                else:
                    linea+=self.mapa[i][j].objeto
            print(linea)
            linea=""

