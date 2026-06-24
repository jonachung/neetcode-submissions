# double linked list
# head <-> __least recently used___ <-> (key, value) <-> __most recently used____ <-> tail
# hashmap to store key value pair

class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = defaultdict(Node)
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def add(self, nodeToAdd):
        prevNode = self.tail.prev
        nodeToAdd.prev = prevNode
        nodeToAdd.next = self.tail
        prevNode.next = nodeToAdd
        self.tail.prev = nodeToAdd

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map.get(key)
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map.get(key)
            self.remove(node)

        newNode = Node(key, value)
        self.map[key] = newNode
        self.add(newNode)

        if len(self.map) > self.capacity:
            leastRecentlyUsedNode = self.head.next
            self.remove(leastRecentlyUsedNode)
            key = leastRecentlyUsedNode.key
            del self.map[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
