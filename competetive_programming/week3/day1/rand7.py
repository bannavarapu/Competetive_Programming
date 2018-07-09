import random


def rand5():
    return random.randint(1, 5)


def rand7():

    # Implement rand7() using rand5()
    x=5*rand5()+rand5()-5
    if x<22:
        return x%7+1
    else:
        return rand7()


print 'Rolling 7-sided die...'
print rand7()
