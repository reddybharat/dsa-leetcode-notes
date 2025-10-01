# Brute Force Example: Container With Most Water
# - Check all possible pairs of lines.
# - For each pair, calculate the area and keep track of the maximum.
# - This is simple but slow: O(n^2) time complexity.

def maxAreaBruteForce(heights: list[int]) -> int:
    n = len(heights)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            area = (j - i) * min(heights[i], heights[j])
            max_area = max(max_area, area)
    return max_area



# Two Pointer Example: Container With Most Water
# - Start with one pointer at the beginning (left) and one at the end (right).
# - Calculate the area between the lines at left and right.
# - Move the pointer at the shorter line inward (since the area is limited by the shorter line).
# - Repeat until the pointers meet. This gives the maximum area efficiently (O(n)).

def maxAreaTwoPointer(heights: list[int]) -> int:
    left, right = 0, len(heights)-1
    max_area = 0

    while left < right:
        max_area = max(max_area, (right - left) * min(heights[left], heights[right]))
        
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1

    return max_area
