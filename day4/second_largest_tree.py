
def find_second_largest(root):

    # Find the second largest item in the binary search tree
    elements=[]
    elements.append(root)
    values=[]
    while(len(elements)>0):
        temp=elements.pop()
        values.append(temp.value)
        if(temp.left is not None):
            elements.append(temp.left)
        if(temp.right is not None):
            elements.append(temp.right)
    
    values=sorted(values)
    if(len(values)==1):
        raise Exception
    if(len(values)>=2):
        return values[len(values)-2]


def find_largest(root):
    if root is None:
        return None
    while(root.right is not None):
        root=root.right
    return root.value

def find_second_largest(root):

    # Find the second largest item in the binary search tree
    parent=root
    child= parent.right if parent.right is not None else None
    
    if(child==None and parent.left is None):
        raise Exception
    elif parent.right is None and parent.left!=None:
        return find_largest(parent.left)
    else:
        while(child.right is not None):
            parent=child
            child=child.right
        if(child.left is not None):
            return find_largest(child.left)
        else:
            return parent.value
