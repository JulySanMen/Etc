public class buslineal{
    public static void main(String[] args) {
        int[] numeros = {4, 2, 7, 1, 9, 3};
        int valorBuscado = 7;
        int indice = busquedaLineal(numeros, valorBuscado);

        if (indice != -1) {
            System.out.println("Valor encontrado en el índice: " + indice);
        } else {
            System.out.println("Valor no encontrado.");
        }
    }
    public static int busquedaLineal(int[] arreglo, int valor) {
        for (int i = 0; i < arreglo.length; i++) {
            if (arreglo[i] == valor) {
                return i;
            }
        }
        return -1;
    }
}
