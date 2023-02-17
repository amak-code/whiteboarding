import re
def is_panagram(string_of_letters):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    set_alphabet = set(alphabet)
    
    str = re.sub(r'[^a-zA-Z]+', '',string_of_letters)

    set_of_letters = set(str.lower())
    if set_alphabet == set_of_letters:
        return True
    
    return False

print(is_panagram("The quick brown fox jumps over the lazy dog."))