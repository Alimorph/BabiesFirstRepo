package FizzBuzz;

public class FizzBuzz {
    private static String buzz = "Buzz";
    private static String fizz = "Fizz";

    public static void main(String[] args) throws Exception {
        for (int i = 1; i <= 100; i++) {
            System.out.print(String.valueOf(i));
            if (i%15==0)
                System.out.print(String.valueOf(": ")+fizz+buzz);
            else if (i%3==0)
                System.out.print(String.valueOf(": ")+fizz);
            else if (i%5==0)
                System.out.print(String.valueOf(": ")+buzz);
            System.out.println();
        }
    }
}