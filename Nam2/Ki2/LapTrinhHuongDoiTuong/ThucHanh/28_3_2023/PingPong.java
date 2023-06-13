class PingPong extends Thread {
    String word;
    int delay;

    PingPong(String word, int delay) {
        this.word = word;
        this.delay = delay;
    }

    public void run() {
        try {
            for (;;) {

                System.out.println(word);
                Thread.sleep(delay);
            }
        } catch (InterruptedException e) {
            return;
        }
    }

    public static void main(String args[]) {
        // new PingPong("ping", 333).start(); // khoi dong tien doan 1
        // new PingPong("Pong", 1000).start();
        Thread thread = new PingPong("ping", 333);
        Thread thread1 = new PingPong("ping", 333);
        thread.start();
        thread1.start();
    }
}