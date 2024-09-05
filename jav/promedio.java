import java.util.Scanner;

public class ArregloEjemplo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Cantidad de numeros que desea ingresar...");
        int n = scanner.nextInt();
        int[] num = new int[n];
        System.out.println("Ingrese esos numeros:");
        for(int i=0;i<n;i++){
            System.out.print("Numero "+(i + i)+ ":");
            num[i] = scanner.nextInt();
        }
        int suma = 0;
        for(int i=0;i<n;i++){
            suma += num[i];
        }
        double promedio = (double)suma/n;
        System.out.println("Suma = " + suma );
        System.out.println("Promedio = " + promedio);
        scanner.close();
    }
}
