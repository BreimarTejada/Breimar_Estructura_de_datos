/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package diagramadeflujos;

/**
 *
 * @author Owner
 */
import java.util.Scanner;

// Clase principal que ejecuta el programa y muestra el menú
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ListaDoble lista = new ListaDoble();
        int opcion;

        do {
            System.out.println("\n--- MENU ---");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Listar clientes hacia la derecha");
            System.out.println("3. Listar clientes hacia la izquierda");
            System.out.println("4. Salir");
            System.out.print("Elige una opcion: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese cedula del cliente: ");
                    int cedula = sc.nextInt();
                    sc.nextLine(); // Limpiar buffer
                    System.out.print("Ingrese nombre del cliente: ");
                    String nombre = sc.nextLine();
                    lista.insertarOrdenado(cedula, nombre);
                    break;
                case 2:
                    System.out.println("Clientes de izquierda a derecha:");
                    lista.listarDerecha();
                    break;
                case 3:
                    System.out.println("Clientes de derecha a izquierda:");
                    lista.listarIzquierda();
                    break;
                case 4:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opcion invalida.");
            }
        } while (opcion != 4);

        sc.close();
    }
}

