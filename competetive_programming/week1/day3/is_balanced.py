def is_balanced(root):
    if root is None:
        return True
    else:
        depths=[]
        nodes=[]
        nodes.append((root,0))
        while len(nodes):
            current_node,depth=nodes.pop()
            if(current_node.left is None and current_node.right is None):
                if depth not in depths:
                    depths.append(depth)
                if(len(depths)>2):
                    return False
                if(len(depths)==2 and abs(depths[0]-depths[1])>1):
                    return False
            if(current_node.left is not None):
                nodes.append((current_node.left,depth+1))
            if(current_node.right is not None):
                nodes.append((current_node.right,depth+1))
