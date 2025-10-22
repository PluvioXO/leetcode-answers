# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = [] 
        if not root:
            return ans
        def dfs(x, i): 
            print(i)
            nonlocal ans; 
            if not x: 
                return False; 
            if sum(i) == targetSum:
                if x.left == None and x.right == None:
                    ans.append(i)
                    return; 
            x.left != None and dfs(x.left, i+[x.left.val])
            x.right != None and dfs(x.right, i+[x.right.val])
        dfs(root, [root.val])
        return ans; 
            