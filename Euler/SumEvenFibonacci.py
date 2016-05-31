def getEvenSum(N):
    if N<=1: return 0
    elif N==2: return 2
    n1,n2=1,2
    prev_even=0
    res=0
    while n2<=N:
        if n1%2==0 and n1!=prev_even: 
            res+=n1
            prev_even=n1
        if n2%2==0 and n2!=prev_even: 
            res+=n2
            prev_even=n2
        tmp=n2
        n2=n1+n2
        n1=tmp
    return res

N=100
print getEvenSum(N)