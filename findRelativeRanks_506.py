#!/usr/bin/python

'''506. Relative Ranks'''
def findRelativeRanks(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    metals = {1:"Gold Medal", 2:"Silver Medal", 3:"Bronze Medal"}
    index_dict = {nums[i]:i for i in range(len(nums))}
    sorted_nums = nums
    sorted_nums.sort(reverse=True)
    rank_dict = {sorted_nums[r-1]:r for r in range(1,len(sorted_nums)+1)}
    ranks = [0] * len(nums)
    for n in nums:
        index = index_dict[n]
        ranking = rank_dict[n]
        if ranking <= 3:
            ranking = metals[ranking]
        ranks[index] = str(ranking)
    return ranks

print(findRelativeRanks([10,3,8,9,4]))