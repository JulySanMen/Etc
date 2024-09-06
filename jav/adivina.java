import java.util.Scanner;
import java.util.Random;

public class adivina {

    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        int numeroAleatorio = random.nextInt(100) + 1; 
        int intento = 0;
        int numeroUsuario;

        System.out.println("Adivina el número (entre 1 y 100)");

        do {
            System.out.print("Ingresa tu número: ");
            numeroUsuario = scanner.nextInt();
            intento++;

            if (numeroUsuario < numeroAleatorio) {
                System.out.println("El número es mayor.");
            } else if (numeroUsuario > numeroAleatorio) {
                System.out.println("El número es menor.");
            } else {
                System.out.println("¡Correcto! Adivinaste el número en " + intento + " intentos.");
            }

        } while (numeroUsuario != numeroAleatorio);

        scanner.close();
    }
}
