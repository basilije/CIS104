primes = []

for testNum in range(3,1001):
	for divisor in range(2, testNum):
		if testNum % divisor == 0:
			break
	if not testNum % divisor == 0:
		primes.append(testNum)

print(primes)
