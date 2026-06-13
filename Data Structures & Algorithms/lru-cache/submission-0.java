class Node {
    int key;
    int value;
    Node prev;
    Node next;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {

    // use doubly linked list + hashmap approach
    // self.capacity = capacity
    // hashmap => {key: key, value: Node}
    // head <-> least recently <-> most recently <-> tail
    // when get() -> remove key from linked list, add to before the tail (most recently used)
    // when put() -> check if key exists, if so remove key from linked list, add before tail. 
    // if key does not exist, add before tail.
    // check if len(hashmap) > k. If so, remove LRU node from hashmap + remove key/value pair from hashmap

    private int capacity;
    private HashMap<Integer, Node> map;
    private Node head;
    private Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();
        this.head = new Node(0,0);
        this.tail = new Node(0,0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    public void addNode(Node node) {
        // add node before the tail (most recently)
        Node prev = this.tail.prev;
        prev.next = node;
        node.prev = prev;
        node.next = this.tail;
        this.tail.prev = node;
    }

    public void removeNode(Node node) {
        // remove the node, can be used to remove after head or used to move node
        // to most recently used
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
    }
    
    public int get(int key) {
        if (this.map.containsKey(key)) {
            Node node = this.map.get(key);
            removeNode(node);
            addNode(node);
            return node.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (this.map.containsKey(key)) {
            Node node = this.map.get(key);
            removeNode(node);
            this.map.remove(key);
        }
        Node newNode = new Node(key, value);
        addNode(newNode);
        this.map.put(key, newNode);

        if (map.size() > this.capacity) {
            Node nodeToRemove = this.head.next;
            removeNode(nodeToRemove);
            this.map.remove(nodeToRemove.key);
        }
    }
}
