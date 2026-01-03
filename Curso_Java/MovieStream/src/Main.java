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

        String movieTitle = ScannerUtils.getText("Write name of the movie: ");
        String movieGenre = ScannerUtils.getText("Write movie genre: ");
        int movieDuration = ScannerUtils.getNumber("Write movie duration: ");
        double movieRate = ScannerUtils.getDouble("Write movie rate: ");
        LocalDate movieDateOfPremiere = ScannerUtils.getDate("Write Date of premiere of the movie (yyyy-MM-dd): ");

        Movie movie = new Movie(movieTitle, movieDuration,movieGenre, movieDateOfPremiere, movieRate);
        Movie movieTwo = new Movie("Lion King", 200, "kids", LocalDate.of(1998,5,21), 4.5 );


//        movie.dateOfPremiere = LocalDate.of(2018,10,15);
//        Movie movie = new Movie();
//        movie.title = "Lord of rings";
//        movie.dateOfPremiere = LocalDate.of(2018,10,15);
//        movie.genre = "Fantasy";
//        movie.rate(4.7);
//        movie.duration = 120;

//        long durationLong = movie.duration;
//        int rate = (int) movie.score;
//        int numberOfAwards = (int) Long.parseLong("25");

//        System.out.println("Movie duration: " + durationLong);
//        System.out.println("Rate in Int: " + rate);
//        System.out.println("Normal rate: " + movie.score);
//        System.out.println("Number of awards: " + numberOfAwards );

        platform.addMovie(movie);
        platform.addMovie(movieTwo);
        System.out.println("Number of movies: " + platform.getContent().size());

        platform.getAllTitles();

        User user = new User("Jose");
        user.watch(movie);

        System.out.println(movie.getDatasheet());

    }
}

// Class of objects and classes