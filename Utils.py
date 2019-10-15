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


def getheight(node):
    if not node:
        return 0
    else:
        return max(getheight(node.left), getheight(node.right)) + 1

def add_padding(str, pad_length_value):
    str = str.strip()
    return str.center(pad_length_value, ' ')

# sotre node , space and slashes in list first, then print out
def pretty_print(tree):
    output = StringIO()
    pretty_output = StringIO()

    current_level = Queue()
    next_level = Queue()
    current_level.enqueue(tree)
    depth = 0

    # get the depth of current tree
    # get the tree node data and store in list
    if tree:
        while not current_level.isEmpty():
            current_node = current_level.dequeue()
            output.write('%s ' % current_node.data if current_node else 'N ')
            next_level.enqueue(
                current_node.left if current_node else current_node)
            next_level.enqueue(
                current_node.right if current_node else current_node)

            if current_level.isEmpty():
                if sum([i is not None for i in next_level.queue]
                       ):  # if next level has node
                    current_level, next_level = next_level, current_level
                    depth = depth + 1
                output.write('\n')
    print('the tree print level by level is :')
    print(output.getvalue())
    print("current tree's depth is %i" % (depth+1))

    # add space to each node
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
        print('current slashes depth im_resize:')
        print(spaces)
        print("current levle's list is:")
        print(keys)
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


class tree(object):
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


def get_random_tree(num = 10):
	'''
	得到值在1~20之间，数量为num的随机二叉树
	'''
    nodes = []
    node1=tree(1)
    node2=tree(2)
    node3=tree(3)
    node4=tree(4)
    node5=tree(5)
    node6=tree(6)
    node7=tree(7)
    node8=tree(8)
    node9=tree(9)
    node10=tree(10)
    node11=tree(11)
    node12=tree(12)
    node13=tree(13)
    node14=tree(14)
    node15=tree(15)
    node16=tree(16)
    node17=tree(17)
    node18=tree(18)
    node19=tree(19)
    node20=tree(20)
    
    for i in range(1,21):
        nodes.append(eval("node"+str(i)))
    
    lst = random.sample(range(20),num)
    
    out_nodes = [nodes[i] for i in lst]
    
    for i in range(0,int(len(out_nodes)/2)):
        #print( "i = {},2*i+1 = {},2*i+2 = {}".format(i,2*i+1,2*i+2))
        out_nodes[i].left = out_nodes[2*i+1]
        if 2*i+2 < len(out_nodes):
            out_nodes[i].right = out_nodes[2*i+2]
        
    
    return out_nodes[0]


#pretty_print(get_random_tree(10))
    

 