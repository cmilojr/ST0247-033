def ruta(x, menor, visitados):
    if menor = []:
        return visitados
    else:
        visistados.append(x)
        menor = self.ordenarmenor(vertex,getsuccesors(x), visitados)
        return ruta(menor,self.ordenarmenor(succeroesordenados(0)),visitados)

def ordenarmenor(vertex,sucesores, visitados):
    menor = None
    arrayaux = []
    for i in sucesores:
        if i not in visitados:
            if menor = None:
                menor = i
            elif menor >= getWeight(vertex,i):
                menor = i

    return menor
        