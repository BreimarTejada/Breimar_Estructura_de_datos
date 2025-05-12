# 🔹 Métodos de Ordenamiento
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def busqueda_secuencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return f"Elemento encontrado en la posición {i}"
    return "Elemento no encontrado"

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quicksort(menores) + iguales + quicksort(mayores)

# 🔹 Menú de Opciones
def mostrar_menu():
    print("\nMenú de Ordenamiento")
    print("1. Método Burbuja")
    print("2. Método Secuencial (Búsqueda)")
    print("3. Método Quicksort")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")
    return opcion

# 🔹 Lógica Principal del Programa
def main():
    lista_original = [7, 2, 9, 1, 5, 10, 3, 8, 6, 4]

    
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            print("\nLista Original:", lista_original)
            print("Ordenada con Burbuja:", burbuja(lista_original.copy()))
        elif opcion == "2":
            elemento = int(input("Ingresa el número a buscar: "))
            print(busqueda_secuencial(lista_original, elemento))
        elif opcion == "3":
            print("\nLista Original:", lista_original)
            print("Ordenada con Quicksort:", quicksort(lista_original.copy()))
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# 🔹 Ejecutar el programa
if __name__ == "__main__":
    main()