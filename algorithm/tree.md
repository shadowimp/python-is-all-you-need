### 定义树

```python
class TreeNode:
  def __init__(self, val=0, left=None,right=None):
    self.val = val 
    self.left = left
    self.right = right 



```




### 二叉树中序遍历  in-order 

递归：

如果当前节点有值： 递归遍历左子树 + node.val  + 递归遍历右子树



非递归:

建立stack ， 遍历根节点， 

if 有left node ， 则将left node入栈， 

直到left node is None ， 将栈顶的元素pop ， 得到value

将node 的right入栈。 以此类推。。 

```python
class TreeNode:
  def __init__(self, val=0, left=None , right=None):
    self.val = val
    self.left = left 
    self.right = right 
    
# 递归
def inorder_traversal(root) -> list[int]:
  nums = []
  if not root:
    return []
  nums.extend(inorder_traversal(root.left))
  nums.append(root.val)
  nums.extend(inorder_traversal(root.right))
  return nums 
 	
  

#非递归
def inorder_traversal(root) -> list[int]:
  # input: root node , output :list 
  if not root:
    return []
  nums = []
  stack = []
  now_node = root 
  while now_node or stack :
    if now_node is not None:
      stack.append(now_node)
      now_node = now_node.left
    else:
      top_node = stack.pop()
      nums.append(top_node.val)
      now_node = top_node.right 
  return nums 
      
  

```

