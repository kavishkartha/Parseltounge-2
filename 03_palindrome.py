string = input("Enter a cool text which may be a palindrome:\n")

def reverse(s):
    return s[::-1]

def isPalindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False

result =''.join(e for e in string if e.isalnum()).lower()
ans = isPalindrome(result)

if ans == 1:
    print("This is a palindrome.")
else:
    print("This is not a palindrome")
