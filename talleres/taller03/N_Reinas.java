//@Author Santiago Espinosa, Juan Camilo

import java.util.ArrayList;

public class N_Reinas {

    public static void main(String[] args) {
        
    }

    public static void imprimirTablero(int[] tablero) {
        int n = tablero.length;
        System.out.print("    ");
        for (int i = 0; i < n; ++i)
            System.out.print(i + " ");
        System.out.println("\n");
        for (int i = 0; i < n; ++i) {
            System.out.print(i + "   ");
            for (int j = 0; j < n; ++j)
                System.out.print((tablero[i] == j ? "Q" : "#") + " ");
            System.out.println();
        }
        System.out.println();
    }

    public static boolean esValido(int[] tablero) {
        int n = tablero.length;
        
        //recorre cada columna (deberia haber una reina por col) del arreglo
        for (int i = 0; i < n; ++i) {
            //fila de la reina en la columna "i"
            int pos = tablero[i];
            //mira las diagonales a la derecha de una reina
            for (int j = 1; j < n - i; j++) {
                int up = pos - j;
                int down = pos + j;
                if( tablero[i + j] == up || tablero[i + j] == down) {
                    return false;
                }
            }
            
            //mira las diagonales a la izquierda de una reina
            for (int j = 1; j < i - n; j++) {
                int up = pos - j;
                int down = pos + j;
                if( tablero[i - j] == up || tablero[i - j] == down) {
                    return false;
                }
            }
        }
        //mira las horizontales del tablero
        for (int i = 0; i < n; i++) {
            for (int j = 1 + i; j < n; j++) {
                if (tablero[i] == tablero[j]) {
                    return false;
                }
            }
        }
        
        return true;
    }

    public static int queens(int n) {
        int cont = 0; 
        int maxPos = n;
        
        //Calcula el numero de posibilidades para un tablero de tamaño n
        for (int i = 0; i < n-1; i++) {
            maxPos = maxPos * n;
        }
        
        //Arreglo de todos los posibles tableros
         ArrayList<int[]> permutaciones = new ArrayList<int[]>(maxPos); 
        
        //Crea todas los posibles tableros de n-reinas y cuenta los que son validos
        for (int i = 0; i < maxPos; i++) {
            int[] tablero = crearTablero(n, i);
            if (esValido(tablero)) {
                cont++;
            }
        }
        
        
        return cont;
    }
    
    
    /*
     * Crea un tablero unico basado en una conversion de un numero (menor o igual al total de posibilidades) a una
     * base equivalente al tamaño n de un tablero 
     */
    public static int[] crearTablero(int base, int numero) {
        int[] tablero = new int[base];
        int count = 1;
        
        while(numero > 0) {
            int remainder = numero % base;
            numero =  numero / base;
            tablero[base - count] = remainder;
            count++;
        }     
        
        return tablero;
    }
   
}
