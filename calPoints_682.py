def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    valid = []
    for n in ops:
        if n == 'C':
            valid.pop()
        elif n == 'D':
            valid.append(valid[-1] * 2)
        elif n == '+':
            valid.append(sum(valid[-2:]))
        else:
            valid.append(int(n))
    return sum(valid)

print(calPoints(["-9","-40","-35","D","73"]))