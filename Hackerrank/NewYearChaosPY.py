def minimumBribes(q):
    bribe = 0
    for index in range(len(q)-1,0,-1):
        if q[index] != index+1:
            if q[index-1] == index+1:
                bribe += 1
                q[index-1], q[index] = q[index], q[index-1]
            elif q[index-2] == index+1:
                bribe += 2
                q[index-2], q[index-1], q[index] = q[index-1], q[index], q[index-2]
            else:
                print('Too chaotic')
                return

    print(bribe)





minimumBribes([1,2,3,4,5])


