def fib(n):

    # Compute the nth Fibonacci number
    if(n<0):
        raise Exception
    if(n==0):
        return 0
    elif(n==1):
        return 1
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return c
    # result=[]
    # result.append(0)
    # result.append(1)
    # for i in range (2,n+1):
    #     result.append(result[i-1]+result[i-2])

    # return result[n]
