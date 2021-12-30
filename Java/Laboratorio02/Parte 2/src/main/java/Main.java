
public class Main {
    public static void main(String[] args) {
        int[][] Matriz = new int [5][5];
        int DiagonalP = 0;
        int DiagonalS = 0;
        int Nentero = 0;
        for (int i=0; i<Matriz.length; i++){
            for(int k=0; k<Matriz[0].length; k++){
                Matriz[i][k] = ++Nentero;
        }
        }
        imprimir(Matriz);
        
        
        System.out.println("Diagonal principal:");
        for (int i = 0; i < Matriz.length; i++){
            for (int k=0 ; k < Matriz[0].length; k++){
                if (i == k){
                System.out.println(Matriz[i][k]);
                
                DiagonalP += Matriz[i][k];
                }}
        }
        int k = (Matriz.length)-1;
        System.out.println("Diagonal Secundaria");
        for (int i=0; i < Matriz.length; i++) {
            DiagonalS += Matriz[i][k];
            System.out.println(Matriz[i][k--]);
            
        }
        System.out.println("Diagonales Principales: " + DiagonalP);
        System.out.println("Diagonales Secundarias: " + DiagonalS);
        System.out.println("Division de diagonales: " + (DiagonalP/DiagonalS));
    }        
    public static void imprimir(int[][] Matriz){
        for (int i = 0; i < Matriz.length; i++){
            for (int k=0 ; k < Matriz[0].length; k++){
                System.out.print(Matriz[i][k] +" ");
            }
            System.out.println("");
        }
    }
}