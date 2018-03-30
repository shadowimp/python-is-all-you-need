#-*-coding:utf-8-*-
class ListNode:
	def __init__(self,x):
		self.val = x 
		self.next = None 

# class Solution: 
# 	def addTwoNumbers(self,l1,l2):
# 		count = 0
# 		num1 = num2 =  0
# 		while l1 is not None: 
# 			num1 += l1.val * (10**count)
# 			l1 = l1.next 
# 			count +=1 

# 		count = 0 
# 		while l2 is not None:
# 			num2 += l2.val * (10**count)
# 			l2 = l2.next 
# 			count +=1

# 		l3 = LinkList(0)
# 		l = l3 
# 		s = num1 + num2

# 		while s>0 :
# 			s,l3.val = divmod(s,10)
# 			if s > 0:
# 				l3.next = LinkList(0)
# 				l3 = l3.next  

# 		return l,l.val,l.next.val,l.next.next.val




		# nums1 = []
		# nums2 = []
		# while l1.next != None :
		# 	nums1.append(l1.val)
		# 	l1 = l1.next 
		# nums1.append(l1.val)
		
		# while l2.next != None:
		# 	nums2.append(l2.val)
		# 	l2 = l2.next 
		# nums2.append(l2.val)

		# n1 = 0 
		# flag1 = 1
		# for x1 in nums1: 
		# 	n1 += x1*flag1
		# 	flag1 *= 10 

		# n2 = 0 
		# flag2 = 1 
		# for x2 in nums2: 
		# 	n2 += x2*flag2
		# 	flag2 *= 10
		
		# s = str(n1 + n2)[::-1] 

		# return s

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0    # 进位符
        root = n = ListNode(0)
        while l1 or l2 or carry:
        # 只要 l1 l2 都不为空才进行操作，否则直接返回 0
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next   # 这步一定要仔细理解




l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)


l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

S1 = Solution() 
print(S1.addTwoNumbers(l1,l2))



