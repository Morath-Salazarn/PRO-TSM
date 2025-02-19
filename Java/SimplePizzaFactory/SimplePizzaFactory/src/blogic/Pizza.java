/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package blogic;

import java.util.ArrayList;

/**
 *
 * @author ml
 */
public abstract class Pizza
{
    private String name;
    private String dough;
    private String sauce;
    private ArrayList<String> toppings = new ArrayList<String>();
    
     
     public void prepare()
     {
         System.out.println("Zubereitung einer " + name );
         System.out.println("Verwendete Teigmischung: " + dough );         
         System.out.println("Als Sauce wird " + sauce + " hinzugefügt.");         
         System.out.println("Die Pizza wird mit folgenden Zutaten belegt:");
         for (int i=0; i< toppings.size(); i++)
         {
               System.out.println("   > " + toppings.get(i) );
         }
     }
     
     public abstract void bake();
     public abstract void box();
     public abstract void cut();
     
     public void startProduction()
     {
            prepare();
            bake();
            cut();
            box();
            System.out.println("==> Fertig! Die Pizza kann ausgeliefert werden....");
            System.out.println();
     }
    
    //getter / setter
    public String getName()
    {
        return this.name;
    }
    public void setName(String Name)
    {
        this.name=Name;
    }
    public String getDough()
    {
        return this.dough;
    }
    public void setDough(String Dough)
    {
        this.dough=Dough;
    }
    public String getSauce()
    {
        return this.sauce;
    }
    public void setSauce(String Sauce)
    {
        this.sauce=Sauce;
    }
    public void addTopping(String Topping)
    {
        toppings.add(Topping);
    }
    
}

