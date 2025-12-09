n= input("enter a word")
def checkPalindrome ():
    n=str(n)
    left=0
    right= len(n)-1
    
    while n[left] <n[right]:
        if n[left]!= n[right]:
            return False
        left+=1
        right-=1
    return True

if checkPalindrome(n):
    print(f"{n} this word is palindrome")
else:
    print(f"{n}this word is not palindrome") 