class ListNode:
    def __init__(self,key = -1,val = -1,next = None):
        self.key = key
        self.val = val
        self.next = next
class MyHashMap:

    def __init__(self):
        self.maps = [ListNode() for _ in range(1000)]
    def hash(self,key):
        return key % len(self.maps)
    def put(self, key: int, value: int) -> None:
        curr = self.maps[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key,value) #key is address of node and value is which store the value on that address
    def get(self, key: int) -> int:
        curr = self.maps[self.hash(key)].next #to skip dummy node we kept .next at curr
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.maps[self.hash(key)]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next #we delete the node when key is equal
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)