
package laboratorio01;

import java.util.Scanner;

public class Laboratorio01 {
    public static void main(String[] args) {

        // Se crean los objetos de Plan
        Plan p = new Plan();
        p.setCostoMantencion(15000);
        p.setCostoMinuto(80);

        Plan n = new Plan();
        n.setCostoMantencion(7000);
        n.setCostoMinuto(120);
        
        int clientesP = 0;
        int clientesN = 0;

        // Se crean los clientes
        Cliente cliente1 =  new Cliente();
        boolean continuar = true;
        while(continuar == true){
            Scanner input = new Scanner(System.in);

            System.out.println("Ingrese el nombre: ");
            String nombre = input.nextLine();
            cliente1.setNombre(nombre);

            System.out.println("Ingrese el tiempo de conexión (minutos): ");
            int tiempoConexion = Integer.parseInt(input.nextLine());
            cliente1.setTiempoConexion(tiempoConexion);

            boolean validar = false;
            while(validar==false){         
                System.out.println("Ingrese el tipo de plan (Preferencial = 'p', Normal = 'n'): ");
                String tipoPlan = input.nextLine();
                if("p".equals(tipoPlan.toLowerCase())){
                    tipoPlan = "Preferencial";
                    cliente1.setTipoPlan(tipoPlan);
                    cliente1.mostrarDatos(p);
                    clientesP += 1;
                    validar = true;
                }
                if("n".equals(tipoPlan.toLowerCase())){
                    tipoPlan = "Normal";
                    cliente1.setTipoPlan(tipoPlan);
                    cliente1.mostrarDatos(n);
                    clientesN += 1;
                    validar = true;
                }
                
            }
            validar = false;
            while(validar==false){           
                System.out.println("¿Desea crear otro cliente? (y/n): ");
                String seleccion = input.nextLine();
                if("y".equals(seleccion.toLowerCase())){
                    continuar = true;
                    validar = true;
                }
                if("n".equals(seleccion.toLowerCase())){
                    continuar = false;
                    validar = true;
                }
            }

        }
        System.out.println("Clientes con plan preferencial: "+clientesP);
        System.out.println("Clientes con plan normal: "+clientesN);
    }
    
}
