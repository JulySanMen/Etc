import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class fibonachi {
    public static List<Integer> fibonachi(int n) {
        List<Integer> secuencia = new ArrayList<>();
        int a = 0, b = 1;
        
        for (int i = 0; i < n; i++) {
            secuencia.add(a);
            int temp = a;
            a = b;
            b = temp + b;
        }
        
        return secuencia;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa la cantidad de números de Fibonacci que deseas ver: ");
        int n = scanner.nextInt();
        
        List<Integer> resultado = fibonachi(n);
        System.out.println(resultado);
        
        scanner.close();
    }
}