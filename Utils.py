# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:19:02 2019

@author: DELL
@进行使用工具类

"""

import pandas as pd
import numpy as np
import random
import copy


class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None


def get_singe_linklist(num = 10):
    # 生成 小于 20的，数量为10的树
    LinkNodes = []
    LinkNode0=LinkNode(0)
    LinkNode1=LinkNode(1)
    LinkNode2=LinkNode(2)
    LinkNode3=LinkNode(3)
    LinkNode4=LinkNode(4)
    LinkNode5=LinkNode(5)
    LinkNode6=LinkNode(6)
    LinkNode7=LinkNode(7)
    LinkNode8=LinkNode(8)
    LinkNode9=LinkNode(9)
    LinkNode10=LinkNode(10)
    LinkNode11=LinkNode(11)
    LinkNode12=LinkNode(12)
    LinkNode13=LinkNode(13)
    LinkNode14=LinkNode(14)
    LinkNode15=LinkNode(15)
    LinkNode16=LinkNode(16)
    LinkNode17=LinkNode(17)
    LinkNode18=LinkNode(18)
    LinkNode19=LinkNode(19)
    
    for i in range(20):
        LinkNodes.append(eval("LinkNode"+str(i)))
        
    lst = [i for i in range(20)]
    
    out_LinkNodes = [LinkNodes[i] for i in lst]
    
    return out_LinkNodes[:num]



def get_Arr(cnt):
    
    testArr1 = random.sample(range(cnt),cnt)
    testArr2 = copy.copy(testArr1)
    testArr3 = copy.copy(testArr1)
    testArr3 = sorted(testArr3)
    
    return testArr1,testArr2,testArr3

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    
 

from collections import namedtuple
from io import StringIO
import math
import random

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, b):
        self.queue.insert(0, b)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []


def getheight(TreeNode):
    if not TreeNode:
        return 0
    else:
        return max(getheight(TreeNode.left), getheight(TreeNode.right)) + 1

def add_padding(str, pad_length_value):
    str = str.strip()
    return str.center(pad_length_value, ' ')

# sotre TreeNode , space and slashes in list first, then print out
def pretty_print(tree):
    output = StringIO()
    pretty_output = StringIO()

    current_level = Queue()
    next_level = Queue()
    current_level.enqueue(tree)
    depth = 0

    # get the depth of current tree
    # get the tree TreeNode data and store in list
    if tree:
        while not current_level.isEmpty():
            current_TreeNode = current_level.dequeue()
            #output.write('%s ' % current_TreeNode.data if current_TreeNode else 'N ')
            next_level.enqueue(
                current_TreeNode.left if current_TreeNode else current_TreeNode)
            next_level.enqueue(
                current_TreeNode.right if current_TreeNode else current_TreeNode)

            if current_level.isEmpty():
                if sum([i is not None for i in next_level.queue]
                       ):  # if next level has TreeNode
                    current_level, next_level = next_level, current_level
                    depth = depth + 1
                #output.write('\n')
    #print('the tree print level by level is :')
    #print(output.getvalue())
    #print("current tree's depth is %i" % (depth+1))

    # add space to each TreeNode
    output.seek(0)
    pad_length = 3
    keys = []
    spaces = int(math.pow(2, depth))

    while spaces > 0:
        skip_start = spaces * pad_length
        skip_mid = (2 * spaces - 1) * pad_length

        key_start_spacing = ' ' * skip_start
        key_mid_spacing = ' ' * skip_mid

        keys = output.readline().split(' ')  # read one level to parse
        padded_keys = (add_padding(key, pad_length) for key in keys)
        padded_str = key_mid_spacing.join(padded_keys)
        complete_str = ''.join([key_start_spacing, padded_str])

        pretty_output.write(complete_str)

        # add space and slashes to middle layer
        slashes_depth = spaces
        #print('current slashes depth im_resize:')
        #print(spaces)
        #print("current levle's list is:")
        #print(keys)
        spaces = spaces // 2
        if spaces > 0:
            pretty_output.write('\n')  # print '\n' each level

            cnt = 0
            while cnt < slashes_depth:
                inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                symbol_start_spacing = ' ' * (skip_start-cnt-1)
                symbol_mid_spacing = ' ' * (skip_mid-2*(cnt+1))
                pretty_output.write(''.join([symbol_start_spacing, symbol]))
                for i in keys[1:-1]:
                    pretty_output.write(''.join([symbol_mid_spacing, symbol]))
                pretty_output.write('\n')
                cnt = cnt + 1

    print(pretty_output.getvalue())


class TreeNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None


def get_random_tree(num = 10):
    # 生成 小于 20的，数量为10的树
    TreeNodes = []
    TreeNode0=TreeNode(0)
    TreeNode1=TreeNode(1)
    TreeNode2=TreeNode(2)
    TreeNode3=TreeNode(3)
    TreeNode4=TreeNode(4)
    TreeNode5=TreeNode(5)
    TreeNode6=TreeNode(6)
    TreeNode7=TreeNode(7)
    TreeNode8=TreeNode(8)
    TreeNode9=TreeNode(9)
    TreeNode10=TreeNode(10)
    TreeNode11=TreeNode(11)
    TreeNode12=TreeNode(12)
    TreeNode13=TreeNode(13)
    TreeNode14=TreeNode(14)
    TreeNode15=TreeNode(15)
    TreeNode16=TreeNode(16)
    TreeNode17=TreeNode(17)
    TreeNode18=TreeNode(18)
    TreeNode19=TreeNode(19)
    
    for i in range(20):
        TreeNodes.append(eval("TreeNode"+str(i)))
    
    lst = random.sample(range(20),num)
    
    out_TreeNodes = [TreeNodes[i] for i in lst]
    
    for i in range(0,int(len(out_TreeNodes)/2)):
        #print( "i = {},2*i+1 = {},2*i+2 = {}".format(i,2*i+1,2*i+2))
        out_TreeNodes[i].left = out_TreeNodes[2*i+1]
        if 2*i+2 < len(out_TreeNodes):
            out_TreeNodes[i].right = out_TreeNodes[2*i+2]
    
    return out_TreeNodes[0],lst




#pretty_print(get_random_tree(10))
    

 