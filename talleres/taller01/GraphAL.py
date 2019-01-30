class GraphAL:

    """La implementacion que haremos
    se basa en una lista de diccionarios
    donde el indice de la lista de los diccionarios
    es el inicio
    la llave del diccionario es el destino
    y el peso es el valor de la llave en cada diccionario"""

    #Constructor para el grafo dirigido
    #@param tamaño de la matriz de orden nxn
    def __init__(self, size):

      #Creamos la lista
      self.__listt = []

      #Llenamos la lista con diccionarios vacio
      #@param tamaño de la matriz nxn
      for i in range(size):
        self.__listt.append(dict())

    """@param vertex desde donde se hara el arco
       @param destination hacia donde va el arco
       @param weight el peso de la longitud entre source y destination"""
    def addArc(self, vertex, edge, weight):

      """Agregamos una clave valor al diccionario ya existente
      Que sera el inicio y el destino que conforma al arco nuevo"""
      #@see <https://www.programiz.com/python-programming/methods/dictionary/update> ver documentacion de la funcion update
      self.__listt[vertex].update({edge : weight})

    #@param vertex desde donde se hara el arco
    def getSuccessors(self, vertice):

      #@return una lista con las llaves de la lista
      #del diccionario, que vendrian siendo los nodos succesores
      return self.__listt[vertice].keys()

    #@param source desde donde se inicia el arco
    #@param destination desde donde se hara el arco
    def getWeight(self, source, destination):

      #@return el peso del arco entre el inicio y el destino
      return self.__listt[source][destination]

    def __str__(self):

      pass
