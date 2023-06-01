import random
#switch first and last elements in a string

def switch_elmts(input_string):
    
    lst = list(input_string)
    temp = lst[0]
    last_el = lst[-1]
    lst[0] = last_el
    lst[-1] = temp
    
    return str(lst)
    
#print(switch_elmts("blah"))

#########################################
#check if the string is palindrome and return true or false

def is_palindrome(input_string):
    #is it only letters ot also could be differnet characters?

    """
    we need to start from the beginning and from the end and got toward 
    the middle of the string. if the characters don't match - return false, 
    othewise return true
    """    
    
    for i in range(len(input_string)//2):
       
        if input_string[i] != input_string[len(input_string) -i - 1]:
            return False
    
    
    return True

#print(is_palindrome("futuf"))    

#################################################
#Given two lists. concatenate them (that is, combine them into a single list).

def concat_lists(list1, list2):
    
    new_list = list1 + list2
    
    return new_list

#print(concat_lists([], [3,4]))


####################################
#Given an integer n, return a list containing n unique random numbers between 1-10, inclusive. 
# (That is, do not repeat any numbers in the returned list.)

def lucky_nums(num):
    
    nums = set()
    
    """
    we need to use random to get numbers and then check 
    if this number is already is in the nums or not.
    """
    
    while len(nums)< num:
    
        r = random.randint(1,10)
        
        if r not in nums:
            nums.add(r)
            
    return nums

#print(lucky_nums(4))

################################
#Given a list of numbers, return the smallest and the largest number.
#For an empty list, it should return None as both smallest and largest
#Make sure it works with a list of one item, which is both smallest and largest

def find_range(range_list):
    
    min_num = None
    max_num = None
    
    result = ()
    
    if not range_list:
        return (min_num, max_num)
    
    elif len(range_list) == 1:
        
        return(range_list[0], range_list[0])
    else:
        min_num = range_list[0]
        max_num = range_list[0]
        for el in range_list:
           if el < min_num:
               min_num = el
           if el > max_num:
               max_num = el
               
        return (min_num, max_num)
    
    
#print(find_range([]))
               

######################################                
#reverse the string

def reverse_string(input_string):
    
    # reversed_string = ""
    # for i in range(len(input_string)):
    #     reversed_string += input_string[len(input_string) -i - 1]
        
    # return reversed_string
        
    reversed_list = list(input_string)
    for i in range(len(reversed_list)//2):
        temp = reversed_list[i]
        reversed_list[i] = reversed_list[len(reversed_list)- i - 1]
        reversed_list[len(reversed_list)- i - 1] = temp
        
    return reversed_list
    
    
    #return ''.join(reversed(input_string))
    #return input_string[::-1]

#print(reverse_string("abrakadabra"))
    

########################
#Given a phrase, print (not return) the word count in ascending order

def word_count(input_string):
    
    word_dict = {}
    
    input_list = input_string.split(" ")
    
    for word in input_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
            
    counts =  word_dict.items()
    
    for w,count in counts:
        print("%s: %s" %(w, count))
        
    
        
#word_count("berry cherry cherry cherry berry apple")
    
    
    
################################
#Determine if the given word is a re-scrambling of a palindrome.

def is_anagram_palindrome(string_input):
    
    dict_letters = {}
    
    for ch in string_input:
        if ch not in dict_letters:
            dict_letters[ch] = 1
        else:
            dict_letters[ch] += 1
    
    count_odds = 0      
    for num in dict_letters.values():
        if len(string_input)%2 == 0:
            if num%2 != 0:
                return False
        else:
            if num%2 != 0:
                count_odds += 1
    
    return count_odds <= 1


#####################
#valid parentheses

def is_valid_parethenses(string_input):
    
    left_par = []
    
    for par in string_input:
        if par == ")" and not left_par:
            return False
        if par == "(":
            left_par.append(par)
        else:
            left_par.pop()
    
    return len(left_par) == 0

#print(is_valid_parethenses(")((()))("))


#######################################
#sum to zero 

def sum_to_zero(list_input):
    
    set_of_input = set(list_input)
    
    for num in list_input:
        if -num in set_of_input:
            return True
        

    return False

print(sum_to_zero([1,2,3,4]))
    