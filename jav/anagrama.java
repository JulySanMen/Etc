import java.util.Arrays;

public class Anagrama {
    public static boolean sonAnagramas(String palabra1, String palabra2) {
        
        if (palabra1.equals(palabra2)) {
            return false;
        }

        palabra1 = palabra1.toLowerCase();
        palabra2 = palabra2.toLowerCase();

        char[] array1 = palabra1.toCharArray();
        char[] array2 = palabra2.toCharArray();
        Arrays.sort(array1);
        Arrays.sort(array2);

        
        return Arrays.equals(array1, array2);
    }

    public static void main(String[] args) {
        System.out.println(sonAnagramas("amor", "roma"));  
        System.out.println(sonAnagramas("amor", "amora")); 
        System.out.println(sonAnagramas("amor", "amor"));  
    }
}