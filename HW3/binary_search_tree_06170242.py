#delete,modify PASS 取用自https://github.com/dustinoy/ohyang/blob/master/HW3/binary_search_tree_06170219.py
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        new_val=TreeNode(val)
        if root is None:   
            root=TreeNode(val)
            return root
            
        if root is not None:
            if root.val <=  new_val.val:
                if root.right is None:
                    root.right=new_val
                    return root.right
                else:
                    return self.insert(root.right,new_val.val)
            else:
                if root.left is None:
                    root.left=new_val
                    return root.left
                else:
                    return self.insert(root.left,new_val.val)
                
    def mini(self, root):
        if root.left is None:
            return root
        else:
            return self.mini(root.left)
                
    def search(self, root, target):
        """
    ## PASS def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        while self.search(root, target) is True:
            if target < root.val:
                return self.delete(root.left,target)
            elif target > root.val:
                return self.delete(root.right,target)
            else:
                if root.left is None:
                    children=root.right
                    root=None
                    return children
                elif root.right is None:
                    children=root.left
                    root=None
                    return children
                elif root.left is None & root.right is None:
                    return root
                children=self.mini(root.right)
                root.val=children.val
                root.right=self.delete(root.right,children.val)
            self.delete(root.val, target)
        else:
            return root
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root.val==target & target is not None:
            return root
        elif root.val>=target:
            return self.search(root.left,target)
        else:
            return self.search(root.right,target)
  
