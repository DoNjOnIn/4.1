n=int(input('N='))
k=1
s=0
#1
while k<=n:
    s+=1/(2*k+1)**2
    k+=1
print(s)
#2
k=1
s=0
while 1>0:
    s += 1 / (2 * k + 1) ** 2
    k+=1
    if k>n:
        break
print(s)
#3
s=0
for i in range(1,n+1):
    s+=1/(2*i+1)**2
print(s)
#4
s=0
for i in range(n,0,-1):
    s+=1/(2*i+1)**2
print(s)