class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)

        else:
            self._insert(self.root, key)


    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)

        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
        else:
            print(f"{key} alredy exists")


            # //////////////////search

        def search (self, key):
            return self._search(self.root, key)
        
        def _search(self, node, key):
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return self._search(node.left, key)
            else:
                return self._search(node.right, key)
            

        # ////////////////////////////delete
        def delete(self,key):
            self.root = self._delete(self.root, key)


        def _delet(self, node, key):
            if node is None:
                return None
            
            if key < node.key:
                node.left = self._delete(node.left, key)
            elif key > node.key:
                node.right = self._delete(node.right, key)

            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                else:
                    successor = self._min_value_node(node.right)
                    node.key = successor.key
                    node.right = self._delete(node.right, successor.key)

                return node

        def _min_value_node(self, node):
            current = node
            while current.left is not None:
                current = current.left
            return current
        # inorder
        def inorder(self):
            self._inorder(self.root)
            print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=" ")
            self._inorder(node.right)

        

        # test

        if __name__ == "__main__":
            tree = BST()
            for val in [10,30,70,20]:
                tree.insert(val)

            print("inorder befor deletion")
            tree.inorder()



