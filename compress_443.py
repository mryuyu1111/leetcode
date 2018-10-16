#!/usr/bin/python

'''443. String Compression'''
def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    count = 0
    c = chars[0]
    alter_pos = 0
    final_count = 0
    for i in range(len(chars)):
        if chars[i] != c:
            chars[alter_pos] = c
            if count > 1:
                replace_len = len(str(count))
                final_count += replace_len
                for j in range(replace_len):
                    chars[alter_pos + j + 1] = str(count)[j]
                alter_pos += replace_len + 1
            elif count == 1:
                alter_pos += 1
            count = 0
            c = chars[i]
        count += 1
        if i == len(chars) - 1:
            chars[alter_pos] = c
            if count > 1:
                replace_len = len(str(count))
                final_count += replace_len
                for j in range(replace_len):
                    chars[alter_pos + j + 1] = str(count)[j]
                alter_pos += replace_len + 1
            elif count == 1:
                alter_pos += 1
    return chars[0:alter_pos]

print(compress(["a","a","b","b","c","c","c"])) # ["a","2","b","2","c","3"]
print(compress(["a","a","a","b","b","a","a"])) # ["a","3","b","2","a","2"]
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))