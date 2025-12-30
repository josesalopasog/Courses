package utils;

import java.util.Scanner;

public class ScannerUtils {
    public static Scanner scanner = new Scanner(System.in); //Creates a static Scanner object named scanner, System.in tells the scanner to read the input from the console

    public static String getText(String message) {
        System.out.println(message + ": ");
        return scanner.nextLine();
    }

    public int getNumber(int number) {
        System.out.println(number + ": ");
        return scanner.nextInt();
    }
    public double getDouble(double number) {
        System.out.println(number + ":");
        return  scanner.nextDouble();
    }
}
