sumOfBoth=0
sumOfFour=0
sumOfEight=0
multiple1 =1
for number in range(5):
	count = 4
	multiple1 *= count
	sumOfFour += multiple1                  
	
	
multiple2 =1
for number in range(5):
	count = 8
	multiple2 *= count
	sumOfEight += multiple2
	
sumOfBoth= sumOfFour  +	sumOfEight
print(sumOfBoth)
