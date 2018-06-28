def contains(ordered_list, number):

    # Check if an integer is present in the list
    low=0
    high=len(ordered_list)-1

    while(low<=high):
        middle=(low+high)/2
        if(ordered_list[middle]==number):
            return True
        elif(number>ordered_list[middle]):
            low=middle+1
        else:
            high=middle-1
    return False

