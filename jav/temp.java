// Calcularemos temperatura 
import java.util.Scanner;

public class temp{
    public static void main (String []args){
        Scanner temp = new Scanner(System.in);
        System.out.println("Ingrese temperatura en Celcius: ");
        double Celcius = temp.nextDouble();

        double Kelvin = 273.15 + Celcius;

        double Farenheit = 9/5. * Celcius + 32;

        double Rankine = 9/5. *(Celcius + 273.15);

        double Reaumur = 4/5. * Celcius;

        System.out.println(Celcius + " grados Celcius valen: ");
        System.out.println(Kelvin + " grados Kelvin");
        System.out.println(Farenheit + " grados Farenheit");
        System.out.println(Rankine + " grados Rankine");
        System.out.println(Reaumur + " grados Reaumur");


    }
}