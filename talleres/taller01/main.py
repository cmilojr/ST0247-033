#@Author Santiago Espinosa, Juan Camilo
from GraphAM import *
from GraphAL import *

#Pruebas

#Pruebas de grafos con Matriz
prueb =  GraphAM(4)
prueb.addArc(1,1,5)
prueb.addArc(0,3,8)
prueb.addArc(1,3,4)
prueb.addArc(2,2,3)

print(prueb.getEdges())
print(prueb.getWeight(1,1))
print(prueb.getSuccessors(1))

#Pruebas de grafos con Listas
prueb = GraphAL(3)
prueb.addArc(0,2,5)
prueb.addArc(1,0,1)
prueb.addArc(1,1,3)
prueb.addArc(1,2,4)

print("")
print(prueb.getWeight(1,1))
print(prueb.getSuccessors(1))
