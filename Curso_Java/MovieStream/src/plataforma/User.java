package plataforma;

import content.Movie;

public class User {
    public String name;
    public String email;

    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public void watch(Movie movie){
        System.out.println(name + " is watching...");
        movie.play();
    }
}
