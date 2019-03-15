#-*-coding:utf-8-*-

'''
链表成对调换。 1->2->3->4 调换成 2->1->4->3
输入： 链表头结点
输出： 调换后的链表头节点

'''
class ListNode: 
	def __init__(self,val):
		self.val = val 
		self.next = None 

class Solution: 
	def swap(self,head): 
		if head != None and head.next != None : #如果有一对以上的节点继续操作
			next = head.next 
			head.next = self.swap(next.next) #重新建立除第一个节点外其他节点的逻辑
			next.next = head # 调换两个节点的关系
			return next #返回第二个节点
		return head # 链表只有一个元素或者没有元素，返回头结点本身

#建立一个链表
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d 

#执行函数
s1 = Solution() 
new_head = s1.swap(a)

#遍历链表的值
while new_head != None : 
	print(new_head.val)
	new_head = new_head.next

