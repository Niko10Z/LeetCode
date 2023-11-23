# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list(lst):
    cur = head = None
    for el in lst:
        if cur is None:
            head = cur = ListNode(el)
        else:
            cur.next = ListNode(el)
            cur = cur.next
    return head


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if list1:
        cur = list1
    else:
        cur = list2
        return cur
    if not list2:
        return cur
    if list2.val < cur.val:
        cur = list2
        second = list1
    else:
        second = list2
    head = cur
    pre = cur
    cur = cur.next
    while cur:
        if not second:
            break
        if not cur:
            pre.next = second
            break
        if cur.val > second.val:
            print(f'{cur.val} > {second.val}')
            pre.next = second
            second = second.next
            pre = pre.next
            pre.next = cur
        else:
            pre = cur
            cur = cur.next
    if second:
        pre.next = second
    return head


# res = mergeTwoLists(make_list([-10,-9,-6,-4,1,9,9]),
#                     make_list([-5,-3,0,7,8,8]))
res = mergeTwoLists(make_list([1,2,4]),
                    make_list([1,3,5]))
while res:
    print(res.val)
    res = res.next
