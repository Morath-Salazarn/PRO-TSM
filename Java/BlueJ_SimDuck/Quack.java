/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
 

/**
 *
 * @author ml
 */
public class Quack implements QuackBehaviour
{
    public void quack(){
        for (int i=0; i<=3;i++)
        {
           System.out.println("quack...");
        }
    }

}
