#!/usr/bin/env python
# coding: utf-8

# In[230]:


class TreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def addLeftChild(self, left):
        self.left = left
        
    def addRightChild(self, right):
        self.right = right


# In[305]:


a = TreeNode("a")
b = TreeNode("b")
c = TreeNode("c")
d = TreeNode("d")
e = TreeNode("e")
f = TreeNode("f")
g = TreeNode("g")
h = TreeNode("h")
i = TreeNode("i")
a.addLeftChild(b)
a.addRightChild(c)
b.addLeftChild(d)
b.addRightChild(e)
c.addLeftChild(f)
c.addRightChild(g)
d.addLeftChild(h)
d.addRightChild(i)


# In[306]:


def lowestCommonAncestor(root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                global ans
                ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return ans
    


# In[307]:


ans = None
print(lowestCommonAncestor(a,e,i).data)


# In[ ]:





# In[ ]:




