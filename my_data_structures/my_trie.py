from my_trie_node import MyTrieNode
from typing import Union


class MyTrie:
    def __init__(self) -> None:
        self.root = MyTrieNode()

    def search(self, word: str) -> Union[MyTrieNode, None]:
        current_node = self.root
        for char in word:
            el = current_node.children.get(char, None)
            if el is None:
                return None
            current_node = el
        return current_node

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            el = current_node.children.get(char, None)
            if el is None:
                current_node.children[char] = MyTrieNode()
            current_node = current_node.children[char]
        current_node.children["*"] = None


trie = MyTrie()
trie.insert("cat")
trie.insert("catniss")
n = trie.search("cat")
