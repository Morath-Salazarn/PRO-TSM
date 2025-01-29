/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package blogic;

/**
 *
 * @author maxi-leidl
 */
public class Auto {
    private double tankVolumen;
    private double tankInhalt;
    private double verbrauchProKm;
    
//Konstruktoren    
    // Standardkonstruktor
    
    public Auto(){
        this.tankInhalt = 20;
        this.tankVolumen = 60;
        this.verbrauchProKm = 6.7;
    }

    public Auto(double tankVolumen, double tankInhalt, double verbrauchProKm) {
        this.tankVolumen = tankVolumen;
        this.tankInhalt = tankInhalt;
        this.verbrauchProKm = verbrauchProKm;
    }

    public double getTankVolumen() {
        return tankVolumen;
    }

    public void setTankVolumen(double tankVolumen) {
        this.tankVolumen = tankVolumen;
    }

    public double getTankInhalt() {
        return tankInhalt;
    }

    public void setTankInhalt(double tankInhalt) {
        this.tankInhalt = tankInhalt;
    }

    public double getVerbrauchProKm() {
        return verbrauchProKm;
    }

    public void setVerbrauchProKm(double verbrauchProKm) {
        this.verbrauchProKm = verbrauchProKm;
    }
    
    
    public boolean istErreichbar(double kilometer){
        return kilometer * verbrauchProKm <= tankVolumen;
    }
    
    
    
}
