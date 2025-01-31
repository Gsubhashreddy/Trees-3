# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

 #T(N)=O(N)
#S(N)=O(1)
class Solution:
    gl=[]   #Global List
    def helper(self,root,targetSum,tempSum,tempArr):
        if root==None:  
            return
        if root.left==None and root.right==None: #If Leaf Node Check the Sum==target
            tempSum+=root.val
            if tempSum==targetSum:
                tempArr.append(root.val)
                self.gl.append(tempArr[:])
            else:
                tempArr.append(root.val)
                
        else:
            tempSum+=root.val
            tempArr.append(root.val)
        self.helper(root.left,targetSum,tempSum,tempArr)    #Left Tree
        
        self.helper(root.right,targetSum,tempSum,tempArr)   #Right Tree
       
        tempArr.pop()       #Pop Element After Done
        
                
                
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.gl=[]
        self.helper(root,targetSum,0,[])
        return self.gl
        
        
            
            
        