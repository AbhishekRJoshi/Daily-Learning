public class Recursion {
    public static void main (String[] args){
        System.out.println(reverseString("Hello"));
    }

    public static String reverseString(String s){
        //Base Condition
        if(s.length() <= 1){
          return s;
        }
        // Smallest amount of work.
        return reverseString(s.substring(1)) + s.charAt(0);
    }
}
