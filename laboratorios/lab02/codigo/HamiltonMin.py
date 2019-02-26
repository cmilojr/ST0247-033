"""
:Author: Santiago Espinosa(sespinosav), Camilo Restrespo(jrcamilo)

"""
from GraphAL import *
from Bfa2_0 import *


class HamiltonMin():
    """
    Reprentacion en grafo de el mapa de la ciudad de medellin
    """

    def __init__(self, archivo):

        """
        :param archivo: archivo con las coordenadas de la ciudad
        :param limitNodes: linea en la cual se encuentran las coordenadas del ultimo lugar ingresado
        :param indexArcs: comienzo de los arcos
        :param limitArchi: ultima linea del archivo
        """
        self.__graph = GraphAL()
        self.__archivo = open(archivo)
        self.__lista = self.__archivo.readlines()
        self.__costoMinimo = 0

    def makeArcs(self):

        """
        Ingresa los arcos al grafo
        """

        print("")
        for i in self.__lista:
            line = i.split(" ")
            self.__graph.addArc(float(line[0]), float(line[1]), float(line[2]))

    def permutaciones(self, vertex):

        """
        Generar permutaciones para evaluar

        :param vertex: archivo con los vertices
        """

        self.__archivo = open(vertex)
        self.__lista = self.__archivo.readlines()

        pal = ""
        lis = Bfa2_0()

        for i in self.__lista:
            line = i.split(" ")
            pal = pal + str(line[0])

        lis.permutaciones(pal)
        listt = lis.getListt()

        return listt

    def CaminoMin(self):

        listt = self.permutaciones()

        for i in self.permutaciones():

            if self.HayCamino(i):

                if self.CostoCamino(i) > self.__costoMinimo:

                    self.__costoMinimo = self.CostoCamino(i)

        return self.__costoMinimo


    def HayCamino(self, vector):

        """
        Evaluamos si existe el camino

        :param vector: camino a evaluar
        :return: si hay o no camino
        """

        for i in vector:
            if vector[vector.index(i) + 1] not in self.__graph.getSuccessors(i):
                return False

        return True

    def CostoCamino(self, vector):

        """
        Costo del camino

        :param vector: Camino
        :return: Costo del camino
        """

        peso = 0

        for i in vector:
            peso = peso + self.__graph.getWeight(i, vector[vector.index(i + 1)])

        return peso

    def getCostoMinimo(self):

        return self.__costoMinimo


