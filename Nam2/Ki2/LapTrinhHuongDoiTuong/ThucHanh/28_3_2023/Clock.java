import java.util.Date;

public class Clock implements Runnable {
    public void run() {
        try {
            for (;;) {
                Date now = new Date();
                System.out.println(now);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            return;
        }
    }
    public static void main(String[] args) {
        Thread clock = new Thread(new Clock());
        clock.start();
    }
}
