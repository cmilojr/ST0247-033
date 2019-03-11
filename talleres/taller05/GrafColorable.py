"""

:Author: Santiago Espinosa, Camilo

"""
from GraphAL3_0.GraphAL3_0 import *
from Bfa3_0.Bfa3_0 import *

class GrafColorable(GraphAL3_0):
    """
    Esta Clase se encarga de evaluar cuantos colores necesita un grafo para ser pintado
    """
    def __init__(self, size):

        super().__init__(size)
        self.__colors = ["R", "G", "B", "Y"] #Con 4 colores se puede pintar cualquier grafo
        
    def cantidadDeColores(self):

        """
        Evalua cuantos colores son necesarios para pintar un grafo 
        """

        permutaciones = self.generarPermutaciones()
        for i in permutaciones:

            self.pintarGrafo(i)

            if self.evaluate:

                cantidadDeColores = 0

                if "R" in i:
                    cantidadDeColores += 1
                
                if "G" in i:
                    cantidadDeColores += 1

                if "B" in i:
                    cantidadDeColores += 1

                if "Y" in i:
                    cantidadDeColores += 1

                return cantidadDeColores

        return -1 
    
    def generarPermutaciones(self):
        """
        Generar todas las permutaciones con repeticion con los colores dados
        """

        Bfa = Bfa3_0()

        return Bfa.permutacionesRepeticion(self.__colors[:self.getSize()], self.getSize()) 
    
    def pintarGrafo(self, graph):
        """
        Pinta el grafo con los colores dados
        """

        for i in range(self.getSize()):

            self.setColor(i, graph[i])
    
    def evaluate(self):
        """
        Evalua si el grafo pintado es valido
        """

        for nodo in range(self.getSize()):

            for sucesor in self.getSuccessors(nodo):
                
                if nodo.getColor == sucesor.getColor:

                    return False

        return True
                



        



            
    
    