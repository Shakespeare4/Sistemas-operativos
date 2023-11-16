import sys
D=sys.argv[1]
d=sys.argv[2]
D=int(D)
d=int(d)
dc=D
c=1 
if D==0:
	print("error")
while dc>=d:
	dc=dc-d
	c=c+1
print ('Coeficiente',(c))

print ('Resto',(dc))
