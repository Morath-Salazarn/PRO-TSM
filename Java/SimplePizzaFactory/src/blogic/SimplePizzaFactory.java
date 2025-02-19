/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package blogic;

/**
 *
 * @author ml
 */
public class SimplePizzaFactory
{
       public Pizza createPizza(String PizzaType)
      {
            Pizza pizza=null;
            
            if (PizzaType.equalsIgnoreCase("cheese"))
            {
                // pizza=new CheesePizza();
            }
            else if (PizzaType.equalsIgnoreCase("pepperoni"))
            {
                // pizza=new PepperoniPizza();
            }
          
            return pizza;
        }
}
