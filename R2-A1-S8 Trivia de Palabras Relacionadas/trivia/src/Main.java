import java.util.Scanner;

Public Class Main {
    Public Static Void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        ListaCliente lista = new ListaCliente();
        int opcion; 

        do{
            System.out.println("\n--- Menu de opciones ---");
            System.out.println("1. Instertar cliente");
            System.out.println("2. Listar clientes hacia la derecha");
            System.out.println("3. Salir");
            System.out.println("Seleccione una opcion: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); //limpiar buffer

            switch (opcion)   {
                case 1:
                System.out.print("Ingrese la cedula del cliente: ");
                String cedula = scanner.nextLine();
                System.out.print("Ingrese el nombre del cliente: ");
                String nombre = scanner.nextLine();
                lista.InsertarOrdenado(new Cliente(cedula, nombre));
                break;
                
                case 2:
                System.out.println("\n Lista de clientes");
                lista.ListarClientes();
                break;

                case 3:
                System.out.println("Saliendo del programa...");
                break;

                default:
                System.out.println("Opcion invalida. Intente nuevamente.");
            }
        }while (opcion != 3);
    }
}

