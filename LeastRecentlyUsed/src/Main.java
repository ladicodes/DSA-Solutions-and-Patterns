import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LeastRecentlyUsed<Integer, String> recentlyUsed = new LeastRecentlyUsed<>(3);

        System.out.println("Enter a key");
        int key = sc.nextInt();
        System.out.println("Enter a value");
        String value = sc.next();
        recentlyUsed.put(key, value);
        recentlyUsed.display();

        System.out.println("Enter a key");
        int key1 = sc.nextInt();
        System.out.println("Enter a value");
        String value1 = sc.next();
        recentlyUsed.put(key1, value1);
        recentlyUsed.display();

        System.out.println("Enter a key");
        int key2 = sc.nextInt();
        System.out.println("Enter a value");
        String value2 = sc.next();
        recentlyUsed.put(key2, value2);
        recentlyUsed.display();

        System.out.println("Enter a key to fetch");
        int key3 = sc.nextInt();
        recentlyUsed.get(key3);
        recentlyUsed.display();

        System.out.println("Enter a key");
        int key4 = sc.nextInt();
        System.out.println("Enter a value");
        String value4 = sc.next();
        recentlyUsed.put(key4, value4);
        recentlyUsed.display();

    }
}