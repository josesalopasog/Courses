package plataforma;

import content.Movie;

import java.util.ArrayList;
import java.util.List;

public class Platform {
    private String name;
    private List<Movie> content;

    public Platform(String name){
        this.name = name;
        this.content = new ArrayList<>();
    }

    public void addMovie(Movie element){
        this.content.add(element);
    }

    public void getAllTitles(){
        for (Movie movie : content) {
            System.out.println(movie.getTitle());
        }
    }

    public void deleteMovi(Movie element){
        this.content.remove(element);
    }

    public String getName() {
        return name;
    }

    public List<Movie> getContent() {
        return content;
    }
}
