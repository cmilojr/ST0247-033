import java.util.ArrayList;
public class DigraphAM extends Digraph {

    int[][] matriz;

    public DigraphAM(int size) {
        super(size);
        matriz = new int[size][size];
    }

    public void addArc(int source, int destination, int weight) {
        matriz[source][destination] = weight;
    }

    public ArrayList<Integer> getSuccessors(int vertex) {
        ArrayList<Integer> respuesta = new ArrayList();
        for (int j =0; j < matriz[vertex].length;j++){
            if (matriz[vertex][j] !=0 ) {
                respuesta.add(j);
            }
        }
        return respuesta;
    }

    public int getWeight(int source, int destination) {
        return matriz[source][destination];
    }
}
