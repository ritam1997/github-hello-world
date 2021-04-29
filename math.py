#Bug456 comment before add function
def add(x, y):
	return x + y
def sub(x, y):
	if(x>y):
		return x - y
	else:
		return y - x
def mul(x, y):
	return x * y
def div(x, y):
	if(y!=0):
		return x / y # Bug789 EDIT
	else:
		return 'Nan'
def fact(x):
	if(x==0): #Base condition for recursion
		return 1
	else
		return x * fact(x-1)
def rev(x): #reverse method
	return str(x)[::-1]
def fact(x):
	if(x==0)
		return 1
	return x*fact(x-1)
def pow(x,y):
	if(x==0 and y==0):
		return 'Nan'
	return x**y
