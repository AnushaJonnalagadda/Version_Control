n=int(input("Enter any number:"))
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
if cnt==2:
    print("{} is a prime number:".format(n))
else:
    print("{} is not a prime number:".format(n))
