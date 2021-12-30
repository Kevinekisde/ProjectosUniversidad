public class Software extends producto{

    public Software(String valorNomProd,String ValorMarcaProdu,int Valorprecio,String ValorTipo){
        super(valorNomProd, ValorMarcaProdu, Valorprecio, ValorTipo);
    }

    public static String Agregar(){
        return "Se instalara el software seleccionado en su computadora";
    }
}