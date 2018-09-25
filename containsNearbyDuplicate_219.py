#! /usr/bin/python

def containsNearbyDuplicate(nums, k):
    """ 219. Contains Duplicate II
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    d = dict()
    for i in range(len(nums)):
        if nums[i] in d:
            if abs(d[nums[i]] - i) <= k:
                return True
        d[nums[i]] = i
    return False

print (containsNearbyDuplicate([1,2,3,1],3))
print (containsNearbyDuplicate([1,0,1,1],1))
print (containsNearbyDuplicate([1,2,3,1,2,3],2))