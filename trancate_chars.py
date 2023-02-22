# Write a function that takes in a string. It should return a string where consecutive repeating characters have been truncated. For example:
# "aaaabbbbbbcccc" => "abc"
# "caaaat" => "cat"

def trancate_chars(list_of_chars):
	if not list_of_chars:
		return list_of_chars

	new_word = ""

	previous = list_of_chars[0]
	
	new_word += previous

	for el in list_of_chars: 		
		temp = el
		if temp != previous:
			new_word += temp
		previous = temp


	return new_word

print(trancate_chars("aaaabbbbbbcccc"))
