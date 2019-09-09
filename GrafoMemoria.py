
#Estructura de datos para memoria
class Grafo:
    
    grafo = {}
 
    def add_nodo(self, nodo):
        self.grafo[nodo] = []
 
    def del_nodo(self, nodo):
        #Remueve el nodo si está en el grafo
        try:
            self.grafo.pop(nodo)
        except KeyError:
            #Aquí el nodo no está en el grafo
            pass
    def is_nodo(self, nodo):
        #Retorna True si el nodo esta en el grafo
        try:
            self.grafo[nodo]
            return True
        except KeyError:
            return False
 
    def add_arista(self, nodo, arista):
        #Agrega la arista al nodo si existe
        try:
            self.grafo[nodo].append(arista)
        except KeyError:
            #Aquí el nodo no está en el grafo
            pass
 
    def delete_arista(self, nodo, arista):
        #Remueve la arista en el nodo
        try:
            self.grafo[nodo].remove(arista)
        except KeyError:
            #Aquí el nodo no está en el grafo
            pass
        except ValueError:
            #Aquí la arista no existe
            pass
 
    def get_arista(self, nodo):
        #Retorna las aristas de un nodo si el nodo está en el grafo
        try:
            return self.grafo[nodo]
        except KeyError:
            pass

    def print_grafo(self):
        #Imprime el grafo

        s= "nodo -> aristas\n"

        for i, j in list(self.grafo.items()):
            s+=str(i)+" -> "+str(j)+"\n"
        print(s)

            