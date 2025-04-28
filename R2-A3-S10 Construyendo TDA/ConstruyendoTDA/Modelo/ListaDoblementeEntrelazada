public class ListaDoble
{
    private Nodo cabeza;

    public ListaDoble()
    {
        cabeza = null;
    }

    public void InsertarAlInicio(int dato)
    {
        Nodo nuevo = new Nodo(dato);
        if (cabeza != null)
        {
            nuevo.Siguiente = cabeza;
            cabeza.Anterior = nuevo;
        }
        cabeza = nuevo;
    }

    public void InsertarAlFinal(int dato)
    {
        Nodo nuevo = new Nodo(dato);
        if (cabeza == null)
        {
            cabeza = nuevo;
            return;
        }

        Nodo temp = cabeza;
        while (temp.Siguiente != null)
            temp = temp.Siguiente;

        temp.Siguiente = nuevo;
        nuevo.Anterior = temp;
    }

    public string MostrarAdelante()
    {
        Nodo temp = cabeza;
        string resultado = "";
        while (temp != null)
        {
            resultado += temp.Dato + " <-> ";
            temp = temp.Siguiente;
        }
        return resultado.TrimEnd(' ', '<', '-', '>');
    }
}
