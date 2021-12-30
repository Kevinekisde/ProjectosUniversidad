package solemne2;

public class Estudiante {
    private String Nombre;
    private String RUT;
    private float notaSolemne1;
    private float notaSolemne2;
    private float notaSolemne3;
    private float promedioEjercicios;
    
    // ------------ Getters and setters ---------------
    public String getNombre() {
        return this.Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public String getRUT() {
        return this.RUT;
    }

    public void setRUT(String RUT) {
        this.RUT = RUT;
    }

    public float getNotaSolemne1() {
        return this.notaSolemne1;
    }

    public void setNotaSolemne1(float notaSolemne1) {
        this.notaSolemne1 = notaSolemne1;
    }

    public float getNotaSolemne2() {
        return this.notaSolemne2;
    }

    public void setNotaSolemne2(float notaSolemne2) {
        this.notaSolemne2 = notaSolemne2;
    }

    public float getNotaSolemne3() {
        return this.notaSolemne3;
    }

    public void setNotaSolemne3(float notaSolemne3) {
        this.notaSolemne3 = notaSolemne3;
    }

    public float getPromedioEjercicios() {
        return this.promedioEjercicios;
    }

    public void setPromedioEjercicios(float promedioEjercicios) {
        this.promedioEjercicios = promedioEjercicios;
    }
    // -------------------------------------------
    public float promedioNotas(){
        float ponderacion30 = (float)0.3;
        float ponderacion10 = (float)0.1; 
        return notaSolemne1*ponderacion30 + notaSolemne2*ponderacion30 + notaSolemne3*ponderacion30 + promedioEjercicios*ponderacion10;
    }

}
