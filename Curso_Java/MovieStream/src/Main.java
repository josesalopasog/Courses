import content.Genre;
import content.Movie;
import content.SummaryContent;
import plataforma.Platform;
import plataforma.User;
import utils.FileUtils;
import utils.ScannerUtils;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.LocalDate;
import java.util.List;

public class Main {
    public static final String APP_NAME = "MOVIE STREAM APP 🎬";
    public static final String VERSION = "1.0.0";

    public static void main(String[] args){
        Platform platform = new Platform(APP_NAME);
        System.out.println(APP_NAME + " v" + VERSION);

        loadSampleMovies(platform);

        System.out.println("Content in this app: " + platform.getTotalDuration() + "min to watch! \n");

        while(true){
            int menuOption = ScannerUtils.getNumber("""
                    Menu:
                    1. Add a movie
                    2. Show all
                    3. Search by title
                    4. Remove movie
                    5. Search by genre
                    6. View Populars
                    7. Play Move
                    8. Exit
                    Write the number of your option >""");
            switch (menuOption){
                case 1:
                    String movieTitle = ScannerUtils.getText("Write name of the movie: ");
                    Genre movieGenre = ScannerUtils.getGenre("Write movie genre: ");
                    int movieDuration = ScannerUtils.getNumber("Write movie duration: ");
                    double movieRate = ScannerUtils.getDouble("Write movie rate: ");
                    LocalDate movieDateOfPremiere = ScannerUtils.getDate("Write Date of premiere of the movie (yyyy-MM-dd): ");

                    Movie movie = new Movie(movieTitle, movieDuration,movieGenre, movieDateOfPremiere, movieRate);

                    platform.addMovie(movie);
                    System.out.println("✅ Movie added!");
                    break;

                case 2:
                    List<SummaryContent> moviesSummary = platform.getSummaries();
                    moviesSummary.forEach(summary -> System.out.println(summary.toString()));
                    break;
                case 3:
                    String title = ScannerUtils.getText("Write title to search ");
                    platform.searchByTitle(title);
                    break;
                case 4:
                    String removeTitle = ScannerUtils.getText("Write title to remove ");
                    platform.removeByTitle(removeTitle);
                    break;
                case 5:
                    Genre genreToSearch = ScannerUtils.getGenre("Write the genre of the movies ");
                    List<Movie> listOfMoviesByGenre = platform.searchByGenre(genreToSearch);

                    if(listOfMoviesByGenre.isEmpty()){
                        System.out.println("No movies found by genre " + genreToSearch);
                    }else{
                        listOfMoviesByGenre.forEach(movieByGenre -> System.out.println(movieByGenre.getDatasheet()));
                    }
                    break;
                case 6:
                    List<Movie> moviesSorted = platform.sortByRate();
                    moviesSorted.forEach(movieSorted -> System.out.println(movieSorted.getDatasheet()));
                    break;
                case 7:
                    String movieTitleToPlay = ScannerUtils.getText("Write name of the movie you want to play");
                    Movie movieToPlay = platform.searchByTitle(movieTitleToPlay);

                    if(movieToPlay != null){
                        platform.playMovie(movieToPlay);
                        break;
                    }else{
                        System.out.println("❌ Movie not found");
                    }
                case 8:
                    System.out.println("👋🏼 Closing app...");
                    return;
                default:
                    System.out.println("❌ Invalid option!");
            }
        }
    }

    private static void loadSampleMovies(Platform platform) {
        platform.getMovieList().addAll(FileUtils.readData());
    }
}

// Class of objects and classes