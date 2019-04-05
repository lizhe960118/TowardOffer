#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (37.24%)
# Total Accepted:    167K
# Total Submissions: 448.5K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#

class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.is_end = False 
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.root
        for char_s in word:
            if char_s not in cur_node.child:
                next_node = TrieNode()
                cur_node.child[char_s] = next_node
            cur_node = cur_node.child[char_s]
        cur_node.is_end = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.root
        for char_s in word:
            if char_s not in cur_node.child:
                return False
            else:
                cur_node = cur_node.child[char_s]
        return cur_node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for char_s in prefix:
            if char_s not in cur_node.child:
                return False
            else:
                cur_node = cur_node.child[char_s]
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

