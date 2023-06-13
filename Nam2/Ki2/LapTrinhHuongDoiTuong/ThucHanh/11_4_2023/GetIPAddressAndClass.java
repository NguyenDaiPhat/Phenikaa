import java.net.InetAddress;

public class GetIPAddressAndClass {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Vui long nhap host name tu tham so dong lenh.");
            System.exit(1);
        }

        String hostName = args[0];

        try {
            InetAddress inetAddress = InetAddress.getByName(hostName);
            String ipAddress = inetAddress.getHostAddress();
            String ipClass = getIPClass(ipAddress);
            System.out.println("dia chi IP cua host name " + hostName + " la: " + ipAddress);
            System.out.println("Lop dia chi cua dia chi IP " + ipAddress + " la: " + ipClass);
        } catch (Exception e) {
            System.out.println("Khong the lay dia chi IP cua host name " + hostName);
        }
    }

    public static String getIPClass(String ipAddress) {
        String[] ipParts = ipAddress.split("\\.");
        int firstOctet = Integer.parseInt(ipParts[0]);
        if (firstOctet >= 1 && firstOctet <= 126) {
            return "A";
        } else if (firstOctet >= 128 && firstOctet <= 191) {
            return "B";
        } else if (firstOctet >= 192 && firstOctet <= 223) {
            return "C";
        } else if (firstOctet >= 224 && firstOctet <= 239) {
            return "D";
        } else if (firstOctet >= 240 && firstOctet <= 255) {
            return "E";
        } else {
            return "Khong xac dinh";
        }
    }
}
