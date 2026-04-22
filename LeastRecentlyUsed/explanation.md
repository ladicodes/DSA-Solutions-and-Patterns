What this thing is

LeastRecentlyUsed<K, V> is a cache with a fixed size.
When it gets full and you add something new, it quietly removes the least recently used item.


The trick doing all the work

This line is where everything happens:

new LinkedHashMap<>(capacity, 0.75f, true)

There are three important parts here:

- capacity → initial size of the map
- 0.75f → load factor
- true → enables access order

About the 0.75f (load factor):

- It controls how full the map gets before it resizes internally
- 0.75 means the map resizes when it reaches 75% of its capacity
- It’s a balance between memory usage and performance
- It does NOT control eviction in this cache, just internal resizing

That last true is the real star. It means:

- The map keeps entries ordered by access order, not insertion order
- Every time you call get() or put(), that key becomes the most recently used

So the map is automatically tracking usage for you.


Auto-removal logic

This method controls when items are removed:

protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
return size() > LeastRecentlyUsed.this.capacity;
}

What it means:

- If the cache size exceeds the limit → remove the oldest entry
- Since we’re using access order, “oldest” = least recently used

Removal happens automatically during put().


Methods breakdown

get(K key)

return cache.get(key);

- Fetches the value
- Updates its position to most recently used
- Returns null if the key doesn’t exist


put(K key, V value)

cache.put(key, value);

- Inserts or updates a value
- If capacity is exceeded, the least recently used item is removed automatically


display()

var entry = new ArrayList<>(cache.entrySet());
for (int i = entry.size() - 1; i >= 0; i--) {

- Copies entries into a list
- Iterates in reverse order

Why reverse?

LinkedHashMap stores:
- Least recently used → at the beginning
- Most recently used → at the end

Reversing lets you print:
Most recent → Least recent


Time and Space Complexity

- get(key): O(1)
  HashMap lookup + constant-time reordering

- put(key, value): O(1)
  Insert/update + possible eviction (still constant time)

- display(): O(n)
  Iterates through all elements

- Space Complexity: O(n)
  Stores up to ‘capacity’ number of elements


Example

Capacity = 3

put(1, A)
put(2, B)
put(3, C)

Cache:
1, 2, 3  (1 is least recently used)

get(1)

Cache becomes:
2, 3, 1  (1 is now most recently used)

put(4, D)

Capacity exceeded → remove 2

Final cache:
3, 1, 4