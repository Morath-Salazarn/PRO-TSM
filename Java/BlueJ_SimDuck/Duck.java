/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
 

/**
 *
 * @author ml
 */
public class Duck
{
    // Instanzvariablen 
    private QuackBehaviour qb;

    /**
     * Konstruktor für Objekte der Klasse Duck
     */
    public Duck()
    {
        // Instanzvariable initialisieren
       this.qb = null;
    }
    
    //öffentliche Methode beginnen hier
    public void swim(){
        System.out.println("Ich schwimme wie alle Enten, da gibt es nichts Spezielles");
    }
    
    public void display(){
        System.out.println("Ich sehe aus, wie eine 0815 - Ente");
    }
    
    public void performQuack(){
        // Hier wird die Methode quack der Schnittstelle aufgerufen
        this.qb.quack();
    }    
    
    //getter- und setter-Methoden beginnen hier
    public void setQuackBehaviour(QuackBehaviour qb){
        // Hier wird ein neues Objekt vom Typ QuackBehaviour übergeben
        // also: entweder Quack, Squeak oder MuteQuack
       this.qb = qb;
    } 
   
}
