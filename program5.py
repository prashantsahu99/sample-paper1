s=input()
sub=input("enter substring")
n=len(s)
c=0
for i in range(0,n-len(sub)+1):
	if s[i:i+3]==sub:
		c=c+1
print(c)		
