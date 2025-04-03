package blogic;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.layout.HBox;


/**
 * JavaFX App
 */
public class App extends Application {

    @Override
    public void start(Stage stage) {
        
        // Ebene 1 Root Pain
        BorderPane root = new BorderPane();
        
        // Ebene 2 Container Links und oben
        VBox vboxlinks = new VBox();
        HBox hboxoben = new HBox();
        
        root.setTop(hboxoben);
        root.setLeft(vboxlinks);
        
        //Ebene 2 Label Mitte
        Label labelmitte = new Label("Hier kommt die Ausgabe hin");
        root.setCenter(labelmitte);
        
        
        Scene scene = new Scene(root, 500, 500);
        
        stage.setTitle("Beispiel FX");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

}