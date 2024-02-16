class Trie(object):

    def __init__(self):
        self.trie = []

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.trie.append([word])

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for val in self.trie:
            if word in val:
                return True
        return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        for val in self.trie:
            if val[0][:len(prefix)] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)