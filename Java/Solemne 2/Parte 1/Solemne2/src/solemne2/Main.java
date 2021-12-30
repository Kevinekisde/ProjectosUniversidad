package solemne2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Datos estudiante = new Datos();
        Scanner input = new Scanner(System.in);
        boolean continuar = true;
        while(continuar){
            System.out.println("------ MENÚ ------");
            System.out.println("1. Crear estudiante.");
            System.out.println("2. Mostrar estudiante.");
            System.out.println("3. Mostrar todos.");
            System.out.println("4. Mostrar promedio general.");
            System.out.println("5. Salir");
            int opcion = Integer.parseInt(input.nextLine());
            System.out.println("------------------");

            switch(opcion){
                case 1:
                    System.out.println("Ingrese el indice del estudiante a crear: ");
                    int indice = Integer.parseInt(input.nextLine());
                    System.out.println("------------------");
                    estudiante.ingresarDatos(indice);
                    break;
                case 2:
                    System.out.println("Ingrese el RUT del estudiante: ");
                    String busqueda = input.nextLine();
                    System.out.println("------------------");
                    estudiante.mostrarEstudiante(busqueda);
                    break;
                case 3:
                    estudiante.mostrarTodo();
                    break;
                case 4:
                    estudiante.promedioGeneral();
                    break;
                case 5:
                    continuar = false;
                    break;
                
                default:
                    System.out.println("Ingrese una de las opciones del menú.");
                    break;
                


            }

        }


    }
    
}
