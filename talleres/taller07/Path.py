"""
:Author: Santiago Espinosa Valderrama
"""

from GraphALv2 import *
from sys import maxsize

class Path(GraphALv2):  
    """
    Class of tools for path's problem 
    """
    
    def __init__(self, size):
        """
        Constructor
        """

        self.listWeight = []

        super().__init__(size)


    def shortest(self, vertex, destination, _sum = 0):
        """
        shortes with backtracking
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


    def shortestg(self, vertex, destination):
        """
        shortes with greedy (dijkstra)
        :return: Weight's shortest path between vertex and destination
        """
        if destination in self.getSuccessors(vertex):
            return self.getWeight(vertex, destination)
        
        elif self.getSuccessors(vertex) == []:
            return "Infinite"
        
        else:
            
            weights = self.getWeightSuccessors(vertex)
            print(weights)

            weightSucesor = min(weights)
            sucesor = self.getDestination(vertex, weightSucesor)

            print(self.getSuccessors(vertex))

            if weightSucesor == "Infinite" or self.shortestg(sucesor, destination) == "Infinite":

                return "Infinite"

            else:

                result = weightSucesor + self.shortestg(sucesor, destination) 

            if result > maxsize:
                return "Infinite"
            
            else:

                return result


if __name__ == "__main__":
     
    graph = Path(8)
    graph.addArc(0,1,3)
    graph.addArc(0,2,5)
    graph.addArc(1,2,4)
    graph.addArc(1,3,7)
    graph.addArc(2,3,8)
    graph.addArc(2,4,2)
    graph.addArc(3,5,3)
    graph.addArc(5,6,3)

    """
    whit backtracking
    """
    print(str(graph.shortest(0,6))) 

    """
    whit greedy(dijkstra)
    """
    print(str(graph.shortestg(0,3))) 
 
 
