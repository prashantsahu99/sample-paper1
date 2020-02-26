l=list(int(x) for x in input().split(','))
c=[x for x in range(1,l[len(l)-1]) if x not in l]
print(l)
print(c)


