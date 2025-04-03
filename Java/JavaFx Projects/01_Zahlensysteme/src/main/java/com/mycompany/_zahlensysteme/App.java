package com.mycompany._zahlensysteme;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.layout.HBox;
import javafx.scene.control.TextField;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.geometry.Insets;

/**
 * JavaFX App
 */
public class App extends Application {

    @Override
    public void start(Stage stage) {
        
        //Ebene 1 BorderPane root
        BorderPane root = new BorderPane();
        
        //Ebene 2 Container links, oben, mitte, unten
        VBox vboxLinks = new VBox();
        VBox vboxMitte = new VBox();
        
        root.setLeft(vboxLinks);
        root.setCenter(vboxMitte);
        
        HBox hboxOben = new HBox();
        HBox hboxUnten = new HBox();
        
        root.setTop(hboxOben);
        root.setBottom(hboxUnten);
        
      
        
      
        //Ebene 3 Radio Button in HBox Oben
        
        ToggleGroup tog = new ToggleGroup();
        
        RadioButton radioDec = new RadioButton("Dec");
        radioDec.setToggleGroup(tog);
        
        RadioButton radioHex = new RadioButton("Hex");
        radioHex.setToggleGroup(tog);
        
        RadioButton radioOct = new RadioButton("Oct");
        radioOct.setToggleGroup(tog);
        
        RadioButton radioBin = new RadioButton("Bin");
        radioBin.setToggleGroup(tog);
        
        hboxOben.getChildren().add(radioDec);
        hboxOben.getChildren().add(radioHex);
        hboxOben.getChildren().add(radioOct);
        hboxOben.getChildren().add(radioBin);
        
        //Ebene 3 TextField in VBox Center mit Gridpane
        
        
        GridPane gridpane = new GridPane();
        
        root.setCenter(gridpane);
        
        gridpane.setVgap(10);
        gridpane.setHgap(10);
            
        Label dec = new Label("Dec:");
        Label hex = new Label("Hex:");
        Label oct = new Label("Oct:");
        Label bin = new Label("Bin:");
        
        TextField decNr = new TextField();
        TextField hexNr = new TextField();
        TextField octNr = new TextField();
        TextField binNr = new TextField();
        
        gridpane.add(dec, 1, 1);
        gridpane.add(hex, 1, 2);
        gridpane.add(oct, 1, 3);
        gridpane.add(bin, 1, 4);
        gridpane.add(decNr, 2, 1);
        gridpane.add(hexNr, 2, 2);
        gridpane.add(octNr, 2, 3);
        gridpane.add(binNr, 2, 4);
        
        
        
        //Ebene 3 Buttons unten
        Button btn1 = new Button("Rechnen");
        Button btn2 = new Button("Alles Löschen");
        
        hboxUnten.getChildren().add(btn1);
        hboxUnten.getChildren().add(btn2);
        
        
        
        Insets pad = new Insets(5,10,30,20);
        
        hboxUnten.setPadding(pad);
        
        
        
      
        Scene scene = new Scene(root, 500, 300);
        
        stage.setTitle("HexBinOct");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

}