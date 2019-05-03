class MakeGraph:
    """
    Make a Graph with a file that contains Medellin's arcs
    """
    def __init__(self, graph, arcs, eafit):
        """
        Constructor Of class
        """

        self.__eafit = eafit

        self.__file = open(arcs)

        self.__list = self.__file.readlines()

        self.__file.close()
        
        self.makeArcs(self.__list, graph)

    
    def makeArcs(self, _list, graph):
        """
        Make arcs in the graph with _list
        """
        for line in _list:
            arc = line.split()
            graph.addArc(int(arc[0])-1, int(arc[1])-1, int(arc[2]))

            """
            Se le resta un uno por que el indice de los nodos empieza en 1
            Y la matriz en 0, por lo tanto el nodo 1 seria el 0
            el 2 el 1 y asi sucesivamente.
            """

    def getEafit(self):

        return self.__eafit
