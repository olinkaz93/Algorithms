#implementation of binary search tree

#insert and lookup

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right= None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            current_node = self.root

            while True:
                if node.value == current_node.value:
                    print("This value is already in the tree!")
                    return
                elif node.value < current_node.value:
                    if current_node.left == None:
                        current_node.left = node
                        return
                    else:
                        current_node = current_node.left
                elif node.value > current_node.value:
                    if current_node.right == None:
                        current_node.right = node
                        return
                    else:
                        current_node = current_node.right


    def lookup(self, value):
        if (self.root == None):
            print("nothing to print, the Tree is empty")
        else:
            current_node = self.root
            print("current node", current_node.value)
            while True:
                if value < current_node.value and current_node.left != None:
                    current_node = current_node.left
                elif value > current_node.value and current_node.right != None:
                    current_node = current_node.right
                elif value == current_node.value:
                    print("found a value!", value)
                    return
                else:
                    print("no such a value")
                    return

    """
    def print_tree(self):
        if self.root == None:
            print("nothing to print")
        else:
            current_node = self.root
            level = 1
            print("level: ", level, "root: ", self.root.value)
            while (current_node.left.value != None or current_node.right.value != None):
    """


if __name__ == "__main__":

    my_binary_tree = BinarySearchTree()
    my_binary_tree.insert(10)
    my_binary_tree.insert(1)
    my_binary_tree.insert(20)
    my_binary_tree.insert(6)
    my_binary_tree.lookup(6)
    my_binary_tree.lookup(100)
    my_binary_tree.lookup(10)
    my_binary_tree.lookup(6)
    my_binary_tree.insert(6)
    my_binary_tree.insert(10)
    my_binary_tree.insert(20)


