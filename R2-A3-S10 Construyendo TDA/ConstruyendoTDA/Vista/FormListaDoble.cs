using System;
using System.Windows.Forms;
using Controlador;

public partial class FormListaDoble : Form
{
    private ListaControlador controlador;

    public FormListaDoble()
    {
        InitializeComponent();
        controlador = new ListaControlador();
    }

    private void btnInicio_Click(object sender, EventArgs e)
    {
        if (int.TryParse(txtDato.Text, out int dato))
        {
            controlador.AgregarAlInicio(dato);
            txtMostrar.Text = controlador.Mostrar();
            txtDato.Clear();
        }
    }

    private void btnFinal_Click(object sender, EventArgs e)
    {
        if (int.TryParse(txtDato.Text, out int dato))
        {
            controlador.AgregarAlFinal(dato);
            txtMostrar.Text = controlador.Mostrar();
            txtDato.Clear();
        }
    }
}
