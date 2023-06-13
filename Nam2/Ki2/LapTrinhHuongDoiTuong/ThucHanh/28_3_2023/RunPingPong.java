class RunPingPong implements Runnable { // cho phep thua ke mot lop khac , cach cai dat so 1 khong ho phep thua ke lop
                                        // khac
    String word;
    int delay;

    RunPingPong(String word, int delay) {
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
        Runnable ping = new RunPingPong("ping", 66);
        Runnable pong = new RunPingPong("PONG", 500);
        new Thread(ping).start();
        new Thread(pong).start();
    }
}