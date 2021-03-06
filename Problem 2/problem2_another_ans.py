# Stealed from Project Euler thread 2 by Begoner
# Just call the function while using it
# Explaination first
'''
This may be a small improvement.  The Fibonacci series is:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

Now, replacing an odd number with O and an even with E, we get:

O, O, E, O, O, E, O, O, E, O, O, E, O, O, E...

And so each third number is even.  We don't need to calculate the odd numbers.  Starting from an two odd terms x, y, the series is:

x, y, x + y, x + 2y, 2x + 3y, 3x + 5y
'''
def calcE():
	x,y = 1,1
	sum = 0
	while (sum < 4000000):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	print sum
