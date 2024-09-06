import java.text.*;
import java.util.*;
import java.util.Date;
 
public class fechas {
 
   public static void main(String args[]) {
     Date now = new Date();
 
     // Obtener los formateadores de fecha de los entornos nacionales
     // predeterminados, alemán y francés
     DateFormat theDate = DateFormat.getDateInstance(DateFormat.LONG);
     DateFormat germanDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.GERMANY);
     DateFormat frenchDate = DateFormat.getDateInstance(DateFormat.LONG, Locale.FRANCE);

     System.out.println("Fecha en el entorno nacional predeterminado: " + theDate.format(now));
     System.out.println("Fecha en el entorno nacional Alemán: " + germanDate.format(now));
     System.out.println("Fecha en el entorno nacional Francés: " + frenchDate.format(now));  
   } 
}