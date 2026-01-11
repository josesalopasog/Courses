package content;

import java.time.LocalDate;

public class Documentary extends Content implements Promotional{
    private String narrator;

    public Documentary(String title, int duration, Genre genre, LocalDate dateOfPremiere, double score, String Narrator) {
        super(title, duration, genre, dateOfPremiere, score);
        this.narrator = narrator;
    }

    @Override
    public void play() {
        System.out.println("Playing documentary " + getTitle() + " Narrator: " + getNarrator());
    }

    @Override
    public String promo() {
        return "💫 Watch the next documentary " + this.getTitle() + " With the narrator: " + narrator;
    }

    public String getNarrator() {
        return narrator;
    }
}
