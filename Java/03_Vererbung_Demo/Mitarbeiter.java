
/**
 * Write a description of class Mitarbeiter here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Mitarbeiter
{
    // instance variables - replace the example below with your own
    private String name;
    private int personalnr;

    /**
     * Constructor for objects of class Mitarbeiter
     */
    public Mitarbeiter()
    {
        name = "Leidl";
        personalnr = 4;
    }
    
    public String getName(){
        return this.name;
    }
    
    public int getPersonalnr (){
        return this.personalnr;
    }
}
