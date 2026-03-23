public class Main {

    public static void main(String[] args) {
        double numA = 10.00;
        int numB = 3;
        double total = calculateTotal(numA, numB);
        System.out.println("Your double total is: " + total);

        int int_total = (int) total; 
        System.out.println("Your total is: " + int_total);

        //String numC = "pippo";
        //int numD = 3;
        //double badTotal = calculateTotal(numC, numD); 
        //System.out.println("Your total is: " + badTotal);
    }

    public static double calculateTotal(double pluto, int quantity) {
        return pluto * quantity;
    }
}