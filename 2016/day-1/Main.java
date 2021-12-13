import java.util.Scanner;
import java.io.File;
import java.lang.Exception;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        for (String text : readFile("./text.txt")) {
            System.out.println(text);
        }
    }

    public static List<String> readFile(String path) {
        try {
            File myObj = new File(path);
            Scanner myReader = new Scanner(myObj);
            List<String> fileArray = new ArrayList<>();
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] data2 = data.split(", ");
                fileArray.addAll(List.of(data2));
            }
            myReader.close();
            return fileArray;
        } catch (Exception e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return null;
    }
}
