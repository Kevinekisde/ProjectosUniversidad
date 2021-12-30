public abstract class producto {
    private String nomprod;
    private int precio;
    private String MarcaProdu;
    private String tipo;
    public double total = 0;

    public producto(String valorNomProd,String ValorMarcaProdu,int Valorprecio,String ValorTipo){
        setNomprod(valorNomProd);
        setPrecio(Valorprecio);
        setMarcaProdu(ValorMarcaProdu);
    }


    public void MostrarProd(producto p){
        System.out.println("Nombre: " + p.getNomprod());
        System.out.println("Marca: " + p.getMarcaProdu());
        System.out.println("Tipo: " + p.getTipo());
        System.out.println("Precio: " + p.getPrecio());
        
    }


    public void armar(producto p1 , producto p2, producto p3, producto p4 , producto p5){
        System.out.println("Todos los componentes han sido ingresado se armara el computador.....");
        System.out.println("1." + " " + p1.nomprod+ " " + p1.MarcaProdu + " " + p1.tipo + " " + p1.precio );
        System.out.println("2." + " " + p2.nomprod + " " + p2.MarcaProdu+ " "  + p2.tipo+ " "  + p2.precio );
        System.out.println("3." + " " + p3.nomprod+ " "  + p3.MarcaProdu+ " "  + p3.tipo+ " "  + p3.precio );
        System.out.println("4." + " " + p4.nomprod+ " "  + p4.MarcaProdu+ " "  + p4.tipo + " " + p4.precio );
        System.out.println("5." + " " + p5.nomprod + " " + p5.MarcaProdu + " " + p5.tipo + " " + p5.precio );
        total = total + p1.precio;
        total = total + p2.precio;
        total = total + p3.precio;
        total = total + p4.precio;
        total = total + p5.precio;
        System.out.println("Precio final : " + total );
        }




 
    public String getNomprod() {
        return this.nomprod;
    }

    public void setNomprod(String nomprod) {
        this.nomprod = nomprod;
    }

    public int getPrecio() {
        return precio;
    }

    public void setPrecio(int precio) {
        this.precio = precio;
    }

    public String getMarcaProdu() {
        return MarcaProdu;
    }

    public void setMarcaProdu(String marcaProdu) {
        MarcaProdu = marcaProdu;
    }

    public String getTipo() {
        return tipo;
    }


    public void setTipo(String tipo) {
        this.tipo = tipo;
    }



    
}


    


    

    


        
