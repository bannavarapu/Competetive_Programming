def is_valid(code):

    # Determine if the input code is valid
    a=[]
    for i in code:
        if(i is '(' or i is '{' or i is '['):
            a.append(i)
        if(i==')' or i=='}' or i==']'):
            if(a==[]):
                return False
            x=a.pop()
            if(i==')' and x!='('):
                return False
            elif(i=='}' and x!='{'):
                return False
            elif(i==']' and x!='['):
                return False
    if(a==[]):
        return True
    return False
