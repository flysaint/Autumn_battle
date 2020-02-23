# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:06:00 2020

@author: fly_s

53.maximum-sum-subarray-en

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

class solution(object):
    def get_max_sum(self,arr):
        max_sum = arr[0]
        max_axis = [0,1]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                if sum(arr[i:j]) > max_sum:
                    max_sum = sum(arr[i:j])
                    max_axis = [i,j]
        
        
        return max_sum,max_axis
                    
                    


if __name__ == "__main__":
    s = solution()
    
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    
    print(s.get_max_sum(arr))
    