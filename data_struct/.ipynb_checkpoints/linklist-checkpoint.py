#-*-coding:utf-8-*-

#单向链表
#定义节点 每个节点包括两部分，数值域和指针域
class Node: 
	def __init__(self,val): 
		self.val = val 
		self.next = None 

#定义链表 方法包括：遍历链表，判断链表是否为空，反转链表，头插法和尾插法 。
class LinkList: 
	#建立链表时初始化头结点
	def __init__(self):
		self.head = None

	#判断链表是否为空da
	def is_empty(self):
		if self.head is None:
			return True 
		else : 
			return False 

	#遍历链表
	def traversal(self):
		temp = self.head
		while temp != None:
			print(temp.val)
			temp = temp.next 

	#尾插法
	def insert_tail(self,item):
		if self.head == None :
			self.head = Node(item)
		else:
			temp = self.head 
			while temp.next != None: 
				temp = temp.next 
			temp.next =  Node(item)

	#头插法
	def insert_head(self,item):  
		if self.head == None : 
			self.head = Node(item)
		else:
			temp = self.head 
			self.head = Node(item) 
			self.head.next = temp


	#在尾部删除元素
	def delete_tail(self):
		if self.head == None : 
			return -1 
		elif self.head.next == None:
			data = self.head.val
			self.head = None
			return data
		else:
			temp = self.head
			while(temp.next.next != None): 
				temp = temp.next
			data = temp.next.val
			temp.next = None 
		return data
 

	#在头部删除元素
	def delete_head(self):
		if self.head == None: 
			return -1 
		elif self.head.next == None:
			data = self.head.val
			self.head = None 
			return data
		else:
			temp = self.head
			self.head = self.head.next
		return temp.val 


n = Node(2)
print(n.val,n.next)
l = LinkList()
print(l.is_empty())
l.insert_tail(2)
print(l.is_empty())
l.traversal()
print("*"*30)
l.insert_tail(4)
l.insert_tail(9)
l.traversal()
print("*"*30)

l.insert_head(78)
l.insert_head(3)
l.traversal()

print("*"*30)
l.delete_tail()
l.traversal()

print("*"*30)
l.delete_head()
l.traversal()


