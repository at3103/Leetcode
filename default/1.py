import itertools

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        finallist =list()
        small =["",600000]
        #for word in words:
        #    if len(word) <=small[1]:
        #        small = [word,len(word)]
        
        wordset= set(words)
        
        for i in range(len(words)):
            word = words[i]
            for j in range(len(words)-1):
                tempwordset=wordset-{word}
                newword=""
                for k in range(j+1):
                    wordlist=list(tempwordset)
                    print wordlist
                    newword +=wordlist[0]
                    tempwordset-={wordlist[0]}
                print "new word is ",newword
                checkword = word+newword
                if checkword in wordset:
                    finallist.append(checkword)
                print finallist
            
        return finallist
        
        