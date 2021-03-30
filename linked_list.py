class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def preppend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            """
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            """

    def print_values(self):

        if (self.head == None):
            print("nothing to be printed!")
        else:
            current_node = self.head
            print("the list has ", self.length, " elements")
            index_of_node = 0
            while (current_node != None):
                print("node at index", index_of_node, "has value ", current_node.data)
                current_node = current_node.next
                index_of_node += 1

    def insert(self, index, data):
        #looping through the linked-list, to find
        #element at index-i, position, so we get the
        #values of node_before_insertion
        #keep node_before_insertion.next for further update of new_node.next
        #update the node_before_insertion.next = new_node
        if self.length == 0:
            if index == 0:
                new_node = Node(data)
                self.head = new_node
                self.length = 1
            else:
                print("Index is not applicable, it is an empty linked list!")
        if self.length <= index:
            print("The index is out of the range of list")
        else:
            node_before_insertion = self.head
            node_after_insertion = node_before_insertion.next
            index_of_node_before_insertion = 0
            while (index_of_node_before_insertion < index - 1):
                node_before_insertion = node_after_insertion
                node_after_insertion = node_before_insertion.next
                index_of_node_before_insertion += 1
            new_node = Node(data)
            node_before_insertion.next = new_node
            new_node.next = node_after_insertion
            self.length += 1
            print("insertion completed", "length: ", self.length)

    def remove(self, index):
        if self.length == 0:
            print("nothing to remove the linked-list is empty!")
        elif self.length < index:
            print("the index is not in the list, as it is shorter!")
        elif self.length == 1:
            #node_before_removal = None
            print("deleting the first and only node", self.head.data)
            self.head = None
            self.tail = self.head
            self.length = 0
        elif index == 0:
            new_head = self.head.next
            self.head = new_head
            if new_head.next != None:
                print("I have removed the first item, new head is ", new_head.data)
            self.length = self.length - 1
        else:
            print("removing element from index: ", index)
            #we covert removal first element (index = 0), so we can now on other indexes > 0
            node_before_removal = self.head
            node_to_be_removed = node_before_removal.next
            next_node_after_removed_one = node_to_be_removed.next
            index_of_node_to_be_removed = 1
            while (index_of_node_to_be_removed < index):
                node_before_removal = node_to_be_removed
                node_to_be_removed = node_before_removal.next
                print("node to be removed", node_to_be_removed.data)
                next_node_after_removed_one = node_to_be_removed.next
                if next_node_after_removed_one == None:
                    print("empty list!")
                index_of_node_to_be_removed+=1
            print("bofore removal", self.length)
            node_before_removal.next = next_node_after_removed_one
            self.length = self.length - 1
            print("after removal", self.length)

    def traverse(self, index):
        print(self.length)
        if (self.length < index - 1):
            print("no such a value, index higher than list's length!")
        elif (self.length == 0):
            print("no value to return! empty linked list")
        else:
            if index == 0:
                print("At index ", index, "there is a head node ", self.head.data)
            else:
                traversed_node = self.head
                traversed_node_index = 0
                while (traversed_node_index < index):
                    traversed_node = traversed_node.next
                    traversed_node_index = traversed_node_index + 1
                print("traveresed node, with index", index, traversed_node.data)


    def reverse(self):
        #we allocate primar input,
        #the previous element before the head is None
        #the current element we start reversing is head
        #the next element after head is self.head.next

        #we must point locations of nodes before assigning, the new node.next value


        previous_node = None
        current_node = self.head
        next_node = None
        if (self.length == 1):
            print ("same list!")
            self.print_values()
        else:
            head_node = self.head
            tail_node = self.tail
            # [ ] -> [ ] -> [ ] -> [ ] -> [ ] -> [ ]

            previous_node = None
            current_node = self.head
            next_node = current_node.next


            #chanking the pointer -> next will connect the previous element
            current_node.next = previous_node
            #print("value of the previous element", previous_node)
            self.tail = current_node
            #print("tail.data", self.tail.data, " tail -> next", self.tail.next)

            while (next_node != None):

                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
                next_node = current_node.next

            self.head = current_node
            self.head.next = previous_node

            #print("revered HEAD!!!!!!!!!!!!!:", self.head.data)
            #print("reversed TAIL", self.tail.data)

if __name__ == '__main__':

    new_list = LinkedList()
    new_list.append(1)
    new_list.append(2)
    new_list.append(3)
    new_list.append(4)

    new_list.print_values()

    print("############### reversing #############")
    new_list.reverse()
    new_list.print_values()