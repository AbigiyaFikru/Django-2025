with open ("log.txt" , "w") as file:
    file.write("User logged in")
    
with open("log.txt" , "r") as file:
    text=file.read()
    print(text)
  