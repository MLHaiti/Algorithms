from binarySearchTree import BinarySearchTree

# using BST
binary_search_tree = BinarySearchTree()

#        3
#     /      \
#    2        5
#   / \      / \
#  1  2.5   4   6

binary_search_tree.insert(3)
binary_search_tree.insert(5)
binary_search_tree.insert(4)
binary_search_tree.insert(6)
binary_search_tree.insert(2)
binary_search_tree.insert(1)
binary_search_tree.insert(2.5)

# get maximum of our BST
print(f"get maximum of our BST: {binary_search_tree.getMaxValue()}")

# traverse BST in order, like: 1, 2, 2.5, 3, 4, 5, 6
print("traverse BST in order: ")
binary_search_tree.traverse()
