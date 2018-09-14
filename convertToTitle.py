'''168. Excel Sheet Column Title'''
def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    s = ''
    letter_num_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
                       6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
                       11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
                       16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
                       21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
                       26: 'Z'}

    num = 26.0
    count = 1
    while True:
        if n / num > 1:
            count += 1
            num += 26 ** count
        else:
            break

    for i in range(count):
        if i != count - 1:
            num = n - 26 ** (count - i - 1)
            num = int((num - 1) / 26 ** (count - i - 1) + 1)
            s += letter_num_dict[num]
            n -= 26 ** (count - i - 1) * num
        else:
            s += letter_num_dict[n]
    return s


print(convertToTitle(701))
# print(convertToTitle(703))
# print(convertToTitle(24568))