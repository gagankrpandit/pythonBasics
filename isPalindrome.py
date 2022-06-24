# Python program to check whether a string is palindrome or not

str_ = input('Enter string: ')
text = str_.lower()

rev_text = text[::-1]

if text == rev_text:
    print('string is palindrome')
else:
    print('not palindrome')
