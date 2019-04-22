class ruta:
    """ 
    Authors: sespinosav, jcmilo
    """

    def __init__(self, n, d, r, morningPath, nightPath):
        """
        :param n: many conductors
        :param d: basic route
        :param morningPaht: set of morning paths
        :param nightPath: set of night paths
        """
        print(ruta.costMin(n, d, r, morningPath, nightPath))

    @staticmethod
    def costMin(n, d, r, morningPath, nightPath):
        """
        :param n: many conductors
        :param d: basic route
        :param morningPaht: set of morning paths
        :param nightPath: set of night paths
        :return pathMin: Return the min cost that the company gives to conductors
        """
        morningPath.sort()
        nightPath.sort()
        extHours = 0

        for rutesM, rutesN in morningPath, nightPath:
            
            if ((rutesM + rutesN) - d) > 0:
                extHours = extHours + ((rutesM + rutesN) - d)*r
        
        return extHours

if __name__ == "__main__":
    path = ruta(2, 20, 5, [10, 15], [10, 15])
    path2 = ruta(2, 20, 5, [10, 10], [10, 10])
    print(ruta.costMin(2, 20, 5, [10, 10], [10, 10]))