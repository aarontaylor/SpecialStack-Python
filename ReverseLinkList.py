# Short way to reverse a *linked list* in Python
def reverse_link_list(head):
    # Check if head is null and don't reverse if true
    if (head == None or head.next ==  None):
        return head

    # Recursive call 
    reversed_list = reverse_link_list(head.next)

    head.next.next = head
    head.next = None

    return reversed_list

