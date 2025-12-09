n= int(input("enter an iteger"))
def fizbuzz(n):
    answer=[]
    for i in range (1,n+1):
        if i%3==0 and i%5==0:
            answer.append("fizzbuzz")
        elif i%3==0:
            answer.append("fizz")
        elif i%5==0:
            answer.append("buzz")
        else:
            answer.append(str(i))
    
    return answer
xxx=(fizbuzz(n))
print (xxx)
            
        
        
        


