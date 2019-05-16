from GraphAM import *
from MakeGraph import *
from GraphPlot import * 
from MakeCars import *
from time import time
import operator
class Carpooling:
    """
    System for picking-up and taking people to EAFIT University in the littlest time possible.

    Sistema para recoger personas y llevarlas a la Universidad Eafit
    en el menor tiempo poisble con la cantidad de carros disponibles.
    """

    def __init__(self, arcs, passangers, limit = 1.1, eafit = 0, constant =  False):
        """
        Class constructor,
        Initializes the graph and creates the arcs


        :param arcs: file with the arcs that will be created in the graph.
        archivo con los arcos que se van a crear en el grafo.

        :param passangers: number of people who will go to the company.
        numero de personas que iran a la empresa.

        :param limit: limit that you can take each car arriving at the company.
        limite que se puede tardar cada carro llegando a la empresa.

        :param eafit: company to which you are going to arrive.
        empresa a la cual se va a llegar.

        :param constan: tell me about the use the constant.
        dice si se usara una cosntante como  limite.
        
        
        Constructor de la clase,
        inicializa el grafo y crea los arcos
        """
        self.__arcs = arcs
        self.__passangers = passangers
        self.__limit = limit
        self.__eafit = eafit
        self.__constant = constant

        self.__graph = GraphAM(passangers)
        self.makeGraph()

        self.__farthest = self.farthest() 

        dicc = self.pickup()

        cars = MakeCars(dicc)

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
        :return: a list with weight of path's weights and paths 
        una lista de tuplas con los pesos de las rutas, y la ruta en el orden de la lista que devuelve en la tupla.
        """

        self.__pickedup = [self.__eafit]
        self.__pathCars = []

        while len(self.__pickedup) < self.__passangers:

            for farth in self.__farthest:

                if len(self.__pickedup) < self.__passangers and farth not in self.__pickedup:
                    if farth != self.__eafit:
                        path = self.calculatePath(farth)
                        self.__pathCars.append(path)
        
        return self.__pathCars

    def calculatePath(self, farth):
        """
        :param farth: driver.
        conductor del carro.

        
        :return: a tuple with the weight of path and a list with people of path.
        una tupla con el peso de la ruta y el carro de dicha ruta donde el orden de la lsita,
        es el orden de la ruta.
        """

        path = []
        visited = 0
        pathWeight = 0

        succesors = self.organizateWeightNear(farth)

        for node in succesors:

            if node != farth and self.__graph.getWeight(farth, node) != 0:

                if visited == 5 or float(pathWeight + self.__graph.getWeight(path[len(path) - 1], self.__eafit)) > float(self.limited(farth)):

                    pathWeight += self.__graph.getWeight(path[len(path) - 1], self.__eafit)
                    return (pathWeight, path)
            
            if node not in self.__pickedup:
                
                if node != farth and self.__graph.getWeight(farth, node) != 0:

                    self.__pickedup.append(node)
                    pathWeight += self.__graph.getWeight(path[len(path) - 1], node)
                    path.append(node)
                    visited += 1

                else:

                    self.__pickedup.append(node)
                    visited += 1
                    path.append(node)
                           
        return(pathWeight, path)

    def makeGraph(self):
        """
        Make arcs

        Crea los arcos 
        """

        _makeGraph = MakeGraph(self.__graph, self.__arcs, self.__eafit)
    
    def farthest(self):
        """
        :return: an ordered list with the nodes that cost more from themselves to eafit
        directly.
        una lista ordenada con los nodos que mas costo tienen desde ellos mismos hasta eafit 
        directamente.
        """
 
        return self.organizateWeight(self.__eafit)

    def organizateWeight(self, initializator):
        """
        Auxiliar of farthest method.
        Auxiliar del metodo farthest.

        :param initializator: person (node) by which the adjacent routes will be organized from highest to lowest.
        persona(nodo) por la cual se van a organizar las rutas adyacentes de mayor a menor.

        :return: an ordered list with the nodes that cost more from themselves to company
        directly.
        una lista ordenada con los nodos que mas costo tienen desde ellos mismos hasta la empresa
        directamente.
        """

        farthestlist = {}
        for node in range(self.__passangers):
            farthestlist[node] = self.__graph.getWeight(node, initializator) 
        
        
        farthestlistOrder = sorted(farthestlist.items(), key=operator.itemgetter(1))

        farthestlistOrder.reverse()

        farthestlist = dict(farthestlistOrder)

        farthpestlist = list(farthestlist.keys())

        return farthestlist

    def organizateWeightNear(self, initializator):
        """
        :return: an ordered list with the nodes that cost menor from themselves to company
        directly.
        una lista ordenada con los nodos que menos costo tienen desde ellos mismos hasta la empresa 
        directamente.
        """
        farthestlist = {}
        for node in range(self.__passangers):
            farthestlist[node] = self.__graph.getWeight(node, initializator) 
        
        
        farthestlistOrder = sorted(farthestlist.items(), key=operator.itemgetter(1))

        farthestlist = dict(farthestlistOrder)

        farthpestlist = list(farthestlist.keys())

        return farthestlist

    def limited(self, node):
        """
        :param node: nodo al cual se le calculara el limite
        :return: limite de tiempo para el nodo
        """

        if self.__constant == True:
            return self.__graph.getWeight(node, self.__eafit) + self.__limit

        return float(float(self.__graph.getWeight(node, self.__eafit))
               * float(self.__limit))
    
if __name__ == "__main__":
    passangers = input("¿Cual es la cantidad de personas que desea organizar para que lleguen a la empresa?: ")
    p = input("Indique el porcentaje máximo que se puede tardar cada carro: ")
    eafit = input("Indique cual es el identificador de la empresa a la cual desea que lleguen los carros: ")
    pathOfFile = "D:\Python\ST0247-033-master\proyectos\Entrega_Final\Arcs" + str(passangers) + ".txt"
    constant = input("Indique si en vez de porcentaje se usara un tiempo constante: ")

    if constant == "True" or constant == "1":
        constant = True
    else:
        constant = False

    print()
    start = time()
    carpooling = Carpooling(pathOfFile, int(passangers), float(p), int(eafit), constant)
    print()
    stop  = time() - start
    print("Tiempo total de ejecución del algoritmo: ", stop)
    pathPlot = "D:\Python\ST0247-033-master\proyectos\Entrega_Final\Coords" + str(passangers) + ".txt"
    graph = GraphPlot(pathPlot)
    