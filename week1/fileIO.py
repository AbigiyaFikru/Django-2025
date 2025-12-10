with open("abigiya.txt" , "w") as file:
    file.write("hello world")
    
with open("abigiya.txt" , "r") as file:
    text= file.read()
    print(text)
    
    
try:
    with open("test.txt") as file:
        content=file.read()
        print (f"welcome {content}")
               
except Exception:
    with open ("test.txt", "w") as file:
        file.write("guest")
        

    
    