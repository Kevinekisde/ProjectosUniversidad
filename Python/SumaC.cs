using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SumaC : MonoBehaviour
{
    public int myInteger = 5;
    public int myInteger2 = 10;
    public float myFloat = 3.5f;
    public bool myBoolean = true;
    public string myString = "Hello world";

    public int myArrayOfInts;

    private int myPrivateInteger = 10 ;
    float _myPrivateFloat= -5.0f;


    void start()
    {
        // OPERADORES 
        // Matematicas : + - * / %
        // % es modulo retorna el resto de una division
        Debug.log("Vamos a sumar 10 a myInteger.Ahora mismo el valor es :" + myInteger);
        myInteger = myInteger + 10;
        debug.log("Despues de la suma el valor es de :" + myInteger );

        Debug.log("Sumando dos numeros:");
        Myinteger = Myinteger + myInteger2;
        debug.log("la suma es de " + myInteger);
    }

    void Mydebug(string messege)
    {
        debug.log(messege);
    }
}
