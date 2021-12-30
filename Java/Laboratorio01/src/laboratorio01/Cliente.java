package laboratorio01;

public class Cliente {
    private String nombre;
    private int tiempoConexion;
    private String tipoPlan;
    private int montoTotal;

    // Atributos (ver y modificar) ------------------------
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getTiempoConexion() {
        return this.tiempoConexion;
    }

    public void setTiempoConexion(int tiempoConexion) {
        this.tiempoConexion = tiempoConexion;
    }

    public String getTipoPlan() {
        return this.tipoPlan;
    }

    public void setTipoPlan(String tipoPlan) {
        this.tipoPlan = tipoPlan;
    }

    public int getMontoTotal() {
        return this.montoTotal;
    }

    public void setMontoTotal(int montoTotal) {
        this.montoTotal = montoTotal;
    }

    public void mostrarDatos(Plan x) {
        int costoTotal = x.getCostoMantencion()+x.getCostoMinuto()*tiempoConexion;
        System.out.println("------------ Datos cliente ------------");
        System.out.println("Nombre: "+getNombre());
        System.out.println("Tipo de plan: "+getTipoPlan());
        System.out.println("Costo de mantención: $"+x.getCostoMantencion());
        System.out.println("Costo por minuto: $"+x.getCostoMinuto());
        System.out.println("Minutos utilizados: "+getTiempoConexion());
        System.out.println("Costo total: $"+ costoTotal);
        System.out.println("---------------------------------------"); 
    }

}
