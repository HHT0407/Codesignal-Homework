#參考https://github.com/LPT0423/LPT/blob/master/HW4/hash_table_06170212.py
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self,capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

        self.head = None

    def add(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        hash = int(h.hexdigest(), 16) 
        index = hash % self.capacity
        if not self.contains(key):
            node = ListNode(key)
            node.next = self.head
            self.head = node

    def remove(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        hash = int(h.hexdigest(), 16) 
        index = hash % self.capacity
        node = self.head

        # if head is our target
        if node and node.val == key:
            self.head = node.next
            return None

        while node and node.next:
            if node.next.val == key:
                node.next = node.next.next
                break

    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        hash = int(h.hexdigest(), 16) 
        index = hash % self.capacity
        node = self.head
        while node:
            if node.val == key:
                return True
            node = node.next
        return False
