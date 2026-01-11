package utils;

import content.Content;
import content.Documentary;
import content.Genre;
import content.Movie;

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

        String finalLine;

        if (content instanceof Documentary documentary){
            finalLine = "DOCUMENTARY" + SEPARATOR + line + SEPARATOR + documentary.getNarrator();
        } else{
            finalLine = "MOVIE" + SEPARATOR +  line;
        }

        try{
            Files.writeString(Paths.get(MOVIES_FILE),
                    finalLine + System.lineSeparator(),
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

                String contentType = data[0];

                if(("MOVIE".equals(contentType) && data.length == 6) || ("DOCUMENTARY".equals(contentType) && data.length == 7)){
                    String title = data[1];
                    int duration = Integer.parseInt(data[2]);
                    Genre genre = Genre.valueOf(data[3].toUpperCase());
                    LocalDate dateOfPremiere = LocalDate.parse(data[4]);
                    double rate = data[4].isBlank() ? 0: Double.parseDouble(data[5]);

                    Content content;

                    if("MOVIE".equals(contentType)){
                        content = new Movie(title,duration,genre,dateOfPremiere,rate);
                    }else{
                        String narrator = data[6];
                        content = new Documentary(title,duration,genre,dateOfPremiere,rate,narrator);
                    }

                    preloadedContents.add(content);
                }
            });
        }catch(IOException e) {
            System.out.println("Error reading the file. " + e.getMessage());
        }

        return preloadedContents;
    }
}
