# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:40:42 2020

@author: fly_s

26.remove-duplicates-from-sorted-array

统计有序数组中，非重复数字的数量。
要求 时间复杂度 O(n)，空间复杂度 O(1)

Example 1:

Given nums = [1,1,2],
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

## 题目描述

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:
    
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

"""

'''
思路
核心思路：使用快慢指针来记录遍历的坐标。
快指针遍历所有值，慢指针只有确认是非重复值的时候才会走

Step1:开始时这两个指针都指向第一个数字
Step2:如果两个指针指的数字相同，则快指针向前走一步
Step3:如果不同，则两个指针都向前走一步
Step4:当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数
'''

class sulution(object):
    def get_duplicates_cnt(self,arr):
        fast = 0
        slow = 0
        lens = len(arr)
        while(fast < lens):
            #print("fast = {},slow = {},arr[fast] = {},arr[slow] = {}".format(fast,slow,arr[fast],arr[slow]))
            if arr[fast] == arr[slow]:
                fast += 1
            if arr[fast] != arr[slow]:
                arr[slow+1] = arr[fast]
                fast += 1
                slow += 1
                
        return slow+1

    



if __name__ == "__main__":
    s = sulution()
    
    arr1 = [1,1,2]
    
    arr2 = [0,0,1,1,1,2,2,3,3,4]
    
    print(s.get_duplicates_cnt(arr1))
    print(s.get_duplicates_cnt(arr2))




















