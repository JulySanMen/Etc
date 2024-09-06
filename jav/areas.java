import java.util.Scanner;

public class areas{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        System.out.println("Selecciona la forma para calcular el área:");
        System.out.println("1. Círculo");
        System.out.println("2. Cuadrado");
        System.out.println("3. Rectángulo");
        System.out.println("4. Triang Triángulo Isóscelesulo");
        System.out.println("5. Triángulo Isósceles")
        System.out.println("6. Triángulo Equilátero")
        System.out.print("otro: ");
        opcion = scanner.nextInt();

        switch (opcion) {
            case 1:
                // Área de un Círculo: A = π * r^2
                System.out.print("Ingresa el radio del círculo: ");
                double radio = scanner.nextDouble();
                double areaCirculo = Math.PI * Math.pow(radio, 2);
                System.out.println("El área del círculo es: " + areaCirculo);
                break;

            case 2:
                // Área de un Cuadrado: A = lado^2
                System.out.print("Ingresa el lado del cuadrado: ");
                double lado = scanner.nextDouble();
                double areaCuadrado = Math.pow(lado, 2);
                System.out.println("El área del cuadrado es: " + areaCuadrado);
                break;

            case 3:
                // Área de un Rectángulo: A = base * altura
                System.out.print("Ingresa la base del rectángulo: ");
                double base = scanner.nextDouble();
                System.out.print("Ingresa la altura del rectángulo: ");
                double altura = scanner.nextDouble();
                double areaRectangulo = base * altura;
                System.out.println("El área del rectángulo es: " + areaRectangulo);
                break;
            
            case 4:
                // Área de un Triángulo: A = (base * altura) / 2
                System.out.print("Ingresa la base del triángulo: ");
                double baseTri = scanner.nextDouble();
                System.out.print("Ingresa la altura del triángulo: ");
                double alturaTri = scanner.nextDouble();
                double areaTriangulo = (baseTri * alturaTri) / 2;
                System.out.println("El área del triángulo es: " + areaTriangulo);
                break;

            case 5:
                // Área de un Triángulo Isósceles
                System.out.print("Ingresa la base del triángulo isósceles: ");
                double baseIso = scanner.nextDouble();
                System.out.print("Ingresa la longitud de los lados iguales del triángulo: ");
                double ladoIso = scanner.nextDouble();
                
                // Calcular la altura usando Pitágoras
                double alturaIso = Math.sqrt(Math.pow(ladoIso, 2) - Math.pow(baseIso / 2, 2));
                double areaIsosceles = (baseIso * alturaIso) / 2;
                System.out.println("El área del triángulo isósceles es: " + areaIsosceles);
                break;
            
            case 6:
                // Área de un Triángulo Equilátero: A = (sqrt(3) / 4) * l^2
                System.out.print("Ingresa la longitud de un lado del triángulo equilátero: ");
                double ladoEquilatero = scanner.nextDouble();
                double areaEquilatero = (Math.sqrt(3) / 4) * Math.pow(ladoEquilatero, 2);
                System.out.println("El área del triángulo equilátero es: " + areaEquilatero);
                break;
            

            default:
                System.out.println("Opción no válida. Por favor, selecciona una opción del 1 al 3.");
        }

        scanner.close();
    }
}
