def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    :type buckets: int
    :type minutesToDie: int
    :type minutesToTest: int
    :rtype: int
    """
    pig = 0
    while (minutesToTest / minutesToDie + 1) ** pig < buckets:
        pig += 1
    return pig

print(poorPigs(1000,15,60))