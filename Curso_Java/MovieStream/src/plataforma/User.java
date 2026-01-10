package plataforma;

import content.Content;

public class User {
    private final String name;
    private String email;
    private int age;
    private int userID;

    public User(String name) {
        this.name = name;

    }

    public void watch(Content content){
        System.out.println(name + " is watching...");
        content.play();
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getUserID() {
        return userID;
    }

    public void setUserID(int userID) {
        this.userID = userID;
    }
}
