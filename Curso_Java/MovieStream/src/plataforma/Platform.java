package plataforma;

import content.*;
import execeptions.MovieAlreadyExistException;
import utils.FileUtils;

import java.util.*;

public class Platform {
    private String name;
    private List<Content> contentList;
    private Map<Content, Integer> views;

    public Platform(String name){
        this.name = name;
        this.contentList = new ArrayList<>();
        this.views = new HashMap<>();
    }

    public void addMovie(Content element){
        Content contentValidation = this.searchByTitle(element.getTitle());
        if (contentValidation != null){
            throw new MovieAlreadyExistException(element.getTitle());
        }
        FileUtils.writeData(element);
        this.contentList.add(element);
    }

    public void playMovie(Content content){
        int countViews = views.getOrDefault(content, 0);
        System.out.println(content.getTitle() + "have" + countViews + "views");

        this.countViews(content);
        content.play();
    }

    private  void countViews(Content content){
        int countViews = views.getOrDefault(content, 0);
        views.put(content, countViews + 1);
    }

    public List<String> getAllTitles(){
        return contentList.stream()
                .map(Content::getTitle)
                .toList();
    }

    public List<SummaryContent> getSummaries(){
        return contentList.stream()
                .map(movie -> new SummaryContent(movie.getTitle(), movie.getDuration(), movie.getGenre()))
                .toList();
    }

    public Content searchByTitle(String title) {
        for (Content content : contentList) {
            if (content.getTitle().equalsIgnoreCase(title)) {
                return content;
            }
        }
        return null;
    }

    public List<Content> searchByGenre(Genre genre){
        List<Content> contentListFiltered = contentList.stream()
                .filter(movie -> movie.getGenre().equals(genre))
                .toList();
        if (contentListFiltered.isEmpty()) {
            System.out.println("No movies found for genre: " + genre);
        }

        return contentListFiltered;
    }

    public List<Content> sortByRate (){
        return contentList.stream()
                .sorted(Comparator.comparingDouble(Content::getScore).reversed())
                .toList();
    }

    public List<Movie> getMovies(){
        return contentList.stream()
                .filter(content -> content instanceof Movie)
                .map(filteredContent -> (Movie) filteredContent)
                .toList();
    }

    public List<Documentary> getDocumentaries(){
        return contentList.stream()
                .filter(content -> content instanceof Documentary)
                .map(filteredContent -> (Documentary) filteredContent)
                .toList();
    }

    public int getTotalDuration(){
        return contentList.stream()
                .mapToInt(Content::getDuration)
                .sum();
    }

    public void removeByTitle(String title) {
        for (int i = 0; i < contentList.size(); i++) {
            if (contentList.get(i).getTitle().equalsIgnoreCase(title)) {
                contentList.remove(i);
                System.out.println("💀 Content removed successfully.");
                return;
            }
        }

        System.out.println("❌ Content not found.");
    }

    public String getName() {
        return name;
    }

    public List<Content> getMovieList() {
        return contentList;
    }



}
