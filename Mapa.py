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
                        nodo = Nodo.Nodo(fil, col, elemento)
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

    def actualizar_contador(self,nodo):
        self.mapa[nodo.fila][nodo.columna].contador += 1

    def ver_campos_continuos(self,nodo):
        nodos = []
        i = nodo.fila
        j = nodo.columna

        for fila in range(i-1, i+2):
            if(fila < len(self.mapa) and fila>=0):
                for columna in range(j-1, j+2):
                    if(columna < len(self.mapa[i]) and columna>=0):
                        nodos.append(self.mapa[fila][columna])

        nodos.remove(self.mapa[i][j])

        return nodos

    def print_contadores(self):

        linea=""

        for fila in range(len(self.mapa)):
            for columna in range(len(self.mapa[fila])):
                linea+=str(self.mapa[fila][columna].contador)+" "
            print(linea)
            linea=""

    #Función encargada de la impresión de la matriz.
    def print_mapa(self,nodo):

        os.system ('clear')

        linea=""

        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                if ( i == nodo.fila and j == nodo.columna):
                    linea+=nodo.objeto
                else:
                    linea+=self.mapa[i][j].objeto
            print(linea)
            linea=""

