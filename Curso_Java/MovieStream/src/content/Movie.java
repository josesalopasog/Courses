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
