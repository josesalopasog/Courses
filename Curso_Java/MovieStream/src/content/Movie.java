package content;

import java.time.LocalDate;

public class Movie {
    private String title;
    private String description;
    private int duration;
    private Genre genre;
    private LocalDate dateOfPremiere;
    private double score;
    private boolean status;
    private LocalDate registrationDate;

    public Movie(String title, int duration, Genre genre, LocalDate dateOfPremiere){
        this.title = title;
        this.duration = duration;
        this.genre = genre;
        this.dateOfPremiere = dateOfPremiere;
        this.registrationDate = LocalDate.now();
        this.status = true;
    }

    public Movie(String title, int duration, Genre genre, LocalDate dateOfPremiere, double score) {
        this(title, duration, genre, dateOfPremiere);
        this.rate(score);
    }

    public void play() {
        System.out.println("Playing " + title);
    }

    public String getDatasheet(){
        return "-----------Movie Datasheet--------------\n"+
                title + "(" + dateOfPremiere.getYear() + ")\n"
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

    //Getters Methods

    public String getTitle() {
        return title;
    }

    public String getDescription(){
        return  description;
    }

    public int getDuration() {
        return duration;
    }

    public Genre getGenre() {
        return genre;
    }

    public LocalDate getDateOfPremiere() {
        return dateOfPremiere;
    }

    public double getScore() {
        return score;
    }

    public boolean isStatus() {
        return status;
    }

    public LocalDate getRegistrationDate() {
        return registrationDate;
    }
    //Setters Methods

    public void setDescription(String description) {
        this.description = description;
    }

    public void setDateOfPremiere(LocalDate dateOfPremiere) {
        this.dateOfPremiere = dateOfPremiere;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public void setRegistrationDate(LocalDate registrationDate) {
        this.registrationDate = registrationDate;
    }


//    public void setTitle(String title) {
//        this.title = title;
//    }


}
