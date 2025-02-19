
/**
 * Write a description of class Hund here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Hund extends Haustier
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class Hund
     */
    public Hund(String name)
    {
        super(name);
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void bellen()
    {
        // put your code here
        System.out.println(getName() + " bellt!");
    }
    
    public void verjageKatze()
    {
        System.out.println(getName() + " verjagt eine Katze!");
    }
}
