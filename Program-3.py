n=int(input('Enter The Number   :'))
j=1
if n%2 ==0:
    for i in range(1,n):
        print(j,end=' ')
        j+=2
else:
    for i in range(n+1//2):
        print(j,end=' ')
        j+=2
