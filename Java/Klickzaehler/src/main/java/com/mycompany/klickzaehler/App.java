package com.mycompany.klickzaehler;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.control.Button;



/**
 * JavaFX App
 */
public class App extends Application {

    @Override
    public void start(Stage stage) {
        BorderPane root = new BorderPane();
        
        VBox vboxRechts = new VBox();
        
        root.setRight(vboxRechts);
        
        Button klick = new Button("+");
        Button reset = new Button("reset");
        
        vboxRechts.getChildren().add(klick);
        vboxRechts.getChildren().add(reset);
        
        Scene scene = new Scene(root, 640, 480);
        stage.setTitle("Klickzähler");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

}