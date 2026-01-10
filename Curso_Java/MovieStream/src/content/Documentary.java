package content;

import java.time.LocalDate;

public class Documentary extends Content{
    private String narrator;

    public Documentary(String title, int duration, Genre genre, LocalDate dateOfPremiere, double score, String Narrator) {
        super(title, duration, genre, dateOfPremiere, score);
        this.narrator = narrator;
    }

    public String getNarrator() {
        return narrator;
    }
}
