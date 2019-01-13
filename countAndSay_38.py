#!/usr/bin/python

'''38. Count and Say'''
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    def construct(s):
        s = [int(num) for num in list(s)]
        unit = s[0]
        count = 1
        res = ''
        for num in s[1:]:
            if num == unit:
                count += 1
            else:
                res += str(count) + str(unit)
                unit = num
                count = 1
        res += str(count) + str(unit)
        return res

    n_dict = {1: '1'}
    for i in range(2, n + 1):
        n_dict[i] = construct(n_dict[i - 1])

    return n_dict[n]

print(countAndSay(10))