# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_recursive(head):
    """
    Recursive approach to reverse a linked list.
    Time: O(n), Space: O(n) due to recursion stack
    Most complex due to recursion overhead and stack space usage
    """
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head


def reverse_list_iterative(head):
    """
    Iterative approach to reverse a linked list.
    Time: O(n), Space: O(1)
    Most efficient approach with optimal space complexity
    """
    node = None
    
    while head:
        temp = head.next
        head.next = node
        node = head
        head = temp
        
    return node


# Example usage and test cases
def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: [1,2,3,4,5]
    test1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverse_list_recursive(test1)
    print("Recursive - Input: [1,2,3,4,5], Output:", linked_list_to_list(reversed1))
    
    # Test case 2: [1,2]
    test2 = create_linked_list([1, 2])
    reversed2 = reverse_list_recursive(test2)
    print("Recursive - Input: [1,2], Output:", linked_list_to_list(reversed2))
    
    # Test case 3: []
    test3 = create_linked_list([])
    reversed3 = reverse_list_recursive(test3)
    print("Recursive - Input: [], Output:", linked_list_to_list(reversed3))
    
    # Test iterative approach
    test4 = create_linked_list([1, 2, 3, 4, 5])
    reversed4 = reverse_list_iterative(test4)
    print("Iterative - Input: [1,2,3,4,5], Output:", linked_list_to_list(reversed4))
