package laboratorio02;

import java.util.Arrays;
import java.util.Scanner;

public class Vector {
    private final int size=10;
    private int arreglo0[] = new int[size];
    private int arreglo1[] = new int[size];
    private int arreglo2[] = new int[size];
    private int arreglo3[] = new int[size];

    public void cuadradoPosicion(){
        for(int i=0;i<size;i++){
            arreglo0[i] = i*i;
        }
       
    }

    public void numerosPares(){
        for(int i=0;i<size;i++){
            arreglo1[i]=(i+1)*2;
        }
    }

    public void numeroImpares(){
        Scanner input = new Scanner(System.in);
        int posicion = 0;
        while(posicion<size){
            System.out.println("Ingrese un número impar: ");
            int numero = input.nextInt();
            if(numero%2 != 0){
                arreglo2[posicion] = numero;
                posicion++;
            }
            else{
                System.out.println("El número ingresado no es impar.");
            }
        }
    }

    public void sumaAB(){ 
        if(arreglo0[1]==1&&arreglo1[1]==4){                  //No supimos como hacer que realmente nos arrojara un error.
            for(int i=0;i<size;i++){
                arreglo3[i] = arreglo0[i]+arreglo1[i];
            }            
        }
        else{
            System.out.println("Error: Los vectores A y/o B aún no han sido creados.");
            System.out.println("*********************************************************"); 
        }

    }

    public void mostrarDatosA(){ 
        if(arreglo0[1]!=0){                                 //No supimos como hacer que realmente nos arrojara un error.
            System.out.println("**** Vector A ****");
            System.out.println(Arrays.toString(arreglo0));
            System.out.println("*********************************************************");
        }
        else{
            System.out.println("Error: El vector no ha sido creado.");
            System.out.println("*********************************************************"); 
        }
    }

    public void mostrarDatosB(){ 
        if(arreglo0[1]!=0){                                 //No supimos como hacer que realmente nos arrojara un error.
            System.out.println("**** Vector B ****");
            System.out.println(Arrays.toString(arreglo1));
            System.out.println("*********************************************************");
        }
        else{
            System.out.println("Error: El vector no ha sido creado.");
            System.out.println("*********************************************************"); 
        }
    }

    public void mostrarDatosC(){ 
        if(arreglo0[1]!=0){                                 //No supimos como hacer que realmente nos arrojara un error.
            System.out.println("**** Vector C ****");
            System.out.println(Arrays.toString(arreglo2));
            System.out.println("*********************************************************");
        }
        else{
            System.out.println("Error: El vector no ha sido creado.");
            System.out.println("*********************************************************"); 
        }
    }

    public void mostrarDatosD(){ 
        if(arreglo0[1]!=0){                                 //No supimos como hacer que realmente nos arrojara un error.
            System.out.println("**** Vector D ****");
            System.out.println(Arrays.toString(arreglo3));
            System.out.println("*********************************************************");
        }
        else{
            System.out.println("Error: El vector no ha sido creado.");
            System.out.println("*********************************************************"); 
        }
    }
    
}
