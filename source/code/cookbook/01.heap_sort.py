#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def heap_sort(nums):
    first = len(nums)//2-1
    for start in range(first,-1,-1): 
        big_heap(nums,start,len(nums)-1)

    for end in range(len(nums)-1,0,-1):
        nums[0],nums[end] = nums[end],nums[0]
        big_heap(nums,0,end-1)

def big_heap(nums,start,end):
    root = start 
    child = root*2 +1

    while child<=end:
        if child +1 <=end and nums[child] < nums[child+1]: 
            child +=1 
        if nums[root] < nums[child]: 
            nums[root],nums[child] = nums[child],nums[root]
            root = child 
            child=root*2+1
        else: 
            break 

if __name__ == "__main__": 
    nums=[10,17,50,7,30,24,27,45,15,5,36,21]
    print(heap_sort(nums))
