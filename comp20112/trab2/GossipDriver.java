import java.io.*;

public class GossipDriver {
    public static void main(String[] args) throws Exception {
        FileReader input = new FileReader(args[0]);
        GossipParser parser = new GossipParser(args[0], input);
        parser.parse();
        System.out.println(parser.output);
    }
}
