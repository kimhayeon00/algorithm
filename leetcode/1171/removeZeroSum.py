# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        total_lst = {}
        root = ListNode(0,head)
        node = root
        while node:
            total += node.val
            if total in total_lst:
                prev = total_lst[total]
                tmp = prev.next
                tmp_sum = total
                while tmp != node:
                    tmp_sum += tmp.val
                    if tmp_sum in total_lst and total_lst[tmp_sum] == tmp:
                        total_lst.pop(tmp_sum)
                    tmp = tmp.next
                prev.next = node.next
                node = prev
            else:
                total_lst[total] = node
            node = node.next
        return root.next
