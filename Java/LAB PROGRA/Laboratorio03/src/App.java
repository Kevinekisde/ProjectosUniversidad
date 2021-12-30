import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Datos datos = new Datos();
        Scanner input = new Scanner(System.in);
        boolean continuar = true;
        while(continuar){
            System.out.println("----------- MENÚ -----------");
            System.out.println("1. Crear personaje 1.");
            System.out.println("2. Crear personaje 2.");
            System.out.println("3. ¡COMBATE!");
            System.out.println("4. Salir.");
            System.out.print("Opción: ");
            int opcion = Integer.parseInt(input.nextLine());
            System.out.println("----------------------------");
            switch(opcion){
                case 1:
                    datos.crearPersonaje(1);
                    break;
                case 2:
                    datos.crearPersonaje(2);
                    break;
                case 3:
                    datos.getCreados(0).combate(datos.getCreados(0), datos.getCreados(1));
                    break;
                case 4:
                    continuar = false;
                    break;
                default:
                    System.out.println("Ingrese una de las opciones del menú.");
            }
        }
    }
}
