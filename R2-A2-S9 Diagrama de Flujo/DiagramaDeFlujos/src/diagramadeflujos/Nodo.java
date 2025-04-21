/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package diagramadeflujos;

/**
 *
 * @author Owner
 */
// Clase Nodo que representa cada cliente en la lista doblemente enlazada
public class Nodo {
    int cedula;
    String nombre;
    Nodo siguiente;
    Nodo anterior;

    public Nodo(int cedula, String nombre) {
        this.cedula = cedula;
        this.nombre = nombre;
        this.siguiente = null;
        this.anterior = null;
    }
}

