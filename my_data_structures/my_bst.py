from my_tree_node import MyTreeNode
from typing import Union


class MyBinarySearchTree:
    def __init__(self) -> None:
        pass

    def search(self, node: MyTreeNode, value: object) -> Union[MyTreeNode, None]:
        if node.left is None and node.right is None and node.value != value:
            return None
        if node.value == value:
            return node
        elif value > node.value:
            return self.search(node.right, value)
        elif value < node.value:
            return self.search(node.left, value)

    def insert(self, tree_node: MyTreeNode, node: MyTreeNode) -> None:
        if tree_node.value < node.value:
            if tree_node.right is None:
                tree_node.right = node
            else:
                return self.insert(tree_node.right, node)
        elif tree_node.value > node.value:
            if tree_node.left is None:
                tree_node.left = node
            else:
                return self.insert(tree_node.left, node)

    def delete(self, value) -> Union[MyTreeNode, None]:
        pass

    def traverse(self) -> None:
        pass


root = MyTreeNode(1)
n1 = MyTreeNode(5)
n2 = MyTreeNode(3)
n3 = MyTreeNode(10)
n4 = MyTreeNode(6)
tree = MyBinarySearchTree()
tree.insert(root, n1)
tree.insert(root, n2)
tree.insert(root, n3)
tree.insert(root, n4)
print(tree.search(root, n4.value).value)
