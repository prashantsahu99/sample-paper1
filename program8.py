s=input()
s=s.upper()
s=set(s)
c=[x for x in s if ord(x) in range(65,92)]
if len(c)==26:
	print("pangram")
else:
	print("not")	
				
	
			
			
