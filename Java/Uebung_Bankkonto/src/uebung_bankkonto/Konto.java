/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package uebung_bankkonto;

/**
 *
 * @author maxi-leidl
 */
public class Konto {
    
    private String inhaber;
    private String kontonummer;
    private double kontostand;

    
   //Konstruktor
    
    public Konto(String inhaber, String kontonummer) {
        this.inhaber = inhaber;
        if(this.kontonummer.length() > 10 || this.kontonummer.length() < 6){
            this.kontonummer = "**********";
        }
        else{
            this.kontonummer = kontonummer;
        }
        this.kontostand = 0.0;
    }
    
    //getter und setter

    public String getInhaber() {
        return inhaber;
    }

    public String getKontonummer() {
        return kontonummer;
    }

    public double getKontostand() {
        return kontostand;
    }

    public void setKontostand(double kontostand) {
        this.kontostand = kontostand;
    }
    
    
    
    
    public void einzahlen(double betrag){
        if(betrag > 0){
            kontostand += betrag;
        }
    }
    
    public boolean auszahlen(double betrag){
        if(betrag >0){
            if(this.kontostand >= betrag){
                this.kontostand -= betrag;
                return true;
            }
        }
        else{
            return false;
        }
    }
    
}
