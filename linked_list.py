"""
Linked List
1. Don't need to pre-allocate space
2. Insertion is easier
3. Traversal and Accessing Element and insert anywhere other than start = O(n)
3.1 Insert at beginning is O(1)
"""


class Node:
    def __init__(self, data=None, next=None): #add self, value, data=None...
        # self.value = value
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #only use when you add self.value back to Node
    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert(self, data_list):
        # self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print("Linked List is Empty")

        itr = self.head
        llstr = []

        while itr:
            llstr.append(str(itr.data))
            itr = itr.next

        lout = " --> ".join(x for x in llstr)
        print(lout)

    def remove_at(self, index):
        if index<0 or index >= self.get_length():
            raise Exception("Not valid index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index >= self.get_length():
            raise Exception("Not valid index")
        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length()-1:
            self.insert_at_end(data)

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1




if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(75)
    ll.insert([1,2,3,4,5,6])
    ll.print()
    ll.remove_at(3)
    ll.insert_at(6, "fig")
    ll.print()

    # lis = []
    # lis.insert(0, 5)
    # lis.insert(0,10)
    # print(lis)
    # lis.append(6)
    # print(lis)

    # ll = LinkedList()
    # ll.add(Node('hey'))
    # ll.add(Node('there'))
    # ll.add(Node('Brendo'))
    # print([node.value for node in ll])