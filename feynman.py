n=1
while n!=0:
    n = int(input())
    p=0
    while n>1:
        p=(p+n*n)
        n=(n-1)
    if n!=0:
        print(str(p+1))
