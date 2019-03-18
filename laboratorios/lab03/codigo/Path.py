"""
:Author: Santiago Espinosa Valderrama
"""

from GraphALv2 import *
from sys import maxsize

class Path(GraphALv2):  
    """
    Class of tools for path's problem 
    """
    
    def __init__(self):
        """
        Constructor
        """

        self.listWeight = []

        super().__init__()


    def shortest(self, vertex, destination, _sum = 0):
        """
        :return: Weight's shortest path between vertex and destination
        """
        if destination in self.getSuccessors(vertex):
            return _sum + self.getWeight(vertex, destination)
        
        if self.getSuccessors(vertex) == []:
            return maxsize

        successors = self.getSuccessors(vertex)

        weightPath = 0

        for sucesor in successors:
            
            auxSum = _sum + self.getWeight(vertex, sucesor)

            weight =  self.shortest(vertex, sucesor, auxSum)

            if weight > weightPath and weightPath < maxsize:
                weightPath = weight
            
        return weightPath

if __name__ == "__main__":
     
    graph = Path()
    graph.addArc(0,1,3)
    graph.addArc(0,2,5)
    graph.addArc(1,2,4)
    graph.addArc(1,3,7)
    graph.addArc(2,3,8)

    print(str(graph.shortest(0,3))) 
 
 
