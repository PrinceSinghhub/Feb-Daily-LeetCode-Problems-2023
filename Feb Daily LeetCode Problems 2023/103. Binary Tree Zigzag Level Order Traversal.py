# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        if root == None:
            return ans

        queue = deque()
        queue.append(root)
        flag = 0

        while len(queue) != 0:

            level = []

            for _ in range(len(queue)):

                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if flag == 0:
                ans.append(level)
                flag = 1
            else:
                ans.append(level[::-1])
                flag = 0
        return ans









