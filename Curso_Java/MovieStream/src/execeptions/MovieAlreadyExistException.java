package execeptions;

public class MovieAlreadyExistException extends RuntimeException {
    public MovieAlreadyExistException(String title){
        super("Content: " + title + "already exists.");
    }
}
