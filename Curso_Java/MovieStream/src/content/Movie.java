package content;

import java.time.LocalDate;

public class Movie extends Content{

    public Movie(String title, int duration, Genre genre, LocalDate dateOfPremiere, double score) {
        super(title, duration, genre, dateOfPremiere, score);
    }

    @Override
    public void play() {
        System.out.println("Playing Movie" + getTitle());
    }
}
