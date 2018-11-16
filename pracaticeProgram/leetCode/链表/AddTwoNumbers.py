# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_node = None
        to_add = 0
        flag_node = ListNode
        while 1:
            if l1.val == -1:
                l1.val = 0
            if l2.val == -1:
                l2.val = 0

            if l1.val == 0 and l2.val == 0 and l1.next == None and l2.next == None:
                break
            else:
                to_sum = (l1.val + l2.val + to_add) % 10
                to_add = (l1.val + l2.val + to_add) / 10
                tmp_node = ListNode(to_sum)
                if result_node == None:
                    result_node = tmp_node
                    flag_node = result_node
                else:
                    flag_node.next = tmp_node
                    flag_node = flag_node.next

            if l1.next != None:
                l1 = l1.next
            else:
                l1.val = -1

            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = -1
        return result_node


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
        tmp_list.append(node.val)
        node = node.next
    return tmp_list



def main():
    line = [2,3,4]
    l1 = listToListNode(line)
    line = [3,4,6]
    l2 = listToListNode(line)
    ret = Solution().addTwoNumbers(l1, l2)
    out = listNodeToInt(ret)
    print out

if __name__ == '__main__':
    main()