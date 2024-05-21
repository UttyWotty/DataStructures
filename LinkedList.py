class Node:
    """
    And object for storing a single node of a linked list
    Models two attributes - data and the link to the next node in the list
    """
    data = None # empty
    next_node = None #also empty

    def __init__(self,data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" %self.data

class LinkedList:
    """
     Singly linkedlist
     """

    def __init__(self):  # we have created an empty  linkedlist. head= None
        self.head = None

    def is_empty(self):
        return self.head == None  # this is to check if the list os empty

    def size(self):  #listenin eleman sayisini ariyoruz
        """
        returns the number of nodes in the list
        Takes O ( n) time
        """
        current = self.head   #head 0dan basladi
        count = 0

        while current:   # her seferinde 1 ekleyerek sayiyoruz
            count += 1
            current = current.next_node   #bir sonraki node a git

        return count   # count olarak sonucu dondur
    def add(self,data):
        """
        Adds a new node containing data at the head of the list
        takes constant time it is the best case scenario

        """
        new_node = Node(data)   # yeni bir node olusturuyoruz
        new_node.next_node = self.head  # adding to the head of the list
        self.head = new_node   # yeni head bu olacak

    def search(self, key):   # adding a search method
        """
        search for the first node containing data that matches the key
        returns the node or None if not found

        Takes O(n) or Linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
               current = current.next_node
        return None

    def insert(self,data, index):
        """
        Inserts a new node that containing data at index position
        Insertion takes O(1) time but findign the node at the insertion point takes linear time O(n)
        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes note containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) linear time
        """
        current = self.head   #if head is selected, there is no previous one
        previous = None
        found = False   # we will keep running to loop as long as found return False

        while current and not found:   #as long as the found is False
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index ==0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
            return current
    def __repr__(self):
        """
        return a string representation of the list
        takes O(n) time
        :return:
        """
        nodes = []
        current = self.head

        while current:   # if the node assigned to the head
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            #value will be added to the head and will say "this is the head"
            elif current.next_node is None: #if it is assigned to a None, means it is the Tail
                nodes.append("[Tail: %s]" % current.data)  # value will say this is the tail
            else:
                nodes.append("[%s]" % current.data)  #not head ot tail

            current = current.next_node  # every iteration, it will move to the next value
        return "->" .join(nodes)  # at the end, all values will join to the nodes named     linked list


l = LinkedList()
l.add(10)

l.add(20)
l.add(45)
l.add(80)
n = l.search(45)
n2 = l.remove(10)
n3 = l.insert(15,1)


#print(n)  #shows the searched Node = 45
print(l)  # show the list again

#print(l)  # this shows [Head -> 3] , [2] [Tail ->1]




