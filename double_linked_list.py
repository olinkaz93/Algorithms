class DoubleNode():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = DoubleNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = DoubleNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def traverse(self, index):
        #some edge cases might be solved here
        #we can assume index will be always in the range of the length of the list

        counter = 0
        current_node = self.head
        #previous_node = self.head.previous
        #next_node = self.head.next
        #if(index >= self.length):
        #    return None
        while (index != counter):
            current_node = current_node.next
            counter += 1

        #print("previous node before index: ", index, " is", current_node.previous)
        print("current at index: ", index, " is", current_node.data)
        #print("next node after index: ", index, " is", current_node.next)
        return (current_node)

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
        if (index == 0):
            self.prepend(data)
            return
        elif (index == self.length ):
            self.append(data)
            return
        else:
            new_node = DoubleNode(data)
            leader = self.traverse(index - 1)
            follower = leader.next
            leader.next = new_node
            new_node.previous = leader
            new_node.next = follower
            follower.previous = new_node
            self.length += 1

    def remove(self, index):
        if (self.length == 1):
            self.head = None
            self.tail = self.head
            self.length -= 1
        elif (index == 0):
            follower = self.head.next
            follower.previous = None
            self.head = follower
            self.length -= 1
        elif (index >= self.length - 1):
            leader = self.traverse(index - 1 )
            leader.next = None
            self.tail = leader
            self.length -= 1
        else:
            leader = self.traverse(index - 1)
            node_to_remove = self.traverse(index)
            follower = self.traverse(index + 1)
            leader.next = follower
            follower.previous = leader
            self.length -=1



if __name__ == '__main__':

    new_double_list = DoubleLinkedList()
    new_double_list.append(5)
    new_double_list.append(4)
    #print("The head", new_double_list.head.data)

    new_double_list.prepend(10)
    print("The head", new_double_list.head.data)
    print("The tail", new_double_list.tail.data)
    new_double_list.traverse(0)
    new_double_list.traverse(1)
    new_double_list.traverse(2)

    new_double_list.print_values()

    print("element at index 0")
    first_element = new_double_list.traverse(0)
    print(first_element.data)
    new_double_list.insert(0, 50)
    new_double_list.print_values()
    new_double_list.insert(4, 100)
    new_double_list.print_values()
    new_double_list.insert(1, 10000000000000)
    new_double_list.print_values()
    new_double_list.remove(0)
    new_double_list.print_values()
    new_double_list.remove(1)
    new_double_list.print_values()
    new_double_list.remove(0)
    new_double_list.print_values()
    #new_double_list.remove(2)
    #new_double_list.print_values()
    print("The head", new_double_list.head.data)
    print("The tail", new_double_list.tail.data)
    print(new_double_list.length)
    new_double_list.remove(2)
    new_double_list.print_values()
    print("The head", new_double_list.head.data)
    print("The tail", new_double_list.tail.data)
    new_double_list.remove(0)
    new_double_list.print_values()
    print("The head", new_double_list.head.data)
    print("The tail", new_double_list.tail.data)
    new_double_list.remove(0)
    new_double_list.print_values()




