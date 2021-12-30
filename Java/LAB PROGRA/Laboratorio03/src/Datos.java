import java.util.Scanner;

public class Datos {
    private Personaje creados[] = new Personaje[2];
    private Personaje backup[] = new Personaje[2];

    public void crearPersonaje(int p){
        Scanner input = new Scanner(System.in);
        System.out.println("--- CREACIÓN PERSONAJE " + p + " ---");
        System.out.print("Nombre: ");
        String nombre = input.nextLine();
        System.out.print("Raza (Enano/Elfo/Humano): ");
        String raza = input.nextLine().toLowerCase();
        System.out.print("Arma: ");
        String arma = input.nextLine().toLowerCase();
        System.out.print("Daño: ");
        int dano = Integer.parseInt(input.nextLine());
        System.out.print("Vida: ");
        int vida = Integer.parseInt(input.nextLine());

        switch(raza){
            case "enano":
                System.out.print("Clan: ");
                String clan = input.nextLine();
                Enano personajeEnano = new Enano(nombre, raza, arma, dano, vida, clan);
                creados[p-1] = personajeEnano;
                backup[p-1] = personajeEnano;
                break; 
            case "elfo":
                System.out.print("Reino: ");
                String reino = input .nextLine();
                Elfo personajeElfo = new Elfo(nombre, raza, arma, dano, vida, reino);
                creados[p-1] = personajeElfo;
                backup[p-1] = personajeElfo; 
                break;
            case "humano":
                System.out.print("Casta: ");
                String casta = input.nextLine();
                Humano personajeHumano = new Humano(nombre, raza, arma, dano, vida,casta);
                creados[p-1] = personajeHumano;
                backup[p-1] = personajeHumano;
                break;
            default:
                System.out.print("La raza ingresada no es válida, vuelva a crear el personaje.");
                break;
        }
    }

    public Personaje getCreados(int indice){
        return this.creados[indice];
    }

    public Personaje getBackup(int indice){
        return this.backup[indice];
    }
    
    
}
