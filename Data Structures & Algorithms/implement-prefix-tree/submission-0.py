class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEnd = False


    def insert(self, word: str) -> None:
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = PrefixTree()
            cur = cur.children[i]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for i in prefix:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        return True
        
        