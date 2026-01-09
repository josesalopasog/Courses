package plataforma;

import content.Movie;
import content.Genre;
import content.SummaryContent;
import execeptions.MovieAlreadyExistException;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Platform {
    private String name;
    private List<Movie> movieList;

    public Platform(String name){
        this.name = name;
        this.movieList = new ArrayList<>();
    }

    public void addMovie(Movie element){
        Movie movieValidation = this.searchByTitle(element.getTitle());
        if (movieValidation != null){
            throw new MovieAlreadyExistException(element.getTitle());
        }
        this.movieList.add(element);
    }

    public List<String> getAllTitles(){
        return movieList.stream()
                .map(Movie::getTitle)
                .toList();
    }

    public List<SummaryContent> getSummaries(){
        return movieList.stream()
                .map(movie -> new SummaryContent(movie.getTitle(), movie.getDuration(), movie.getGenre()))
                .toList();
    }

    public Movie searchByTitle(String title) {
        for (Movie movie : movieList) {
            if (movie.getTitle().equalsIgnoreCase(title)) {
                return movie;
            }
        }
        return null;
    }

    public List<Movie> searchByGenre(Genre genre){
        List<Movie> movieListFiltered = movieList.stream()
                .filter(movie -> movie.getGenre().equals(genre))
                .toList();
        if (movieListFiltered.isEmpty()) {
            System.out.println("No movies found for genre: " + genre);
        }

        return movieListFiltered;
    }

    public List<Movie> sortByRate (){
        return movieList.stream()
                .sorted(Comparator.comparingDouble(Movie::getScore).reversed())
                .toList();
    }

    public int getTotalDuration(){
        return movieList.stream()
                .mapToInt(Movie::getDuration)
                .sum();
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
