def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    flag = False
    one = True
    for b in bits:
        if flag:
            flag = False
            one = False
        else:
            if b == 1:
                flag = True
            else:
                one = True
    return one

print(isOneBitCharacter([1,1,1,0]))