
/**
 * Write a description of class Katze here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Katze extends Haustier
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class Katze
     */
    public Katze(String name)
    {
        super(name);
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void miau()
    {
        // put your code here
        System.out.println(getName() + " miaut");
    }
}
