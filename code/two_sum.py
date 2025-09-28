def two_sum_bruteforce(nums, target):
    """
    Brute-force approach: Check all pairs.
    Time: O(n^2), Space: O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_optimized(nums, target):
    """
    Optimized approach: Use a hash map to find complement in one pass.
    Time: O(n), Space: O(n)
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i

# Example usage:
# print(two_sum_bruteforce([2,7,11,15], 9))  # Output: [0, 1]
# print(two_sum_optimized([2,7,11,15], 9))   # Output: [0, 1]
