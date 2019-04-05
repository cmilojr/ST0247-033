class GraphAM:
    
    #Implementacion de grafos utilizando matrices de adjacencia
    
    def __init__(self, size):

        #:param size: tamaño de la matriz nxn
        #Creamos la matriz

        self.__matriz = [None] * size
        for i in range(size):
            self.__matriz[i] = [None] * size

        """
        Inicializamos todos los pesos en None
        esto provoca que si dos vertices
        no estan conectados tendran peso None
        e identificaremos que no tienen arco
        cuando se agrega un arco, al tener que pasar
        el peso por parametro
        identificamos que hay arco
        """

        for i in self.__matriz:
            for j in i:
                j = None

    def getEdges(self):


        """
        :return listt: una lista con diccionarios
        de los arcos totales del grafo
        las llaves de los diccionarios son el inicie(source)
        y la clave es el destino
        """
    
        listt = []
        for i in self.__matriz:
            for j in i:
                if j != None:
                    dicc = {self.__matriz.index(i) : i.index(j)}
                    listt.append(dicc)

        return listt

    """
    :param source: nodo de partido
    :param destination: hacia donde va el arco
    :return weight: el peso de la longitud entre source y destination"""   
    
    def getWeight(self, source, destination):
        
        """
        :param source: nodo de partido
        :param destination: hacia donde va el arco
        :return weight: el peso de la longitud entre source y destination
        """
    
        #Vamos a la poscision de la matriz en
        #El nodo de partida y el destinatino
        #Y tomamos su peso
        return self.__matriz[source][destination]

    """
    Vamos a la poscision de la matriz en
    El nodo de partida y el destinatino
    Y le agregamos un peso
    Lo que provoca que cambie de estar en None
    A tener un peso y así sabremos que existe el arco
    """
    def addArc(self, source, destination, weight):
        self.__matriz[source][destination] = weight
    
    def getSuccessors(self, vertex):
     
        #:param vertex: vertice del cual vamos a sacar sus sucesroes
        #:return succesirs: una lista de los nodos succesores de vertex

        #Inicializamos la lista que deseamos retornar
        succesor = []

        #Recorremos
        for i in self.__matriz[vertex]:
            #Verificamos si hay arco entre los nodos
            #Atravez de saber si el peso tiene valor
            if i != None:
                #Agregamos a la lista de succesores
                #El nodo
                succesor.append(self.__matriz[vertex].index(i))

        return succesor

    def __str__(self):

        pass

