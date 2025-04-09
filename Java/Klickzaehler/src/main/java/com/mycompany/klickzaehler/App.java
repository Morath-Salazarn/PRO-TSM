package com.mycompany.klickzaehler;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.control.Button;
import javafx.geometry.Insets;
import javafx.scene.control.TextField;


/**
 * JavaFX App
 */
public class App extends Application {

    @Override
    public void start(Stage stage) {
        BorderPane root = new BorderPane();
        
        
        VBox vboxRechts = new VBox();
        
        Insets pad = new Insets(10, 10, 50, 10);
        vboxRechts.setPadding(pad);
        vboxRechts.setSpacing(5);
                
        TextField zaehler = new TextField();
        
        root.setRight(vboxRechts);
        root.setTop(zaehler);
        
        Button klick = new Button("+");
        Button reset = new Button("reset");
        
        vboxRechts.getChildren().add(klick);
        vboxRechts.getChildren().add(reset);
        
        Scene scene = new Scene(root, 200, 150);
        stage.setTitle("Klickzähler");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

}