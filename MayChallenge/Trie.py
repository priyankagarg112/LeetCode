'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Node:
    def __init__(self):
        self.children = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def _getindex(self, a):
        return ord(str(a))-ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        head = self.root
        for l in word:
            index = self._getindex(l)
            if head.children[index]:
                head =head.children[index]
                continue
            head.children[index] = Node()
            head =head.children[index]
        # print("-----------")
        head.end=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # print("----------------")
        head = self.root
        for l in word:
            index = self._getindex(l)
            if head.children[index]:
                head = head.children[index]
                continue
            return False
        if head.end:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        head = self.root
        for l in prefix:
            index = self._getindex(l)
            if not head.children[index]:
                return False
            head = head.children[index]

        return True
