/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package diagramadeflujos;

/**
 *
 * @author Owner
 */
// Clase que administra la lista doblemente enlazada
public class ListaDoble {
    Nodo cabeza;

    // Inserta un cliente de forma ordenada por número de cédula
    public void insertarOrdenado(int cedula, String nombre) {
        Nodo nuevo = new Nodo(cedula, nombre);

        if (cabeza == null) {
            cabeza = nuevo;
        } else if (cedula < cabeza.cedula) {
            nuevo.siguiente = cabeza;
            cabeza.anterior = nuevo;
            cabeza = nuevo;
        } else {
            Nodo actual = cabeza;
            while (actual.siguiente != null && actual.siguiente.cedula < cedula) {
                actual = actual.siguiente;
            }
            nuevo.siguiente = actual.siguiente;
            if (actual.siguiente != null) {
                actual.siguiente.anterior = nuevo;
            }
            actual.siguiente = nuevo;
            nuevo.anterior = actual;
        }
    }

    // Lista los clientes desde el primero hasta el último
    public void listarDerecha() {
        Nodo actual = cabeza;
        if (actual == null) {
            System.out.println("Lista vacia.");
            return;
        }
        while (actual != null) {
            System.out.println("Cedula: " + actual.cedula + ", Nombre: " + actual.nombre);
            actual = actual.siguiente;
        }
    }

    // Lista los clientes desde el último hasta el primero
    public void listarIzquierda() {
        Nodo actual = cabeza;
        if (actual == null) {
            System.out.println("Lista vacía.");
            return;
        }
        while (actual.siguiente != null) {
            actual = actual.siguiente;
        }
        while (actual != null) {
            System.out.println("Cedula: " + actual.cedula + ", Nombre: " + actual.nombre);
            actual = actual.anterior;
        }
    }
}
