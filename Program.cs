// Archivo: Program.cs

using System;
using Controlador;

class Program
{
    static void Main(string[] args)
    {
        ListaControlador controlador = new ListaControlador();
        int opcion;

        do
        {
            Console.WriteLine("\n--- Lista doble enlazada ---");
            Console.WriteLine("1. Insertar al inicio");
            Console.WriteLine("2. Insertar al final");
            Console.WriteLine("3. Mostrar lista");
            Console.WriteLine("4. Salir");
            Console.Write("Elige una opción: ");
            int.TryParse(Console.ReadLine(), out opcion);

            switch (opcion)
            {
                case 1:
                    Console.Write("Ingresa un número: ");
                    int datoInicio;
                    int.TryParse(Console.ReadLine(), out datoInicio);
                    controlador.InsertarAlInicio(datoInicio);
                    break;

                case 2:
                    Console.Write("Ingresa un número: ");
                    int datoFinal;
                    int.TryParse(Console.ReadLine(), out datoFinal);
                    controlador.InsertarAlFinal(datoFinal);
                    break;

                case 3:
                    Console.WriteLine("\nLista actual:");
                    Console.WriteLine(controlador.Mostrar());
                    break;

                case 4:
                    Console.WriteLine("Saliendo...");
                    break;

                default:
                    Console.WriteLine("Opción no válida.");
                    break;
            }
        } while (opcion != 4);
    }
}
