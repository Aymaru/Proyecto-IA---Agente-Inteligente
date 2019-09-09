import Mapa
import Agente

#Función main, encargada de ejecutar y ser el centro de los módulos.
def main():
        MapaNuevo = Mapa.mapa()

        if (MapaNuevo.cargar_mapa()):

                #Esta es una instancia del agente que creamos.
                Bichito = Agente.Agente(MapaNuevo.mapa)
                #Ciclo de movimiento del agente a través del mapa, con el método del agente 
                #, el print del mapa y un sleep del time, todo esto para crear una simulación de 
                # interfaz.
                while True:
                    MapaNuevo.printMapa()
                    MapaNuevo.mapa=Bichito.caminar(MapaNuevo.mapa)

        else:
                print("¡Mapa con errores!")

main()
