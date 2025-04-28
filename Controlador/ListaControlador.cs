// Archivo: Controlador/ListaControlador.cs

using Modelo;

namespace Controlador
{
    public class ListaControlador
    {
        private ListaDoble lista;

        public ListaControlador()
        {
            lista = new ListaDoble();
        }

        public void InsertarAlInicio(int dato)
        {
            lista.InsertarInicio(dato);
        }

        public void InsertarAlFinal(int dato)
        {
            lista.InsertarFinal(dato);
        }

        public string Mostrar()
        {
            return lista.MostrarLista();
        }
    }
}
