// Archivo: Modelo/ListaDoble.cs

namespace Modelo
{
    public class ListaDoble
    {
        public Nodo Inicio { get; private set; }
        public Nodo Fin { get; private set; }

        public ListaDoble()
        {
            Inicio = null;
            Fin = null;
        }

        public void InsertarInicio(int dato)
        {
            Nodo nuevo = new Nodo(dato);

            if (Inicio == null)
            {
                Inicio = Fin = nuevo;
            }
            else
            {
                nuevo.Siguiente = Inicio;
                Inicio.Anterior = nuevo;
                Inicio = nuevo;
            }
        }

        public void InsertarFinal(int dato)
        {
            Nodo nuevo = new Nodo(dato);

            if (Fin == null)
            {
                Inicio = Fin = nuevo;
            }
            else
            {
                Fin.Siguiente = nuevo;
                nuevo.Anterior = Fin;
                Fin = nuevo;
            }
        }

        public string MostrarLista()
        {
            string resultado = "";
            Nodo actual = Inicio;

            while (actual != null)
            {
                resultado += actual.Dato + " <-> ";
                actual = actual.Siguiente;
            }

            return resultado + "null";
        }
    }
}
