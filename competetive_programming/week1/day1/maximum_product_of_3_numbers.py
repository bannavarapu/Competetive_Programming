def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    if(len(list_of_ints)<3):
        raise illegalArgumentException
    else:
        max1=list_of_ints[0]
        max2=list_of_ints[1]
        max3=list_of_ints[2]
        max4=0
        max5=0
        for i in list_of_ints:
            if(i<0):
                if(i<max4):
                    max4=i
                elif(i<max5):
                    max5=i
            if(i>max1):
                max3=max2
                max2=max1
                max1=i
            elif(i>max2):
                max3=max2
                max2=i
            elif(i>max3):
                max3=i
    out = max1*max2*max3 if max1*max2*max3>max1*max5*max4 else max1*max4*max5
    return out
