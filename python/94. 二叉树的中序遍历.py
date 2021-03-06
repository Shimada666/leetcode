# -*- coding: utf-8 -*-
"""
    :author: Shimada666
    :url: https://github.com/shimada666
    :copyright: © 2020 Shimada666 <Shimada666@foxmail.com>
    :license: MIT, see LICENSE for more details.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """颜色标记法"""

    # 简单版本
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    '''层次遍历'''
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     WHITE, GRAY = 0, 1
    #     stack = []
    #     init_level = 0
    #     stack.append((root, WHITE, init_level))
    #     result = []
    #     while stack:
    #         node, color, level = stack.pop()
    #         if node:
    #             if color == WHITE:
    #                 stack.append((node.right, WHITE, level+1))
    #                 stack.append((node.left, WHITE, level+1))
    #                 stack.append((node, GRAY, level))
    #             else:
    #                 if len(result) == level: result.append([])
    #                 result[level].append(node.val)
    #     return result

    '''无需额外空间的优化版本'''
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     stack, rst = [root], []
    #     while stack:
    #         i = stack.pop()
    #         if isinstance(i, TreeNode):
    #             stack.extend([i.right, i.val, i.left])
    #         elif isinstance(i, int):
    #             rst.append(i)
    #     return rst
