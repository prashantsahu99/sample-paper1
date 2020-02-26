l=list(int(x) for x in input().split())
n=len(l)
c=[]
z=0
for i in l:
	if i!=0:
		c.append(i)
	else:
		z+=1
for i in range(0,z):
	c.append(0)
print(c)				
