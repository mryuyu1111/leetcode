def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    start = 0
    end = len(height) - 1
    vol = 0
    while end - start >= 1:
        current_vol = min(height[start], height[end]) * (end - start)
        if current_vol > vol:
            vol = current_vol
        if height[start] >= height[end]:
            end -= 1
        else:
            start += 1
    return vol

print(maxArea([1,8,6,2,5,4,8,3,7]))