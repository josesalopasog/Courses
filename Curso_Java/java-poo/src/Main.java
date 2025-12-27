import content.Movie;

public class Main {
    public static void main(String[] args){
        Movie movie = new Movie();
        movie.title = "Lord of rings";
        movie.dateOfPremiere = 2001;
        movie.genre = "Fantasy";
        movie.rate(4.7);

        System.out.println(movie.getDatasheet());
    }
}
