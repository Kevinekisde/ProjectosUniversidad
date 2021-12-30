import java.util.Scanner;
public class Enano extends Personaje{
    private String clan;

    public Enano(String valorNombre, String valorRaza, String valorArma, int valorDano, int valorVida, String valorClan){
        super(valorNombre, valorRaza, valorArma, valorDano, valorVida);
        setClan(valorClan);
    }

    public void aumentaVida(){

    }

    @Override
    public String historia(){
        return "Los fuertes y tenaces Enanos, nacidos de las montañas, son reconocidos por su imponente arquitectura y codiciada habilidad en la mineria y herreria.";
    }

    public String victoria(){
        return "El enano ha ganado!";
    }

    public String derrota(){
        return "El enano ha sido aplastado. :(";
    }

    public void bonus(Personaje contrincante, boolean flag){
        if(flag){
            Scanner input = new Scanner(System.in);
            boolean verificado = false;
            while(verificado==false){
                System.out.println("Ingrese la bonificación de vida del enano(50-100):");
                System.out.print("-> ");
                int bonif = Integer.parseInt(input.nextLine());
                if(bonif>=50 && bonif<=100){
                    setVida(getVida()+bonif);
                    verificado = true;
                }
                else{System.out.println("La bonificación debe estar dentro del rango 50-100.");}
            }
        }     
    }

    // --------- Getters y setters ---------

    public String getClan() {
        return this.clan;
    }

    public void setClan(String clan) {
        this.clan = clan;
    }

}
