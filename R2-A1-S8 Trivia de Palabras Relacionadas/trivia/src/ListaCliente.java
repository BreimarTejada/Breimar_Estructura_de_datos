//lista enlazada simple con inserccion ordenada

Public class ListaCliente {
    Private Nodo cabeza;

    //insertar el cliente por orden de cedula
   Public void InsertarOrdenado(Cliente cliente){
    Nodo nuevo = new Nodo(cliente);

    if(cabeza ==null || cliente.cedula.compareTo(cabeza.cliente.cedula) < 0){
        nuevo.siguiente = cabeza;
        cabeza = nuevo;
    } else {
        Nodo actual = cabeza;
        while (actual.siguiente != null && actual.siguiente.cliente.cedula.compareTo(cliente.cedula) < 0){
            actual = actual.siguiente;
    
        }
        nuevo.siguiente = actual.siguiente;
        actual.siguiente = nuevo;
    }
   }
   //muestra los clientes desde el primer nodo hasta el ultimo
   Public void ListarClientes(){
    if (cabeza == null){
        System.out.println("la lista esta vacia");
    }else {
        Nodo actual = cabeza;
        while (actual != null){
            System.out.println(actual.cliente);
            actual = actual.siguiente;
        }
    }
   }
}