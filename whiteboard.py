# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters 
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False


def solution(word):
    # set the word to be all the same case 
    word = word.lower()
    # find a way to reverse the word
    reversed_word = word[::-1]
    # is the reversed word the same as the original word
    if reversed_word == word:
        # if so, then we want to return True because it is a palindrome
        return True
    # if not, return False because that is not a palindrome
    else:
        return False
