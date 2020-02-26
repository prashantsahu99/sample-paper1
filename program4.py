l=list(int(x) for x in input().split(','))
c=50
h=30
d=[]
for i in l:
	q=((2*c*i)//h)**0.5
	d.append(q)
n=len(d)
for i in range(0,n):
	print(round(d[i]),end='')
	if i!=n-1:
		print(",",end='')	
