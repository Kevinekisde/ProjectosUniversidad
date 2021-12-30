import java.util.Scanner;

public class Datos {
    private producto creados[] = new producto [6];
    private producto backup[] = new producto [6];
    public double total = 0 ;


    public void CrearProductos(int p){
        Scanner input = new Scanner(System.in);
        System.out.println("Ingrese su producto ");
        System.out.println("Tipo (Hardware/Software): ");
        String tipo = input.nextLine();
        System.out.println("Nombre: ");
        String NomProd= input.nextLine();
        System.out.println("Marca: ");
        String MarcaProdu = input.nextLine();
        System.out.println("Valor: ");
        int precio = Integer.parseInt(input.nextLine());
        try {
            if (precio < 1){
                throw new Exception("El valor no es valido"); 
            }
        } catch(Exception e){
            System.out.println(e.getMessage());
        }


        switch(tipo){
            case "hardware":
            hardware productohardware = new hardware(NomProd,MarcaProdu,precio,tipo);
            creados[p-1] = productohardware;
            backup[p-1] = productohardware;
            System.out.println(hardware.Agregar());
            break;

            case "software":
            Software producSoftware = new Software(NomProd,MarcaProdu,precio,tipo);
            creados[p-1] = producSoftware;
            backup[p-1] = producSoftware;
            System.out.println(Software.Agregar());
            break;
            
            default:
            System.out.println("El tipo de producto ingresado no es valido, vuelva a ingresarlo.");
        }

    }

    
    public producto getCreados(int indice){
        return this.creados[indice];
    }

    public producto getBackup(int indice){
        return this.backup[indice];
    }





}
