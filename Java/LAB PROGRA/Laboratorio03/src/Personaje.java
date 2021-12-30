public abstract class Personaje {
    private String nombre;
    private String raza;
    String arma;
    int dano;
    int vida;

    public Personaje(String valorNombre, String valorRaza, String valorArma, int valorDano, int valorVida){
        setNombre(valorNombre);
        setRaza(valorRaza);
        setArma(valorArma);
        setDano(valorDano);
        setVida(valorVida);     
    }

    public boolean muerto(Personaje p){
        if(p.getVida()<=0){
            return true;
        }
        else{
            return false;
        }
    }

    public void mostrarDatos(Personaje p){
        System.out.println("Nombre: " + p.getNombre());
        System.out.println("Raza: " + p.getRaza());
        System.out.println("Arma: " + p.getArma());
        System.out.println("Daño: " + p.getDano());
        System.out.println("Vida final: " + p.getVida());

    }

    public void mostrarGanador(Personaje p, String perdedor){
        System.out.println("El personaje "+ perdedor + " ha sido derrotado.");
        System.out.println("-------- GANADOR --------");
        mostrarDatos(p);
    }

    public void mostrarMensajes(int ganador, Personaje p1, Personaje p2){
        System.out.println("****************************");
        if(ganador==1){
            System.out.println(p1.victoria());
            System.out.println("----------------------------");
            System.out.println(p2.derrota());
        }

        if(ganador==2){
            System.out.println(p2.victoria()); 
            System.out.println("----------------------------");
            System.out.println(p1.derrota());
        }
        System.out.println("****************************");
    }

    public void combate(Personaje p1, Personaje p2){
        int contador = 0;
        boolean flag = true;
        int vidaP1temp = p1.getVida();
        int vidaP2temp = p2.getVida();
        while(contador<=10){
            p1.bonus(p2, flag);
            p2.bonus(p1, flag);
            // p1 ataca a p2
            p2.setVida(p2.getVida()-p1.getDano());
            if(muerto(p2)){
                mostrarGanador(p1,"2");
                mostrarMensajes(1, p1, p2);
                break;}
            // p2 ataca a p1
            p1.setVida(p1.getVida()-p2.getDano());
            if(muerto(p1)){
                mostrarGanador(p2, "1");
                mostrarMensajes(2, p1, p2);
                break;}
            if(contador==10){
                if(p1.getVida()>p2.getVida()){
                    mostrarGanador(p1, "2");
                    mostrarMensajes(1, p1, p2);
                    break;}
                if(p2.getVida()>p1.getVida()){
                    mostrarGanador(p2, "1");
                    mostrarMensajes(2, p1, p2);
                    break;}
                if(p1.getVida()<=0 && p2.getVida()<=0){
                    System.out.println("Empate :0");
                }
            }
            if(contador==0){
                flag = false;
            }
            contador++;
        }
        p1.setVida(vidaP1temp);
        p2.setVida(vidaP2temp);



    }

    // Métodos abstractos
    public abstract void bonus(Personaje contrincante, boolean flag);

    public abstract String historia();

    public abstract String victoria();

    public abstract String derrota();

    // --------- Getters y setters ---------

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getRaza() {
        return this.raza;
    }

    public void setRaza(String raza) {
        this.raza = raza;
    }

    public String getArma() {
        return this.arma;
    }

    public void setArma(String arma) {
        this.arma = arma;
    }

    public int getVida() {
        return this.vida;
    }

    public void setVida(int vida) {
        this.vida = vida;
    }

    public int getDano() {
        return this.dano;
    }

    public void setDano(int dano) {
        this.dano = dano;
    }   
}
