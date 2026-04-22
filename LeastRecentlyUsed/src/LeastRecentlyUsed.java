import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;

public class LeastRecentlyUsed<K, V> {

    private final int capacity;
    private final LinkedHashMap<K, V> cache;

    public LeastRecentlyUsed(int capacity) {
        this.capacity = capacity;
        this.cache = new LinkedHashMap<>(capacity, 0.75f, true){
            @Override
            protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
                return size() > LeastRecentlyUsed.this.capacity;
            }
        };
    }
    public V get(K key) {
        return cache.get(key);
    }
    public void put(K key, V value) {
        cache.put(key, value);
    }
    public void display() {
        var entry = new ArrayList<>(cache.entrySet());
        for (int i = entry.size() - 1; i >= 0; i--) {
            var orderedCache = entry.get(i);
            System.out.print(orderedCache.getKey() + ":" + orderedCache.getValue() + " ");
        }
        System.out.println();
    }
    
}