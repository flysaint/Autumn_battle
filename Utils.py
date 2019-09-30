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
    
    