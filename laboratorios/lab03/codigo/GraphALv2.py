
class GraphALv2:
    """
    La implementacion que haremos
    se basa en una diccionario de diccionarios
    donde la llave del diccionario es el nodo
    el valor es un diccionario, donde la llave es el destino y el valor del peso
    """

    def __init__(self):
      """
      Constructor creamos un diccionario
      """
      self.__adja = dict({})

    def addNode(self, node):
      """
      Crea un nuevo nodo

      :param node: nodo a crear
      """
      self.__adja[node] = None

    def addArc(self, vertex, edge, weight):
        """
        Agrega un arco al grafo

        :param vertex: cola del arco
        :param edge: cabeza del arco
        :param weight: peso del arco
        """

        if vertex in self.__adja and self.__adja[vertex] != None:

          self.__adja[vertex].update({edge : weight})

        else:

          self.__adja[vertex] = {edge : weight}

        if edge in self.__adja and self.__adja[edge] != None:

          self.__adja[edge].update({vertex : edge})

        else:

          self.__adja[edge] = {vertex : weight}


    def getSuccessors(self, vertex):
       """
       :param vertex: nodo al que se le sacaran los sucesores
       :return: los sucesores de vertex
       """

       return self.__adja[vertex].keys()

    def getWeight(self, source, destination):

      """
      :param source: nodo de salida
      :param destination: nodo de llegada
      :return: peso del arco entre source y destination
      """

      return self.__adja[source][destination]


