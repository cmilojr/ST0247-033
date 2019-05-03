from GraphAM import *
from MakeGraph import *
from GraphPlot import * 
from time import time
import operator
class Carpooling:
    """
    System for picking-up and taking people to EAFIT University in the littlest time possible.

    Sistema para recoger personas y llevarlas a la Universidad Eafit
    en el menor tiempo poisble con la cantidad de carros disponibles
    """

    def __init__(self, arcs, passangers, limit = 1.1, eafit = 0):
        """
        Class constructor,
        Initializes the graph and creates the arcs
        
        Consturctor de la clase,
        inicializa el grafo y crea los arcos
        """
        self.__arcs = arcs
        self.__passangers = passangers
        self.__limit = limit
        self.__eafit = eafit

        self.__graph = GraphAM(passangers)
        self.makeGraph()

        self.__farthest = self.farthest() 

        dicc = self.pickup()

        print()
        print("La llave del diccionario indica el tiempo")
        print("que se tarda el carro desde que inicia la")
        print("ruta hasta la empresa")
        print()
        print("El valor del diccionario es el carro")
        print()
        print("El primer pasajero del carro es el conductor")
        print("e indica desde donde parte el carro")
        print()
        print("El orden en que estan colocados los pasajeros")
        print("en el carro, es el orden en el que serán recogidos")
        print()
        print("Numero de carros necesarios: ", len(dicc))
        print()
        print(dicc)
    
    def pickup(self):
        """
        recoger
        :variable pickedup: recogidos
        """

        self.__pickedup = [self.__eafit]
        self.__pathCars = {}

        for farth in self.__farthest:

            if len(self.__pickedup) < self.__passangers:
                if farth != self.__eafit:
                    path = self.calculatePath(farth)
                    self.__pathCars.update(path)
        
            else:
                return self.__pathCars
        
        return self.__pathCars

    def calculatePath(self, farth):

        path = []
        visited = 0
        pathWeight = 0

        succesors = self.organizateWeight(farth)

        for node in succesors:

            if visited >= 4 or pathWeight > self.limited(farth, node):

                return {pathWeight : path}
            
            if node not in self.__pickedup:

                self.__pickedup.append(node)
                pathWeight += self.__graph.getWeight(farth, node)
                visited += 1
                path.append(node)
        
        return {pathWeight : path}

    def makeGraph(self):
        """
        Creates the arcs

        Crea los arcos 
        """

        _makeGraph = MakeGraph(self.__graph, self.__arcs, self.__eafit)
    
    def farthest(self):
        """
        :return: una lista ordenada con los nodos que mas costo tienen desde ellos mismos hasta eafit 
        directamente
        """
 
        return self.organizateWeight(self.__eafit)

    def organizateWeight(self, initializator):

        farthestlist = {}
        for node in range(self.__passangers):
            farthestlist[node] = self.__graph.getWeight(node, initializator) 
        
        
        farthestlistOrder = sorted(farthestlist.items(), key=operator.itemgetter(1))

        farthestlistOrder.reverse()

        farthestlist = dict(farthestlistOrder)

        farthestlist = list(farthestlist.keys())

        return farthestlist

    def limited(self, node, succesor):
        """
        :param node: nodo al cual se le calculara el limite

        :return: limite de tiempo para el nodo
        """

        return (int((float(self.__graph.getWeight(node, self.__eafit))
               * self.__limit)
               + float(self.__graph.getWeight(succesor, self.__eafit))))
    
if __name__ == "__main__":
    passangers = input("¿Cual es la cantidad de personas que desea organizar para que lleguen a la empresa?: ")
    p = input("Indique el porcentaje máximo que se puede tardar cada carro: ")
    eafit = input("Indique cual es el identificador de la empresa a la cual desea que lleguen los carros: ")
    pathOfFile = "D:\Python\ST0247-033-master\proyectos\Entrega_Final\Arcs" + str(passangers) + ".txt"
    print()
    start = time()
    carpooling = Carpooling(pathOfFile, int(passangers), float(p), int(eafit))
    print()
    stop  = time() - start
    print("Tiempo total de ejecución del algoritmo: ", stop)
    pathPlot = "D:\Python\ST0247-033-master\proyectos\Entrega_Final\Coords" + str(passangers) + ".txt"
    graph = GraphPlot(pathPlot)



