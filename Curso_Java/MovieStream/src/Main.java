import content.Movie;
import plataforma.Platform;
import plataforma.User;
import utils.ScannerUtils;

import java.time.LocalDate;

public class Main {
    public static final String APP_NAME = "MOVIE STREAM APP 🎬";
    public static final String VERSION = "1.0.0";

    public static void main(String[] args){
        Platform platform = new Platform(APP_NAME);
        System.out.println(APP_NAME + " v" + VERSION);

        loadSampleMovies(platform);

        while(true){
            int menuOption = ScannerUtils.getNumber("""
                    Menu:
                    1. Add a movie
                    2. Show all
                    3. Search by title
                    4. Remove movie
                    5. Exit
                    Write the number of your option >""");
            switch (menuOption){
                case 1:
                    String movieTitle = ScannerUtils.getText("Write name of the movie: ");
                    String movieGenre = ScannerUtils.getText("Write movie genre: ");
                    int movieDuration = ScannerUtils.getNumber("Write movie duration: ");
                    double movieRate = ScannerUtils.getDouble("Write movie rate: ");
                    LocalDate movieDateOfPremiere = ScannerUtils.getDate("Write Date of premiere of the movie (yyyy-MM-dd): ");

                    Movie movie = new Movie(movieTitle, movieDuration,movieGenre, movieDateOfPremiere, movieRate);

                    platform.addMovie(movie);
                    System.out.println("✅ Movie added!");
                    break;

                case 2:
                    platform.getAllTitles();
                    break;
                case 3:
                    String title = ScannerUtils.getText("Write title to search: ");
                    platform.searchByTitle(title);
                    break;
                case 4:
                    String removeTitle = ScannerUtils.getText("Write title to remove: ");
                    platform.removeByTitle(removeTitle);
                    break;
                case 5:
                    System.out.println("👋🏼 Closing app...");
                    return;
                default:
                    System.out.println("❌ Invalid option!");
            }
        }
    }

    private static void loadSampleMovies(Platform platform) {
        platform.addMovie(new Movie("Inception", 148, "Sci-Fi",
                LocalDate.of(2010, 7, 16), 8.8));

        platform.addMovie(new Movie("Interstellar", 169, "Sci-Fi",
                LocalDate.of(2014, 11, 7), 8.6));

        platform.addMovie(new Movie("The Dark Knight", 152, "Action",
                LocalDate.of(2008, 7, 18), 9.0));

        platform.addMovie(new Movie("Gladiator", 155, "Drama",
                LocalDate.of(2000, 5, 5), 8.5));

        platform.addMovie(new Movie("Parasite", 132, "Thriller",
                LocalDate.of(2019, 5, 30), 8.6));
    }
}

// Class of objects and classes