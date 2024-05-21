from LinkedList import LinkedList

def merge_sort(linked_list):
    """Sorts a linked list in ascending order
    - Recursively divide the linked list into sub lists containing a single node
    - Repeatedly merge the sub lists to produce sorted sub lists until one remains

    Returns a sorted linked list
    """
    if linked_list.size() == 1:  # Only one element
        return linked_list
    elif linked_list.head is None:  # Empty list
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """Divide the unsorted list at midpoint into sub lists"""
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """Merges two linked lists sorting by data in nodes.
    Returns a new, merged list
    """
    merged = LinkedList()
    merged.add(0)  # Add a fake head that is discarded later
    current = merged.head

    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node

    head = merged.head.next_node  # Discard the fake head
    merged.head = head

    return merged

# Example usage
l = LinkedList()
l.add(10)
l.add(20)
l.add(44)
l.add(2)
l.add(54)

print("Unsorted list:", l)
sorted_linked_list = merge_sort(l)
print("Sorted list:", sorted_linked_list)
