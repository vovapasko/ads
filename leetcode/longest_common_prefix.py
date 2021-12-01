class MyTrieNode:
    def __init__(self) -> None:
        self.children = {}


class MyTrie:
    def __init__(self) -> None:
        self.root = MyTrieNode()

    def insert(self, word: str):
        node = self.root
        for w in word:
            child = node.children.get(w, None)
            if child is None:
                node.children[w] = MyTrieNode()
                child = node.children[w]
            node = child
        node.children["*"] = None

    def get_common_str(self) -> str:
        return self.__search(self.root, "")

    def __search(self, node: MyTrieNode, word: str = ""):
        value = list(node.children.keys())[0]
        if len(node.children) > 1 or value == "*":
            return word
        child = node.children[value]
        return self.__search(child, word + value)
