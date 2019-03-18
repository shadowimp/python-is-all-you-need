def climb_stairs(n):
	if n  == 1 :
		return 1
	if n == 2 :
		return 2
	steps = [0 for i in range(n)]
	steps[0],steps[1] = (1,2)
	for i in range(2,n):
		steps[i] = steps[i-1] + steps[i-2]

	return steps[n-1]

print(climb_stairs(10))
