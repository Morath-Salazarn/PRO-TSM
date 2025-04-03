/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package eansupport;

/**
 *
 * @author maxi-leidl
 */
public class EanNotNumericException extends RuntimeException {
    public EanNotNumericException(){
        super("Es handelt sich um eine ungültige Zahl");
    }
    
}
