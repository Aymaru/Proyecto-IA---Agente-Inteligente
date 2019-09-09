import os
import Nodo

class mapa:
    mapa = []
    contadores = []

#Función encargada de la carga del mapa desde un text a la variable global -mapa-.
    def cargar_mapa(self):
        fila=[] #variable de uso para meter en la matriz las filas del archivo.
        tam=0 #variable de tamaño, para saber si el tamaño de la matriz es uniforme.


        #Bloque de código encargado de la carga del archivo.
        try:

            f = open("Mapa.txt", "r")
            for linea in f.readlines():
                fila=[]
                for elemento in linea:
                    if elemento != '\n':
                        fila.append(elemento)
                        tam+=1
                self.mapa.append(fila)

            f.close()

            if(tam!=len(self.mapa)*len(self.mapa[0])):
                return False

        except AttributeError:
            print("Debes insertar un fichero")
        except FileNotFoundError:
            print("La ruta no es correcta o no existe el fichero")

        fila=[]

        return True

    #Función encargada de la impresión de la matriz.
    def printMapa(self):

        os.system ('cls')

        linea=""

        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[i])):
                linea+=self.mapa[i][j]
            print(linea)
            linea=""

