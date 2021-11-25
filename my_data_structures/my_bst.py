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
                self.insert(tree_node.right, node)
        elif tree_node.value > node.value:
            if tree_node.left is None:
                tree_node.left = node
            else:
                self.insert(tree_node.left, node)

    def delete(self, tree_node: MyTreeNode, node: MyTreeNode) -> Union[MyTreeNode, None]:
        pass

    def traverse_in_order(self, tree_node: MyTreeNode) -> None:
        # in-order traversing
        if tree_node is None:
            return
        self.traverse_in_order(tree_node.left)
        print(tree_node.value)
        self.traverse_in_order(tree_node.right)

    def traverse_preorder(self, tree_node: MyTreeNode):
        if tree_node is None:
            return
        print(tree_node.value)
        self.traverse_in_order(tree_node.left)
        self.traverse_in_order(tree_node.right)

    def traverse_postorder(self, tree_node: MyTreeNode):
        if tree_node is None:
            return
        self.traverse_in_order(tree_node.left)
        self.traverse_in_order(tree_node.right)
        print(tree_node.value)

    def get_biggest_number(self, tree_node: MyTreeNode):
        if tree_node.right is None:
            return tree_node.value
        return self.get_biggest_number(tree_node.right)


root = MyTreeNode(55)
n1 = MyTreeNode(25)
n2 = MyTreeNode(17)
n3 = MyTreeNode(11)
n4 = MyTreeNode(33)
n5 = MyTreeNode(61)
n6 = MyTreeNode(89)
n7 = MyTreeNode(30)
n8 = MyTreeNode(40)
n9 = MyTreeNode(56)
n10 = MyTreeNode(82)
n11 = MyTreeNode(95)

tree = MyBinarySearchTree()
tree.insert(root, n1)
tree.insert(root, n2)
tree.insert(root, n3)
tree.insert(root, n4)
tree.insert(root, n5)
tree.insert(root, n6)
tree.insert(root, n7)
tree.insert(root, n8)
tree.insert(root, n9)
tree.insert(root, n10)
tree.insert(root, n11)
print("In order")
print(tree.traverse_in_order(root))
print("Pre order")
print(tree.traverse_preorder(root))
print("Post order")
print(tree.traverse_postorder(root))
print("Biggest number = ", tree.get_biggest_number(root))
