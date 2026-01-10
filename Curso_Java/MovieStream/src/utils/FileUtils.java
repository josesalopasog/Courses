package utils;

import content.Content;
import content.Genre;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class FileUtils {

    public static final String MOVIES_FILE = "movies.txt";
    public static final String SEPARATOR = "|";

    public static void writeData(Content content) {
        String line = String.join(SEPARATOR,
                content.getTitle(),
                String.valueOf(content.getDuration()),
                content.getGenre().name(),
                content.getDateOfPremiere().toString(),
                String.valueOf(content.getScore())
        );
        try{
            Files.writeString(Paths.get(MOVIES_FILE),
                    line + System.lineSeparator(),
                    StandardOpenOption.CREATE,
                    StandardOpenOption.APPEND

            );
        } catch (IOException e) {
            System.out.println("Error loading the file" + e.getMessage());
        }
    }

    public static List<Content> readData() {
        List<Content> preloadedContents = new ArrayList<>();
        try {
            List<String> lines = Files.readAllLines(Paths.get(MOVIES_FILE));
            lines.forEach(line -> {
                String[] data = line.split("\\" + SEPARATOR);

                if(data.length == 5){
                    String title = data[0];
                    int duration = Integer.parseInt(data[1]);
                    Genre genre = Genre.valueOf(data[2].toUpperCase());
                    LocalDate dateOfPremiere = LocalDate.parse(data[3]);
                    double rate = data[3].isBlank() ? 0: Double.parseDouble(data[4]);

                    Content content = new Content(title, duration, genre, dateOfPremiere, rate);

                    preloadedContents.add(content);
                }
            });
        }catch(IOException e) {
            System.out.println("Error reading the file. " + e.getMessage());
        }

        return preloadedContents;
    }
}
