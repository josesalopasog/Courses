import content.Movie;

public class MainStackHeap {
    public static void main(String[] args){
        Movie movieOne = new Movie("Lion King", 135, "Animated");
        Movie movieTwo = new Movie("Harry Potter", 200, "Fantasy");

        movieOne = movieTwo;
        movieOne.title = "The hobbit";

        System.out.println(movieOne.title);
        System.out.println(movieTwo.title);
    }
}

