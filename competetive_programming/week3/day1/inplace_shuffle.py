import random
def shuffle(the_list):

    # Shuffle the input in place
    length = len(the_list)
    for i in range(0,length):
        random_int=random.randrange(1,length)
        if(i!=random_int):
            the_list[i],the_list[random_int]=the_list[random_int],the_list[i]

sample_list = [1, 2]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list
