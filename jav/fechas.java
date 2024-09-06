import java.text.*;
import java.util.*;
import java.util.Date;
 
public class fechas {
 
   public static void main(String args[]) {
     Date now = new Date();
 
     DateFormat theDate = DateFormat.getDateInstance(DateFormat.LONG);
     DateFormat germanDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.GERMANY);
     DateFormat frenchDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.FRANCE);
     DateFormat italianDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.ITALY);
     DateFormat japaneseDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.JAPAN);
     DateFormat usDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.US);

     System.out.println("Fecha en el entorno nacional predeterminado: " + theDate.format(now));
     System.out.println("Fecha en el entorno nacional Alemán: " + germanDate.format(now));
     System.out.println("Fecha en el entorno nacional Francés: " + frenchDate.format(now));
     System.out.println("Fecha en el entorno nacional Italiano: " + italianDate.format(now));
     System.out.println("Fecha en el entorno nacional Japonés: " + japaneseDate.format(now));
     System.out.println("Fecha en el entorno nacional Estadounidense: " + usDate.format(now));  
   } 
}