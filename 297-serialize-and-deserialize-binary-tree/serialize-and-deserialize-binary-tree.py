# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.       
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        data = ""
        level = deque()
        level.appendleft((root, 1))
        while level:
            
            for i in range(len(level)):
                node, index =  level.popleft()
                data += str(index) + " " + str(node.val) + ","
                if node.left:
                    level.append((node.left, 2*index))
                if node.right:
                    level.append((node.right, 2*index + 1))

        print(data)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return []
        nodes = data.split(",")
        nodes_dict = {}
        
        for node in nodes:
            if node != "":
                index, val = node.split(" ")
                nodes_dict[int(index)] = TreeNode(int(val))
              
              
        root = nodes_dict[1]
        for index in nodes_dict:
            node = nodes_dict[index]
            left_child = 2*index
            right_child = 2* index + 1
            if left_child in nodes_dict:
                node.left = nodes_dict[left_child]

            if right_child in nodes_dict:
                node.right = nodes_dict[right_child]
        return  root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))