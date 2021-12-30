package parte2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
      Matriz matriz = new Matriz();
      Scanner input = new Scanner(System.in); 
      boolean continuar = true;
      while(continuar){
        System.out.println("------ MENÚ ------");
        System.out.println("1. Ingresar valor.");
        System.out.println("2. Mostrar matriz.");
        System.out.println("3. Salir.");
        int opcion = Integer.parseInt(input.nextLine());
        System.out.println("------------------");

        switch(opcion){
            case 1:
                matriz.mostrarMatriz();
                System.out.print("Ingrese la fila: ");
                int fila = Integer.parseInt(input.nextLine());
                System.out.print("Ingrese la columna: ");
                int columna = Integer.parseInt(input.nextLine());
                System.out.println("------------------");
                matriz.ingresarCaracter(fila, columna);
                break;
            case 2:
                matriz.mostrarMatriz();
                break;
            case 3:
                continuar=false;
                break;
            default:
                System.out.println("Ingrese una de las opciones del menú.");
                break;
        }
      }
    }
    
}
