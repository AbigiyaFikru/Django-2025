valid_sales=[]

with open ("sales.txt" , "r") as file:
    lines=file.readlines()
    
for line in lines:
    line= line.strip()
    try:
        data= int(line)
        valid_sales.append(data)
    except ValueError:
        print(f"invalid entry:{line}")
total_sale= sum(valid_sales)
print(f"Valid sales numbers: {valid_sales}")
print(f"Total sales: {total_sale}")