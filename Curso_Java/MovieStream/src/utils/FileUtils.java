package utils;

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

    public static void writeData(Movie movie) {
        String line = String.join(SEPARATOR,
                movie.getTitle(),
                String.valueOf(movie.getDuration()),
                movie.getGenre().name(),
                movie.getDateOfPremiere().toString(),
                String.valueOf(movie.getScore())
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

    public static List<Movie> readData() {
        List<Movie> preloadedMovies = new ArrayList<>();
        try {
            List<String> lines = Files.readAllLines(Paths.get(MOVIES_FILE));
            lines.forEach(line -> {
                String[] data = line.split("\\" + SEPARATOR);

                if(data.length == 5){
                    String title = data[0];
                    int duration = Integer.parseInt(data[1]);
                    Genre genre = Genre.valueOf(data[2].toUpperCase());
                    double rate = data[3].isBlank() ? 0: Double.parseDouble(data[3]);
                    LocalDate dateOfPremiere = LocalDate.parse(data[4]);

                    Movie movie = new Movie(title, duration, genre, dateOfPremiere, rate);

                    preloadedMovies.add(movie);
                }
            });
        }catch(IOException e) {
            System.out.println("Error reading the file. " + e.getMessage());
        }

        return preloadedMovies;
    }
}
