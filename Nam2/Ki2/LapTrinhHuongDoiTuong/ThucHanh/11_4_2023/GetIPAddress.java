import java.net.InetAddress;

public class GetIPAddress {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Hay nhap host name tu tham so dong lenh.");
            System.exit(1);
        }

        String hostName = args[0];

        try {
            InetAddress inetAddress = InetAddress.getByName(hostName);
            String ipAddress = inetAddress.getHostAddress();
            System.out.println("dia chi IP cua host name " + hostName + " la: " + ipAddress);
        } catch (Exception e) {
            System.out.println("Khong the lay dia chi IP cua host name " + hostName);
        }
    }
}
