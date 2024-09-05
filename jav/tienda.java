import java.util.Scanner;

public class tienda{
    public static void main(String[]args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el nombre del producto: ");
        String nombreProducto = scanner.nextLine();

        System.out.print("Ingrese precio del producto: ");
        double preciop = scanner.nextDouble();

        System.out.print("Ingrese la cantidad: ");
        int cant = scanner.nextInt();

        double totVenta = preciop * cant;

        System.out.println("**VENTA**");
        System.out.println(cant + " "+ nombreProducto +"  " + "$" + preciop + "  Total:" + totVenta);
        scanner.close();
    }
}