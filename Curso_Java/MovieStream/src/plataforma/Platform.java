package plataforma;

import content.Movie;

import java.util.ArrayList;
import java.util.List;

public class Platform {
    private String name;
    private List<Movie> movieList;

    public Platform(String name){
        this.name = name;
        this.movieList = new ArrayList<>();
    }

    public void addMovie(Movie element){
        this.movieList.add(element);
    }

    public void getAllTitles(){
        for (Movie movie : movieList) {
            System.out.println(movie.getTitle());
        }
    }

    public void searchByTitle(String title){
        boolean found = false;

        for(Movie movie: movieList) {
            if(movie.getTitle().equalsIgnoreCase(title)){
                System.out.println(movie.getDatasheet());
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("❌ Movie not found");
        }

    }

    public void removeByTitle(String title) {
        for (int i = 0; i < movieList.size(); i++) {
            if (movieList.get(i).getTitle().equalsIgnoreCase(title)) {
                movieList.remove(i);
                System.out.println("💀 Movie removed successfully.");
                return;
            }
        }

        System.out.println("❌ Movie not found.");
    }

    public String getName() {
        return name;
    }

    public List<Movie> getMovieList() {
        return movieList;
    }



}
