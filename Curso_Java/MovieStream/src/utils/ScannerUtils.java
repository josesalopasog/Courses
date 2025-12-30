package utils;

import java.util.Scanner;

public class ScannerUtils {
    public static Scanner scanner = new Scanner(System.in); //Creates a static Scanner object named scanner, System.in tells the scanner to read the input from the console

    public static String getText(String message) {
        System.out.println(message + ": ");
        String text = scanner.nextLine();
        scanner.nextLine();
        return text;
    }

    public static int getNumber(String message) {
        System.out.println(message + ": ");
        int number = scanner.nextInt();
        scanner.nextLine();
        return number;
    }
    public static double getDouble(String message) {
        while (true) {
            try {
                System.out.print(message + ": ");
                String input = scanner.nextLine().replace(",", ".");
                return Double.parseDouble(input);
            } catch (NumberFormatException e) {
                System.out.println("❌ Valor inválido. Intente nuevamente.");
            }
        }
    }
}
