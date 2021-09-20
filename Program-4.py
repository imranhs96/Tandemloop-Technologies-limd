list1=list(map(int,input().split()))
m={}
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
j=0
for i in list1:
    if i%1 ==0:
        a+=1

    if i%2 ==0:
        b+=1

    if i%3 ==0:
        c+=1
        
    if i%4 ==0:
        d+=1
        
    if i%5 ==0:
        e+=1
        
    if i%6 ==0:
        f+=1
        
    if i%7 ==0:
        g+=1
        
    if i%8 ==0:
        h+=1
        
    if i%9 ==0:
        j+=1
        
    m[1]=a
    m[2]=b
    m[3]=c
    m[4]=d
    m[5]=e
    m[6]=f
    m[7]=g
    m[8]=h
    m[9]=j
print(m)
    
