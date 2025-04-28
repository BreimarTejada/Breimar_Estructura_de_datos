using Modelo;

public class ListaControlador
{
    private ListaDoble lista;

    public ListaControlador()
    {
        lista = new ListaDoble();
    }

    public void AgregarAlInicio(int dato)
    {
        lista.InsertarAlInicio(dato);
    }

    public void AgregarAlFinal(int dato)
    {
        lista.InsertarAlFinal(dato);
    }

    public string Mostrar()
    {
        return lista.MostrarAdelante();
    }
}
