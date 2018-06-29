def merge_ranges(meetings):

    # Merge meeting ranges
    startlist=[]
    endlist=[]
    for i in meetings:
        starttime,endtime=i
        startlist.append(starttime)
        endlist.append(endtime)
    
    startlist=sorted(startlist)
    endlist=sorted(endlist)
    toreturn=[]
    st=startlist[0]
    et=endlist[0]
    for i in range(1,len(startlist)):
        if(startlist[i]>endlist[i-1]):
            toreturn.append((st,endlist[i-1]))
            st=startlist[i]
    toreturn.append((st,endlist[len(endlist)-1]))
    print(startlist)
    print(endlist)
    print(toreturn)

    return toreturn

