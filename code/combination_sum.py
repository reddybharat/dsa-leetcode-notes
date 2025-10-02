from typing import List
from itertools import combinations_with_replacement, product

def combination_sum_bruteforce(candidates: List[int], target: int) -> List[List[int]]:
    """
    Alternative brute force approach using recursive generation.
    Generates all possible combinations recursively.
    
    Args:
        candidates: List of distinct integers
        target: Target sum to achieve
        
    Returns:
        List of all unique combinations that sum to target
    """
    result = []
    
    def generate_combinations(current_combo, remaining_target, start_idx):
        """
        Generate all possible combinations recursively.
        
        Args:
            current_combo: Current combination being built
            remaining_target: Remaining sum to achieve
            start_idx: Starting index to avoid duplicates
        """
        if remaining_target == 0:
            result.append(current_combo[:])
            return
        
        if remaining_target < 0:
            return
        
        # Try each candidate starting from start_idx
        for i in range(start_idx, len(candidates)):
            current_combo.append(candidates[i])
            generate_combinations(current_combo, remaining_target - candidates[i], i)
            current_combo.pop()
    
    generate_combinations([], target, 0)
    return result

def combination_sum_backtracking(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations using backtracking (optimized approach).
    The same number may be chosen from candidates an unlimited number of times.
    
    Args:
        candidates: List of distinct integers
        target: Target sum to achieve
        
    Returns:
        List of all unique combinations that sum to target
    """
    res = []

    def make_combinations(idx, comb, total):
        """
        Backtracking function to find all valid combinations.
        
        Args:
            idx: Current index in candidates array
            comb: Current combination being built
            total: Current sum of the combination
        """
        # Base case: found a valid combination
        if total == target:
            res.append(comb[:])  # Make a copy of the combination
            return
        
        # Base case: invalid path (sum exceeded or no more candidates)
        if total > target or idx >= len(candidates):
            return

        # Choice 1: Include current candidate (can reuse same candidate)
        comb.append(candidates[idx])
        make_combinations(idx, comb, total + candidates[idx])
        comb.pop()  # Backtrack: remove the last element
        
        # Choice 2: Skip current candidate (move to next)
        make_combinations(idx + 1, comb, total)

    make_combinations(0, [], 0)
    return res

# Example usage and test cases
if __name__ == "__main__":
    # Test case 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    
    print("=== Test Case 1 ===")
    print(f"Candidates: {candidates1}, Target: {target1}")
    
    result_backtrack = combination_sum_backtracking(candidates1, target1)
    print(f"Backtracking Result: {result_backtrack}")
    
    result_bruteforce = combination_sum_bruteforce(candidates1, target1)
    print(f"Brute Force Result: {result_bruteforce}")

    # Expected: [[2, 2, 3], [7]]
    
    print()
    
    # Test case 2
    candidates2 = [2, 3, 5]
    target2 = 8
    
    print("=== Test Case 2 ===")
    print(f"Candidates: {candidates2}, Target: {target2}")
    
    result_backtrack = combination_sum_backtracking(candidates2, target2)
    print(f"Backtracking Result: {result_backtrack}")
    
    result_bruteforce = combination_sum_bruteforce(candidates2, target2)
    print(f"Brute Force Result: {result_bruteforce}")

    # Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    
    print()
    
    # Test case 3
    candidates3 = [2]
    target3 = 1
    
    print("=== Test Case 3 ===")
    print(f"Candidates: {candidates3}, Target: {target3}")
    
    result_backtrack = combination_sum_backtracking(candidates3, target3)
    print(f"Backtracking Result: {result_backtrack}")
    
    result_bruteforce = combination_sum_bruteforce(candidates3, target3)
    print(f"Brute Force Result: {result_bruteforce}")
    
    # Expected: []
