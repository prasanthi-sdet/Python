def calculate_sum(numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum

numList = [55, 90, 20, 60, 30]
result = calculate_sum(numList)
print("Sum: " + str(result))