package laboratorio02;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Vector vect = new Vector();

        Scanner input = new Scanner(System.in);
        boolean continuar = true;
        while(continuar){
            System.out.println("1. Crear vector A");
            System.out.println("2. Crear vector B");
            System.out.println("3. Crear vector C");
            System.out.println("4. Crear vector D");
            System.out.println("5. Mostrar vector A");
            System.out.println("6. Mostrar vector B");
            System.out.println("7. Mostrar vector C");
            System.out.println("8. Mostrar vector D");
            System.out.println("9. Salir");
            System.out.println("Seleccione una opción:");
            int opcion = input.nextInt();
            System.out.println("*********************************************************"); 

            switch(opcion){
                case 1:
                    vect.cuadradoPosicion();
                    break;
                case 2:
                    vect.numerosPares();
                    break;
                case 3:
                    vect.numeroImpares();
                    break;
                case 4:
                    vect.sumaAB();
                    break;
                case 5:
                    vect.mostrarDatosA();
                    break;
                case 6:
                    vect.mostrarDatosB();
                    break;
                case 7:
                    vect.mostrarDatosC();
                    break;                  
                case 8:
                    vect.mostrarDatosD();
                    break;
                case 9:
                    continuar = false;
                    break;
                default:
                    System.out.println("Ingrese una de las opciones señaladas");                
            }

        }
        
    }
    
}
