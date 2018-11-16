# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy, flag = ListNode(0), 0
        head = dummy
        while flag or l1 or l2:
            node = ListNode(flag)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            flag = node.val / 10
            node.val %= 10
            head.next = node
            head = head.next
        return dummy.next


def listToListNode(input):
    numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToInt(node):
    if not node:
        return []
    tmp_list = []
    while node:
        tmp_list.append(node)
        node = node.next
    return tmp_list



def main():
    line = [0]
    l1 = listToListNode(line)
    line = [0,3,5]
    l2 = listToListNode(line)
    ret = Solution().addTwoNumbers(l1, l2)
    out = listNodeToInt(ret)
    print out
    while 1:
        tmp = []
        for i in out:
            tmp.append(i.val)
            if i.next:
                continue
        print(tmp)
        break

if __name__ == '__main__':
    main()
