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

    def remove(self, value):
        value_to_remove = value
        if self.root == None:
            print("Nothing to remove, BST is empty")
        else:
            current_node = self.root
            parent_node = None
            while(True):
                if(value_to_remove < current_node.value and current_node.left != None):
                    parent_node = current_node
                    current_node = current_node.left
                elif(value_to_remove > current_node.value and current_node.right != None):
                    parent_node = current_node
                    current_node = current_node.right
                elif(value_to_remove == current_node.value):
                    print("found it, now remove it!")
                    print("parent", current_node.value)
                    #when the node to remove is the root we must update the self.root
                    #when the node to remove is a leaf element - has no right neither left children
                    if (current_node.left == None and current_node.right == None):
                        if (parent_node == None):
                            self.root = None
                            return
                        elif current_node.value > parent_node.value:
                            parent_node.right = None
                            return
                        elif current_node.value < parent_node.value:
                            parent_node.left = None
                        return
                    #when the node to remove had only the right leaf
                    elif (current_node.left == None and current_node.right != None):
                        #we must link, this leaf to the parent node, accordingly wethher the value is > or <
                        if parent_node == None:
                            self.root = current_node.right
                            return
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                        elif current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                    elif (current_node.left != None and current_node.right == None):
                        if parent_node == None:
                            self.root = current_node.left
                            return
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                            return
                        elif current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                            return
                    #if the node had 2 children, we move the .right children link to the parent
                    elif (current_node.left != None and current_node.right != None):
                        #if we remove root we must find the new
                        if parent_node == None:
                            self.root = current_node.right
                            return
                        #elif current_node.value > parent_node.value:
                        #    parent_node.right = cu

                else:
                    print("no value!")
                    return

    #DFS traversal
    def DFS_inorder(self, node, my_list):
        if node != None:
            self.DFS_inorder(node.left, my_list)
            my_list.append(node.value)
            self.DFS_inorder(node.right, my_list)
        return my_list

    def DFS_preorder(self, node, my_list):
        if node != None:
            my_list.append(node.value)
            self.DFS_inorder(node.left, my_list)
            self.DFS_inorder(node.right, my_list)
        return my_list

    def DFS_postorder(self, node, my_list):
        if node != None:
            self.DFS_inorder(node.left, my_list)
            self.DFS_inorder(node.right, my_list)
            my_list.append(node.value)
        return my_list

    def PreOrder(self, node, list):
        if (node == None):
            return
        list.append(node.value)
        self.PreOrder(node.left, list)
        self.PreOrder(node.right, list)
        return list

    def InOrder(self, node, list):
        if (node == None):
            return
        self.PreOrder(node.left, list)
        list.append(node.value)
        self.PreOrder(node.right, list)
        return list

    def PostOrder(self, node, list):
        if (node == None):
            return
        self.PreOrder(node.left, list)
        self.PreOrder(node.right, list)
        list.append(node.value)
        return list



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
    my_binary_tree.remove(2)
    my_binary_tree.remove(20)
    my_binary_tree.insert(100)
    my_binary_tree.insert(150)
    my_binary_tree.insert(1110)
    my_binary_tree.insert(7)
    print(my_binary_tree.DFS_inorder(my_binary_tree.root, []))
    print(my_binary_tree.DFS_preorder(my_binary_tree.root, []))
    print(my_binary_tree.DFS_postorder(my_binary_tree.root, []))
    result = my_binary_tree.PreOrder(my_binary_tree.root, [])
    print("PreOrder DFS", result)
    result = my_binary_tree.InOrder(my_binary_tree.root, [])
    print("InOrder DFS", result)
    result = my_binary_tree.PostOrder(my_binary_tree.root, [])
    print("PostOrder DFS", result)
