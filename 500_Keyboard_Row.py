"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.



Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

from functools import reduce

def word_helper(word, kboard):
    word  = word.lower()
    return reduce(lambda acc, x: acc + kboard.get(x), word, 0) == len(word) * kboard.get(word[0],0)
    

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = {k:1 for  k in 'qwertyuiop'}
        keyboard.update({k:10 for  k in 'asdfghjkl'})
        keyboard.update({k:100 for  k in 'zxcvbnm'})
        
        return [word for word in words if word_helper(word, keyboard)]