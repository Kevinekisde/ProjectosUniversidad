package solemne2;

import java.util.Scanner;

public class Datos {
    private Estudiante baseDatos[] = new Estudiante[35];

    public Estudiante getBaseDatos(int indice){
        return this.baseDatos[indice];
    }

    public void ingresarDatos(int indice){
        Estudiante estudiante = new Estudiante();
        baseDatos[indice] = estudiante; 

        Scanner input = new Scanner(System.in);

        System.out.println("Ingrese el nombre:");
        String nombre = input.nextLine();
        baseDatos[indice].setNombre(nombre);

        System.out.println("Ingrese el RUT:");
        String rut = input.nextLine();
        baseDatos[indice].setRUT(rut); 

        System.out.println("Ingrese las notas del estudiante:");
        System.out.println("Solemne 1: ");
        float solemne1 = input.nextFloat();
        baseDatos[indice].setNotaSolemne1(solemne1);

        System.out.println("Solemne 2: ");
        float solemne2 = input.nextFloat();
        baseDatos[indice].setNotaSolemne2(solemne2);

        System.out.println("Solemne 3: ");
        float solemne3 = input.nextFloat();
        baseDatos[indice].setNotaSolemne3(solemne3);

        System.out.println("Promedio ejercicios: ");
        float ejercicios = input.nextFloat();
        baseDatos[indice].setPromedioEjercicios(ejercicios);
    }
    
    public void mostrarDatos(int indice){
        System.out.println("------------------");
        System.out.println("Nombre: " + baseDatos[indice].getNombre());
        System.out.println("RUT: " + baseDatos[indice].getRUT());
        System.out.println("--- Notas ---");
        System.out.println("Solemne 1: " + baseDatos[indice].getNotaSolemne1());
        System.out.println("Solemne 2: " + baseDatos[indice].getNotaSolemne2());
        System.out.println("Solemne 3: " + baseDatos[indice].getNotaSolemne3());
        System.out.println("Ejercicios: " + baseDatos[indice].getPromedioEjercicios());
        System.out.println("Promedio final: " + baseDatos[indice].promedioNotas());
        System.out.println("------------------");

    }

    public void mostrarEstudiante(String rut){
        for(int i=0;i<baseDatos.length;i++){
            if(baseDatos[i]!=null){
                if(baseDatos[i].getRUT().equals(rut)){
                    mostrarDatos(i);
                    }
            }
        }

    }

    public void mostrarTodo(){
        for(int i=0;i<baseDatos.length;i++){
            if(baseDatos[i]!=null){
                mostrarDatos(i);
            }
        }
    }

    public void promedioGeneral(){
        float sumaSolemne1=0, sumaSolemne2=0, sumaSolemne3=0, sumaEjercicios=0, contador=0;
        for(int i=0;i<baseDatos.length;i++){
            if(baseDatos[i]!=null){
                sumaSolemne1 = sumaSolemne1 + baseDatos[i].getNotaSolemne1();
                sumaSolemne2 = sumaSolemne2 + baseDatos[i].getNotaSolemne2();
                sumaSolemne3 = sumaSolemne3 + baseDatos[i].getNotaSolemne3();
                sumaEjercicios = sumaEjercicios + baseDatos[i].getPromedioEjercicios();
                contador++;
            }
        }
        System.out.println("Promedio general Solemne 1: " + sumaSolemne1/contador);
        System.out.println("Promedio general Solemne 2: " + sumaSolemne2/contador);
        System.out.println("Promedio general Solemne 3: " + sumaSolemne3/contador);
        System.out.println("Promedio general Ejercicios: " + sumaEjercicios/contador);
    }
    
}
