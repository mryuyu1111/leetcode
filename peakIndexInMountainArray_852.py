#!/usr/bin/python

'''852. Peak Index in a Mountain Array'''
def peakIndexInMountainArray(A):
    """
    :type A: List[int]
    :rtype: int
    """
    old_d = d = 0
    old_u = u = len(A)-1
    h = int(len(A)/2)
    while True:
        right = h + 1
        left = h - 1
        if A[right] < A[h] and A[left] < A[h]:
            return h
        if A[right] > A[h]:
            d = old_d = right
            new_h = right + int(len(A[d:old_u])/2)
            old_u = u
        if A[left] > A[h]:
            u = old_u = left
            new_h = old_d + int(len(A[old_d:u])/2)
            old_d = d
        h = new_h

print(peakIndexInMountainArray([40,48,61,75,100,99,98,39,30,10]))