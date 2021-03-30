from linked_list import Node, LinkedList

new_list = LinkedList()
new_list.append("my new list")
new_list.print_values()

class ListWithBetterTraversing(LinkedList):
    def traverse_v2(self, index):
        counter = 0
        actual_node = self.head
        while (counter != index):
            actual_node = actual_node.next
            counter += 1
        print("element at index: ", index, "value/data: ", actual_node.data)
        print("element after this is: ", actual_node.next)

another_list = ListWithBetterTraversing()
another_list.append("element")
another_list.traverse_v2(0)
