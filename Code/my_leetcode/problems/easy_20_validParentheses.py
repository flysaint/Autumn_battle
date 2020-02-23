# -*- coding: utf-8 -*-
"""

easy_20_validParentheses

Created on Mon Feb 17 03:10:07 2020

@author: fly_s

题目地址
https://leetcode.com/problems/valid-parentheses/description

easy_20_validParentheses
题目描述
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true



"""
'''
核心思路：
1. 遍历字符串。
2. 遇到正向符号，直接保存对应的反向的符号。 
3. 遇到反向符号，将保存在栈尾的符号出栈，进行对比。
4. 不断遍历，不断出栈。
'''

class Solution:
    def isValid(self,strs):
        dic = {
                "{":"}",
                "[":"]",
                "(":")"
                }
        stack = []
        for s in strs:
            if s in dic:
                stack.append(dic[s])
            else:
                if len(stack) != 0:
                    top_s = stack.pop()
                    if s == top_s:
                        continue
                    else:
                        return False
                else:
                    return False
        return True

'''

class Solution:
    def isValid(self,strs):
        stack = []
        dic = {"{":"}","[":"]","(":")"}
        
        for s in strs:
            if s in dic:
                stack.append(dic[s])
            else:
                if len(stack) != 0:
                    top_s = stack.pop()
                    if top_s == s:
                        continue
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0

'''        
        
        
if __name__ == "__main__":
    s = Solution()
    
    print(s.isValid("{([)]"))




    
    
    
    
    



















    
    
    
    
    
    
        
    
