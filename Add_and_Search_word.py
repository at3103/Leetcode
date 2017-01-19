import re
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = dict()
        self.wlength = set()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.data[word] = 1
        self.wlength.add(len(word))

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        flag = False

        if word.count('.') == 0:
            return bool(self.data.get(word,0))
        elif word.count('.') == len(word):
            if len(word) in self.wlength:
                flag = True
        else:
            length = len(word)
            if bool(self.data.get(word,0)):
                return True
            l = self.data.keys()
            for k in l:
                if length == len(k) and bool(re.match(word,k)):
                    self.addWord(word)
                    flag = True    
                    break
        
        return flag
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")