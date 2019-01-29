import math
numberRange = range(3,1001)
primes = []

for testNum in numberRange:
	testRange = range(2, testNum)
	for divisor in testRange:
		if testNum % divisor == 0:
			break
	if not(testNum % divisor == 0):
		primes.append(testNum)

print(primes)
