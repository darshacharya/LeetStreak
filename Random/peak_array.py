n=3
arr=[]
while n!=1:
    if n%2==0:
        n=n/2
        arr.append(n)
    elif n%2==1:
        n=(n*3)+1
        arr.append(n)
print(arr)