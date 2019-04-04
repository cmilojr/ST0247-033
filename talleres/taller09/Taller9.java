public class Taller9 {    
    public int levenshtein(String A,String B){
        int mat [][]= new int[A.length()+1][B.length()+1];
        for (int i = 0; i <= A.length(); i++) {
            for (int j = 0; j <= B.length(); j++) {
                if(i==0)mat[i][j]=j;
                else if(j==0)mat[i][j]=i;
                else{
                    double c= Math.min(mat[i-1][j-1]+(A.charAt(i-1)==B.charAt(j-1) ? 0 : 1),Math.min(mat[i-1][j]+1,mat[i][j-1]+1));
                    mat[i][j]= (int)c;
                    
                }
            }
        }
        return mat[A.length()][B.length()];
    }
}