#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (42.08%)
# Total Accepted:    309.1K
# Total Submissions: 734.5K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
                head = head.next
        return temp

if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(3)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4    
    result = Solution().deleteDuplicates(head)
    while result:
        print(result.val)
        result = result.next

        

