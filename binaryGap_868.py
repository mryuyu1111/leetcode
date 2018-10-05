def binaryGap(N):
    """
    :type N: int
    :rtype: int
    """
    b = bin(N)[2:]
    d = 0
    count = None
    for c in b:
        if c == '1':
            if count:
                if count > d:
                    d = count
            count = 1
        else:
            if count:
                count += 1
    return d

print(binaryGap(22))