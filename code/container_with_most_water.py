def max_area_bruteforce(heights):
    """
    Time: O(n^2)
    Space: O(1)
    """
    n = len(heights)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(heights[i], heights[j])
            max_area = max(max_area, area)
    return max_area


def max_area_two_pointer(heights):
    """
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, (right - left) * min(heights[left], heights[right]))
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return max_area
