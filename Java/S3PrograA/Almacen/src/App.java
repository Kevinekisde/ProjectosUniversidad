/*SOLEMNE N3 PROGRAMACION AVANZADA
    INTEGRANTES: KEVIN LEIVA, CRISTOPHER BANDERAS, THOMAS CONTRERAS
    ENUNCIADO: Se trata de un programa el cual simula una tienda de
    tecnologia, en donde puedes cotizar tus productos (Con su nombre,
    marca y precio) para obtener el valor total de tu peticion. */


import java.util.Scanner;

public class App {    public static void main(String[] args) {
        Datos datos = new Datos();
        Scanner input = new Scanner(System.in);
        boolean continuar = true;
        while(continuar){
            System.out.println("----------- MENÚ -----------");
            System.out.println("1.Componente 1.");
            System.out.println("2.Componente 2");
            System.out.println("3.Componente 3");
            System.out.println("4.Componente 4");
            System.out.println("5.Componente 5");
            System.out.println("6.Cotizar Armado");
            System.out.println("7.Salir");
            System.out.println("Opcion: ");
            int Opcion = Integer.parseInt(input.nextLine());

            switch(Opcion){
                case 1:
                datos.CrearProductos(1);
                break;
                case 2:
                datos.CrearProductos(2);
                break;
                case 3:
                datos.CrearProductos(3);
                break;
                case 4:
                datos.CrearProductos(4);
                break;
                case 5:
                datos.CrearProductos(5);
                break;
                case 6:
                datos.getCreados(0).armar(datos.getCreados(0),datos.getCreados(1),datos.getCreados(2),
                datos.getCreados(3),datos.getCreados(4));
                break;
                case 7:
                continuar = false;
                break;

            }
        }
    }
}
