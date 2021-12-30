package parte2;
public class Matriz {
    private char matriz[][] = new char[4][4];

    public void mostrarMatriz(){
        for(int x=0; x<matriz.length;x++){
            for(int y=0; y<matriz[x].length;y++){
                System.out.print(matriz[x][y]);
                if(y!=matriz[x].length-1){
                    System.out.print("\t");
                }
            }
            System.out.println("");
        }
    }

    public boolean verificar(int numero){
        if(numero<matriz.length){
            return true;
        }
        else{
            System.out.println("Al menos uno de los valores está fuera de la matriz.");
            return false;
        }       
    }
    
    public void ingresarCaracter(int fila, int columna){
        if(verificar(fila)==true && verificar(columna)==true){
            if(matriz[fila][columna]=='X'){
                System.out.println("Ese espacio ya está ocupado.");   
            }
            else{
                matriz[fila][columna]= 'X'; 
            }
        }       
    }

    
}
