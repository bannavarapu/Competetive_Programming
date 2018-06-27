def is_binary_search_tree(root):

   return is_bst(root,float("+inf"),float("-inf"))

def is_bst(root,maxi,mini):
    if(root is None):
        return True
    if(maxi<root.value or mini>root.value):
        return False
    return is_bst(root.left,root.value,mini-1) and is_bst(root.right,maxi+1,root.value)
