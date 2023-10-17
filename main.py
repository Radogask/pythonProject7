#№21-667
#Вариант 0
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    count = [0]
    result = [0]
    inorder(root, count, k, result)
    return result[0]

def inorder(node, count, k, result):
    if node is None:
        return

    inorder(node.left, count, k, result)

    count[0] += 1
    if count[0] == k:
        result[0] = node.val
        return

    inorder(node.right, count, k, result)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

k = 4
result = kth_smallest(root, k)
print(f"{k}-й наименьший элемент: {result}")