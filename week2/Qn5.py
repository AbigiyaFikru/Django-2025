data= ["200" ,"450","abc" , "700"]
with open ("sales.txt" , "w") as file:
    for item in data:
        file.write(item + "\n")

with open ("sales.txt" , "r") as file:
    lines=file.readlines()
    
for line in lines:
    line= line.strip()
    try:
        data= int(line)
        print(f"sales number: {data}")
    except ValueError:
        print(f"invalid entry:{line}")
    

         
   