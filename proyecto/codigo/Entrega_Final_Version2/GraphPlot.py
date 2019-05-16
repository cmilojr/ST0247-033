from pylab import *

class GraphPlot:
    """
    Make a Graph with a file that contains Medellin's arcs
    """
    def __init__(self, coords):
        """
        Constructor Of class
        """

        self.__x = []
        self.__y = []
        self.__file = open(coords, encoding="utf8")

        self.__list = self.__file.readlines()

        self.makeCoords(self.__list)

        self.__file.close()

        self.makeGraph()

    
    def makeCoords(self, _list):
        for line in _list:
            arc = line.split()
            self.__x.append(float(arc[1]))
            self.__y.append(float(arc[2]))

    def makeGraph(self):

        plot(self.__x, self.__y, 'o')
        xlabel('Coordenadas en x')
        ylabel('Coordebadas en y')

        show()

