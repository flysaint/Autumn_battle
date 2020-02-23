# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:00:02 2020

@author: fly_s

hard_02_add-two-numbers

You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 4) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 442 + 465 = 907.
"""


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        # dummy head
        head = curr = ListNode(0)
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = val // 10
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
          




if __name__ == "__main__":
    
    s = solution()
    
    
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(4)
    
    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    
    
    node1.next = node2
    node2.next = node3
    
    node4.next = node5
    node5.next = node6
    
    node = node1
    
    head = s.addTwoNumbers(node1,node4)
    
    while(head):
        print(head.val)
        head = head.next
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
''' 
class solution(object):
    def addTwoNumbers(self, l1, l2):
            head = ListNode(0)
            # curr is the dummy linked list
            curr = head
            carry = 0
            
            while l1 or l2:
                x = l1.val if l1 else 0
                y = l2.val if l2 else 0
                
                sum_node = x + y + carry
                carry = sum_node // 10
                curr.next = ListNode(sum_node % 10)
                # pointer move to the next node
                curr =  curr.next
                
                
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            # finally there need to carry
            if (carry > 0):
                curr.next = ListNode(1)
            return head.next    
    
'''    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





























