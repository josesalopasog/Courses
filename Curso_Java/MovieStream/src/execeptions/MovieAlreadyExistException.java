package execeptions;

public class MovieAlreadyExistException extends RuntimeException {
    public MovieAlreadyExistException(String title){
        super("Movie: " + title + "already exists.");
    }
}
