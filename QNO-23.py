class Solution(object):
    def mergeKLists(self, lists):
        self.node = []
        dummy = head = ListNode(0)

        for l in lists:
            while l:
                self.node.append(l.val)
                l = l.next
        for x in sorted(self.node):
            dummy.next = ListNode(x)
            dummy = dummy.next
        return head.next
    