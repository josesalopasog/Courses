package utils;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.Scanner;

public class ScannerUtils {
    public static final Scanner SCANNER = new Scanner(System.in); //Creates a static Scanner object named scanner, System.in tells the scanner to read the input from the console

    public static String getText(String message) {
        System.out.println(message + ": ");
        String text = SCANNER.nextLine();
        SCANNER.nextLine();
        return text;
    }

    public static int getNumber(String message) {
        System.out.println(message + ": ");
        int number = SCANNER.nextInt();
        SCANNER.nextLine();
        return number;
    }
    public static double getDouble(String message) {
        while (true) {
            try {
                System.out.print(message + ": ");
                String input = SCANNER.nextLine().replace(",", ".");
                return Double.parseDouble(input);
            } catch (NumberFormatException e) {
                System.out.println("❌ Valor inválido. Intente nuevamente.");
            }
        }
    }

    public static LocalDate getDate(String message){
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");

        LocalDate date = null;
        boolean valid = false;

        while(!valid){
            System.out.println(message + ": ");
            String inputDate = SCANNER.nextLine();

            try{
                date = LocalDate.parse(inputDate, formatter);
                valid = true;
            } catch (DateTimeParseException e) {
                System.out.println("❌ Enter a valid format");
            }
        }
        return date;
    }
}
