import content.*;
import execeptions.MovieAlreadyExistException;
import plataforma.Platform;
import utils.FileUtils;
import utils.ScannerUtils;

import java.io.IOException;
import java.time.LocalDate;
import java.util.List;

public class Main {
    public static final String APP_NAME = "MOVIE STREAM APP 🎬";
    public static final String VERSION = "1.0.0";

    public static void main(String[] args){
        Platform platform = new Platform(APP_NAME);
        System.out.println(APP_NAME + " v" + VERSION);

        loadSampleMovies(platform);

        System.out.println("Content in this app: " + platform.getTotalDuration() + "min to watch! \n");

        while(true){
            int menuOption = ScannerUtils.getNumber("""
                    Menu:
                    1. Add a content
                    2. Show all
                    3. Search by title
                    4. Remove content
                    5. Search by genre
                    6. View Populars
                    7. Play Move
                    8. Exit
                    Write the number of your option >""");
            switch (menuOption){
                case 1:
                    int contentOption = ScannerUtils.getNumber("Write the type of content that you want to add: \n 1.Movie \n 2.Documentary");

                    try{
                        switch (contentOption){
                            case 1:
                                String movieTitle = ScannerUtils.getText("Write name of the content: ");
                                Genre movieGenre = ScannerUtils.getGenre("Write content genre: ");
                                int movieDuration = ScannerUtils.getNumber("Write content duration: ");
                                LocalDate movieDateOfPremiere = ScannerUtils.getDate("Write Date of premiere of the content (yyyy-MM-dd): ");
                                double movieRate = ScannerUtils.getDouble("Write content rate: ");

                                Movie movie = new Movie(movieTitle, movieDuration,movieGenre, movieDateOfPremiere, movieRate);

                                platform.addMovie(movie);
                                System.out.println("✅ Content added!");
                                break;
                            case 2:
                                String documentaryTitle = ScannerUtils.getText("Write name of the content: ");
                                Genre documentaryGenre = ScannerUtils.getGenre("Write content genre: ");
                                int documentaryDuration = ScannerUtils.getNumber("Write content duration: ");
                                double documentaryRate = ScannerUtils.getDouble("Write content rate: ");
                                LocalDate documentaryDateOfPremiere = ScannerUtils.getDate("Write Date of premiere of the content (yyyy-MM-dd): ");
                                String documentaryNarrator = ScannerUtils.getText("Write the narrator of the documentary:");
                                Documentary documentary = new Documentary(documentaryTitle,documentaryDuration, documentaryGenre, documentaryDateOfPremiere, documentaryRate, documentaryNarrator);

                                platform.addMovie(documentary);
                                System.out.println("✅ Content added!");
                            default:
                                System.out.println("❌ Invalid option!");
                        }


                    }catch (MovieAlreadyExistException e) {
                        System.out.println("Couldn't add the movie: " + e.getMessage());
                    }

                case 2:
                    List<SummaryContent> moviesSummary = platform.getSummaries();
                    moviesSummary.forEach(summary -> System.out.println(summary.toString()));
                    break;
                case 3:
                    String title = ScannerUtils.getText("Write title to search ");
                    platform.searchByTitle(title);
                    break;
                case 4:
                    String removeTitle = ScannerUtils.getText("Write title to remove ");
                    platform.removeByTitle(removeTitle);
                    break;
                case 5:
                    Genre genreToSearch = ScannerUtils.getGenre("Write the genre of the movies ");
                    List<Content> listOfMoviesByGenre = platform.searchByGenre(genreToSearch);

                    if(listOfMoviesByGenre.isEmpty()){
                        System.out.println("No movies found by genre " + genreToSearch);
                    }else{
                        listOfMoviesByGenre.forEach(movieByGenre -> System.out.println(movieByGenre.getDatasheet()));
                    }
                    break;
                case 6:
                    List<Content> moviesSorted = platform.sortByRate();
                    moviesSorted.forEach(movieSorted -> System.out.println(movieSorted.getDatasheet()));
                    break;
                case 7:
                    String movieTitleToPlay = ScannerUtils.getText("Write name of the content you want to play");
                    Content contentToPlay = platform.searchByTitle(movieTitleToPlay);

                    if(contentToPlay != null){
                        platform.playMovie(contentToPlay);
                        break;
                    }else{
                        System.out.println("❌ Content not found");
                    }
                case 8:
                    System.out.println("👋🏼 Closing app...");
                    return;
                default:
                    System.out.println("❌ Invalid option!");
            }
        }
    }

    private static void loadSampleMovies(Platform platform) {
        platform.getMovieList().addAll(FileUtils.readData());
    }
}

// Class of objects and classes