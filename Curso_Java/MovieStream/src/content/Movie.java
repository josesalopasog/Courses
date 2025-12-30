package content;

import java.time.LocalDate;

public class Movie {
    public String title;
    public String description;
    public int duration;
    public String genre;
    public LocalDate dateOfPremiere;
    public double score;
    public boolean status;
    public LocalDate registrationDate;

    public Movie(String title, int duration, String genre){
        this.title = title;
        this.duration = duration;
        this.genre = genre;
        this.registrationDate = LocalDate.now();
        this.status = true;
    }

    public Movie(String title, int duration, String genre, double score) {
        this(title, duration, genre);
        this.rate(score);
    }

    public void play() {
        System.out.println("Playing " + title);
    }

    public String getDatasheet(){
        return title + "(" + dateOfPremiere.getYear() + ")\n"
                + "Genre:" + genre + "\n"
                + "Score:" + score + "\n";
    }

    public void rate(double score){
        if (score >= 0 && score <= 5) {
            this.score = score;
        }

    }

    public boolean isPopular(){
        return score >=4;
    }
}
