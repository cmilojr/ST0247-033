from sys import maxsize

class GraphALv2:
    """
    La implementacion que haremos
    se basa en una diccionario de diccionarios
    donde la llave del diccionario es el nodo
    el valor es un diccionario, donde la llave es el destino y el valor del peso
    """

    def __init__(self, size):
      """
      Constructor creamos un diccionario
      """
      self.__adja = dict({})
      self.__size = size

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



    def getSuccessors(self, vertex):
       """
       :param vertex: nodo al que se le sacaran los sucesores
       :return: los sucesores de vertex
       """
       listt = []
       if vertex in self.__adja:
        for sucesor in self.__adja[vertex].keys():
          listt.append(sucesor)

       return listt

    def getWeight(self, source, destination):

      """
      :param source: nodo de salida
      :param destination: nodo de llegada
      :return: peso del arco entre source y destination
      """
    
      return self.__adja[source][destination]
    
    def getWeightSuccessors(self, vertex):
      """
      :param vertex: nodo al que se le sacaran los pesos de los sucesores
      :return: los pesos de los sucesores de vertex
      """
      
      successors = self.getSuccessors(vertex)
      weights = []

      for sucesor in successors:

        weights.append(self.getWeight(vertex, sucesor))
      
      return weights

    def getDestination(self, vertex, weight):

      for destination in range(self.__size):
        if destination in self.getSuccessors(vertex):
          if self.__adja[vertex][destination] == weight:
              
            return destination
      
      return maxsize




