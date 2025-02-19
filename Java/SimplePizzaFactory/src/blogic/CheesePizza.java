/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package blogic;

/**
 *
 * @author maxi-leidl
 */
public class CheesePizza extends Pizza {

    public CheesePizza() {
        name = "Kaesepizza";
        dough = "duenner knuspriger Teig";
        sauce = "Tomatensauce";
        toppings.add("geriebener Mozzarella");
        
    }
    
    
    
    public void bake(){
        System.out.println("Backzeit: 9 Minuten bei 220 Grad.");
    }
    public void box(){
        
    }
    public void cut(){
        
    }
}
