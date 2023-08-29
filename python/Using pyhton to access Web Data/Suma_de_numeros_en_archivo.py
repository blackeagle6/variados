import re
with open("./Sumaarchivo.txt","r") as file:
    file_content = file.read()
    file_numbers = re.findall(r'[0-9]+',file_content)
total_sum = sum(int(num) for num in file_numbers)
print(total_sum)
