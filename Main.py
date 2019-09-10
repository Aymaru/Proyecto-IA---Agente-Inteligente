import Mapa
import Agente

#Función main, encargada de ejecutar y ser el centro de los módulos.
def main():
        MapaNuevo = Mapa.Mapa()

        if (MapaNuevo.cargar_mapa()):

                #Esta es una instancia del agente que creamos.
                posicion_inicial = [0,12]
                Bichito = Agente.Agente(posicion_inicial,'0')
                #Ciclo de movimiento del agente a través del mapa, con el método del agente 
                #, el print del mapa y un sleep del time, todo esto para crear una simulación de 
                # interfaz.
                while True:
                    MapaNuevo.print_mapa(Bichito.ubicacion)

        else:
                print("¡Mapa con errores!")

main()
