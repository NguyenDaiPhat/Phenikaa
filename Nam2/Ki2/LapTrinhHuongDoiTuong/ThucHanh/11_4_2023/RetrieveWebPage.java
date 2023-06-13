import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class RetrieveWebPage {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Hay nhap URL cua trang web tu tham so dong lenh.");
            System.exit(1);
        }

        String urlString = args[0]; 

        try {
            URL url = new URL(urlString);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            int responseCode = connection.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                String line;
                StringBuilder html = new StringBuilder();
                while ((line = reader.readLine()) != null) {
                    html.append(line);
                }
                reader.close();
                connection.disconnect();
                System.out.println("Ma HTML cua trang web:");
                System.out.println(html.toString());
            } else {
                System.out.println("Khong the ket noi toi trang web. Ma tra ve: " + responseCode);
            }

        } catch (IOException e) {
            System.out.println("Loi khi ket noi toi trang web: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
