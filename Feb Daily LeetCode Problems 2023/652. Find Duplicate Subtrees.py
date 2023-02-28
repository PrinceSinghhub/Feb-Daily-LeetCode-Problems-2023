# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        frequency = {}
        result = []
        self.findDuplicates(root, frequency, result)
        return result

    def findDuplicates(self, node, frequency, result):
        if node is None:
            return "#"

        leftIdentifier = self.findDuplicates(node.left, frequency, result)
        rightIdentifier = self.findDuplicates(node.right, frequency, result)

        identifier = str(node.val) + "," + leftIdentifier + "," + rightIdentifier
        frequency[identifier] = frequency.get(identifier, 0) + 1

        if frequency[identifier] == 2:
            result.append(node)

        return identifier
