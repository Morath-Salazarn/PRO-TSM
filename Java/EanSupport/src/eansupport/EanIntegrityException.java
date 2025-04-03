/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package eansupport;

/**
 *
 * @author maxi-leidl
 */
public class EanIntegrityException extends RuntimeException {
    public EanIntegrityException(){
        super("Die Integrität der Nummer ist verletzt");
    }
    
}
