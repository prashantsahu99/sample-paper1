l=list(int(x) for x in input().split(','))
c=[]
for i in l:
	f=1
	for j in range(1,i+1):
		f=f*j
	c.append(f)
print(c)		
