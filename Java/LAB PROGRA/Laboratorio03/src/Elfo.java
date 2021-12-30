public class Elfo extends Personaje{
    private String reino;

    public Elfo(String valorNombre, String valorRaza, String valorArma, int valorDano, int valorVida, String ValorReino){
        super(valorNombre, valorRaza, valorArma, valorDano, valorVida);
        setReino(ValorReino);
    }

    public void quitaVida(){

    }

    @Override
    public String historia(){
        return "Los habilosos e inteligentes Elfos fueron los primeros en habitar el planeta, reconocidos por sus afinados sentidos. Los Elfos se enaltecen a ellos mismos por ser la raza mas pura de los reinos.";
    }

    public String victoria(){
        return "El elfo ha demostrado su superioridad.";
    }

    public String derrota(){
        System.out.println("Al parecer el elfo tiene mucho cerebro, pero pocos músculos.");
        return historia();
    }
    public void bonus(Personaje contrincante, boolean flag){
        if(flag){
            int porcentaje = contrincante.getVida()/10;
            contrincante.setVida(contrincante.getVida()-porcentaje);
        }

    }

    // --------- Getters y setters ---------

    public String getReino() {
        return this.reino;
    }

    public void setReino(String reino) {
        this.reino = reino;
    }

}
