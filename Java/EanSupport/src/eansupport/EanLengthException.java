/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package eansupport;

/**
 *
 * @author maxi-leidl
 */
public class EanLengthException extends RuntimeException {
    public EanLengthException(){
        super("Die eingegebene Zahl ist zu lang oder zu kurz");
    }
    
}
