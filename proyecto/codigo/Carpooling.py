from GraphAM import *
from MakeGraph import *
class Carpooling:
    """
    System for picking-up and taking people to EAFIT University in the littlest time possible.

    Sistema para recoger personas y llevarlas a la Universidad Eafit
    en el menor tiempo poisble con la cantidad de carros disponibles
    """

    def __init__(self, arcs, passangers, eafit = 1):
        """
        Class constructor,
        Initializes the graph and creates the arcs
        
        Consturctor de la clase,
        inicializa el grafo y crea los arcos
        """

        self.__graph = GraphAM(passangers)

        self.makeGraph(self.__graph, arcs, eafit)
      
    def makeGraph(self, graph, arcs, eafit):
        """
        Creates the arcs

        Crea los arcos 
        """

        _makeGraph = MakeGraph(graph, arcs, eafit)
        
if __name__ == "__main__":
    carpooling = Carpooling("D:\Python\ST0247-033-master\proyectos\Entrega 2\Arcs.txt", 205)
