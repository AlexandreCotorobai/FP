def closerToTarget(x,y,target):
    l=target-y
    m=target-x
    if l<0:
        l=-l
    if m<0:
        m=-m
    if l<m:
        return y
    elif m<l:
        return x
    else:
        if x<y:
            return x
        else:
            return y

print(closerToTarget(5,-1,-5)) 
        
