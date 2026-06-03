class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word: str) -> None:
        for i in word:
            if i not in self.children:
                self.children[i] = WordDictionary()
            self = self.children[i]
        self.isEnd = True
        

    def search(self, word: str) -> bool:
        for i in range(len(word)):
            if word[i] == ".":
                for j in self.children.values():
                    if j.search(word[i+1:]):
                        return True
                return False
            elif word[i] in self.children:
                self = self.children[word[i]]
            else:
                return False
        return self.isEnd
