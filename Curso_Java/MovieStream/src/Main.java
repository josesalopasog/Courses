import content.Movie;
import plataforma.User;

import java.time.LocalDate;
import java.time.temporal.IsoFields;
import java.util.SortedSet;

public class Main {
    public static void main(String[] args){
        Movie movie = new Movie();
        movie.title = "Lord of rings";
        movie.dateOfPremiere = LocalDate.of(2018,10,15);
        movie.genre = "Fantasy";
        movie.rate(4.7);
        movie.duration = 120;

        long durationLong = movie.duration;
        int rate = (int) movie.score;
        int numberOfAwards = (int) Long.parseLong("25");

        System.out.println("Movie duration: " + durationLong);
        System.out.println("Rate in Int: " + rate);
        System.out.println("Normal rate: " + movie.score);
        System.out.println("");

        User user = new User();
        user.name = "Jose";

        user.watch(movie);

        System.out.println(movie.getDatasheet());


    }
}

// Class of objects and classes