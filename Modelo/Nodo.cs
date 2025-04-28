// Archivo: Modelo/Nodo.cs

namespace Modelo
{
    public class Nodo
    {
        public int Dato { get; set; }
        public Nodo Anterior { get; set; }
        public Nodo Siguiente { get; set; }

        public Nodo(int dato)
        {
            Dato = dato;
            Anterior = null;
            Siguiente = null;
        }
    }
}
