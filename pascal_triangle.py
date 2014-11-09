row = int(raw_input("row index: "))
column = int(raw_input("column index: "))

def pascal_triangle(r,c):
	if (r==0 or c==0):
		return 1;
	else:
		valOne = pascal_triangle(r, c-1);
		valTwo = pascal_triangle(r-1, c);
	return valOne + valTwo;

print pascal_triangle(row,column)