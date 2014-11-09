num = 1

while num < 101:
	if num % 3 == 0 and num % 5 == 0:
		print "fizzbuzz"
		num += 1
	elif num % 3 == 0:
		print "fizz"
		num += 1
	elif num % 5 == 0:
		print "buzz"
		num += 1
	else:
		print num
		num +=1

