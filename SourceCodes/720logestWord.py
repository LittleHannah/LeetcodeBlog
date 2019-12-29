'''
720 字典中最长的单词

给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。
若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。
'''


from DataStructure import TrieNode
import collections
from functools import reduce

# example input
words1 = ["w","wo","wor","worl", "world"]
# example output
# 'world'

# example input
words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# example output
# 'apple'



def longestWord(words):
    wordset = set(words)
    words.sort(key = lambda c: (-len(c), c))
    for word in words:
        if all(word[:k] in wordset for k in range(1, len(word))):
            return word
    return ""


print(words1,'中最长的符合条件的单词为', longestWord(words1))
print(words2,'中最长的符合条件的单词为', longestWord(words2))
