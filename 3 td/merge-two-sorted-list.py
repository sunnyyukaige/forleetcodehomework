class Solution:
    def mergeTwoLists(self, l1, l2):
        phead = ListNode(-1)
        p = phead
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next            
            p = p.next
        p.next = l1 if l1 is not None else l2
        return phead.next


    def mergeTwoListsP1(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
