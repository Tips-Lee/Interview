class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = '', ''
        while l1 != None:
            s1 = s1 + str(l1.val)
            l1 = l1.next

        while l2 != None:
            s2 = s2 + str(l2.val)
            l2 = l2.next

        num = int(''.join(reversed(s1))) + int(''.join(reversed(s2)))

        head = p = ListNode(num % 10)
        num //= 10
        while num != 0:
            n = num % 10
            num //= 10
            node = ListNode(n)
            p.next = node
            p = p.next
        return head


l1 = [0, 8, 6, 5, 6, 8, 3, 5, 7]
n1 = p = ListNode(l1[0])
for i in l1[1:]:
    node = ListNode(i)
    p.next = node
    p = p.next

l2 = [6, 7, 8, 0, 8, 5, 8, 9, 7]
n2 = p = ListNode(l2[0])
for i in l2[1:]:
    node = ListNode(i)
    p.next = node
    p = p.next

s = Solution()
ans = s.addTwoNumbers(n1, n2)
print(ans)
