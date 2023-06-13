import java.net.MalformedURLException;
import java.net.URL;

public class ParseURL {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Vui long nhap URL tu tham so dong lenh.");
            System.exit(1);
        }

        String urlString = args[0]; 

        try {
            URL url = new URL(urlString);

            
            String protocol = url.getProtocol();
            String domain = url.getHost();
            String path = url.getPath();
            String query = url.getQuery();
            String fragment = url.getRef();

            
            System.out.println("Giao thuc: " + protocol);
            System.out.println("Ten mien: " + domain);
            System.out.println("Duong dan: " + path);
            System.out.println("Tham so truy van: " + query);
            System.out.println("Fragment: " + fragment);

        } catch (MalformedURLException e) {
            System.out.println("URL khong dung.");
            e.printStackTrace();
        }
    }
}
