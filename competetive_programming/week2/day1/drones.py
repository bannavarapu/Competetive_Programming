def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    a=delivery_ids[0]
    for i in range(1,len(delivery_ids)):
        a = a ^ delivery_ids[i]
    return a
