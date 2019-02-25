from N_Reinas import *
from time import time

tablero = N_Reinas(8)
#tablero.addBlock(1, 0)

star = time()

tablero.generatePermutations()

stop = time()

tablero.getCount()

timer = stop - star

print('')
print('Tiempo de ejecucion: '+str(timer))

