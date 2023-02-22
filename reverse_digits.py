# Write a function that takes in a number. Return a number with the digits of the given number, but in reverse order. For example:
# 123 => 321


def reverse_digits(num):
	
	num_string = str(num)

	reverse_num_string = ""

	for i in range(len(num_string)):
		
		reverse_num_string += num_string[-i - 1]


	return int(reverse_num_string)



#  another solution when you don't convert int to a string

def reverse_digits2(num):
	reverse = 0
	while num != 0:
		reverse = reverse* 10 + num % 10
		num = num // 10
	return reverse


print(reverse_digits2(123))
print(reverse_digits(123))