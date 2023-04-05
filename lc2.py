# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_sum_node = ListNode()
        cur_l1_node = l1
        cur_l2_node = l2
        carry = 0

        if cur_l1_node.val + cur_l2_node.val >= 10:
            carry = 1
            cur_sum_node.val = cur_l1_node.val + cur_l2_node.val - 10
            cur_sum_node.next = ListNode()
            start_node = cur_sum_node
            if cur_l1_node.next is None and cur_l2_node.next is None:
                cur_sum_node.next.val = 1
                return start_node
        
        else:
            cur_sum_node.val = cur_l1_node.val + cur_l2_node.val
            if cur_l1_node.next is None and cur_l2_node.next is None:
                return cur_sum_node

            cur_sum_node.next = ListNode()
            start_node = cur_sum_node

        


        cur_sum_node = cur_sum_node.next
        cur_l1_node = cur_l1_node.next
        cur_l2_node = cur_l2_node.next

        while True:
            if cur_l1_node is not None and cur_l2_node is not None:
                val = cur_l1_node.val + cur_l2_node.val + carry
                if val >= 10:
                    cur_sum_node.val = val - 10
                    carry = 1
                else:
                    cur_sum_node.val = val
                    carry = 0
                cur_l1_node = cur_l1_node.next
                cur_l2_node = cur_l2_node.next

            elif cur_l1_node is not None and cur_l2_node is None:
                val = cur_l1_node.val + carry

                if val >= 10:
                    cur_sum_node.val = val - 10
                    carry = 1
                else:
                    cur_sum_node.val = val
                    carry = 0

                cur_l1_node = cur_l1_node.next

            elif cur_l1_node is None and cur_l2_node is not None:
                val = cur_l2_node.val + carry

                if val >= 10:
                    cur_sum_node.val = val - 10
                    carry = 1
                else:
                    cur_sum_node.val = val
                    carry = 0

                cur_l2_node = cur_l2_node.next


            if cur_l1_node is None and cur_l2_node is None:
                if carry == 1:
                    cur_sum_node.next = ListNode(val=1)
                return start_node
            
            cur_sum_node.next = ListNode()
            cur_sum_node = cur_sum_node.next