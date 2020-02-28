word = input().strip()  # Getting word as input from the user.

if word[::-1] == word:
    print("{} is a Palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))
