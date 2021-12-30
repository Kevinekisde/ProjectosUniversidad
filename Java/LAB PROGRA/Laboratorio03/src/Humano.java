import java.util.Scanner;

public class Humano extends Personaje{
    private String casta;

    public Humano(String valorNombre, String valorRaza, String valorArma, int valorDano, int valorVida, String valorCasta){
        super(valorNombre, valorRaza, valorArma, valorDano, valorVida);
        setCasta(valorCasta);
    }

    public void superBono(){

    }

    @Override
    public String historia(){
        return "Los valientes y polivalentes Humanos fueron los ultimos en habitar el planeta, son reconocidos por su gran ambicion y habilidad para la guerra. Dado esto y su adaptabilidad han logrado predominar en la historia.";
    }

    public String victoria(){
        return "El humano ha demostrado quien manda!";
    }

    public String derrota(){
        Scanner input = new Scanner(System.in);
        System.out.print("Arma: ");
        setArma(input.nextLine());
        return "En un intento desesperado el humano cambia su arma, pero está muy débil para continuar";
    }

    public void bonus(Personaje contrincante, boolean flag){
        if(flag){
            Scanner input = new Scanner(System.in);
            boolean verificado = false;
            while(verificado==false){
                System.out.println("Ingrese la bonificación de daño del humano (5-15): ");
                System.out.print("-> ");
                int bonif = Integer.parseInt(input.nextLine());
                if(bonif>=5 && bonif<=15){
                    setDano(getDano()+bonif);
                    verificado = true;
                }
            }
        }
        else{
            contrincante.setVida(contrincante.getVida()-1);
        }
    }

    // --------- Getters y setters ---------

    public String getCasta() {
        return this.casta;
    }

    public void setCasta(String casta) {
        this.casta = casta;
    }
    
}
