import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * This class <description of functionality>
 *
 * @author jipderksen
 */
public class Main {

    static int[][] octos = new int[10][10];
    static int shine = 0;

    public static void main(String[] args) {


        // put all octo integers in the octos array
        try {
            File myObj = new File("./text.txt");
            Scanner myReader = new Scanner(myObj);
            int lineNumber = 0;
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine().trim();
                int[] line = new int[10];
                for (int i = 0; i < data.length(); i++) {
                    line[i] = Integer.parseInt(String.valueOf(data.charAt(i)));
                }
                octos[lineNumber] = line;
                lineNumber++;
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < octos.length; j++) {
                for (int k = 0; k < octos[j].length; k++) {
                    increase(j, k, 1);
                }
            }
        }

        for (int[] octo : octos) {
            for (int octi : octo) {
                System.out.println(octi);
            }
        }

        System.out.println(shine);
    }

    static void increase(int x, int y, int num) {
        try {
            octos[x][y]++;
            if (octos[x][y] == 9) {
                shine++;
                octos[x][y] = 0;
                increase(x - 1, y, num);
                increase(x, y - 1, num);
                increase(x, y + 1, num);
                increase(x + 1, y, num);
                increase(x - 1, y - 1, num);
                increase(x - 1, y + 1, num);
                increase(x + 1, y - 1, num);
                increase(x + 1, y + 1, num);
            }
        } catch (Exception ex) {
            System.out.printf("%d, %d\n", x, y);
        }
    }
}
