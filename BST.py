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
            #when we want to add value to the tree, we will add it to the LEAF node, which has both .left and .right
            #elements == None !, so we need to find the node which will have no more children

            current_node = self.root
            print("current node", current_node.value)
            while(current_node.left != None and current_node.right != None):
                if node.value < current_node.value:
                    current_node = current_node.left
                elif node.value > current_node.value:
                    current_node = current_node.right
            if node.value < current_node.value:
                current_node.left = node
            elif node.value > current_node.value:
                current_node.right = node
            else:
                print("current value exists!")


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

    def search(self, value):
        if self.root == None:
            print("no elements in the TREE!")
        else:
            current_node = self.root
            print("ROOT: ", self.root.value)
            while (value != current_node.value and current_node.right != None and current_node.left !=None):
                if (value > current_node.value and current_node.right != None):
                    current_node = current_node.right
                    print("current right value", current_node.value)
                elif (value < current_node.value and current_node.left != None):
                    current_node = current_node.left
                    print("current left value", current_node.value)
            if value == current_node.value:
                    print("found a value!", value)
            else:
                print("no such a value")

if __name__ == "__main__":

    my_binary_tree = BinarySearchTree()
    my_binary_tree.insert(10)
    my_binary_tree.insert(1)
    my_binary_tree.insert(20)
    my_binary_tree.insert(6)
    my_binary_tree.lookup(6)
    my_binary_tree.insert(100)
    my_binary_tree.lookup(100)
    my_binary_tree.lookup(1)
    my_binary_tree.insert(1000000000000)
    my_binary_tree.lookup(1000000000000)
    my_binary_tree.insert(0)
    my_binary_tree.lookup(0)
    my_binary_tree.insert(20)
    print("SEARCH")
    my_binary_tree.search(10000000000000000000000000000)
    my_binary_tree.insert(10000000000000000000000000000)
    my_binary_tree.search(898098098)



