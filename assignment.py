import re
f = open("regex_test.txt")
data = f.readlines()
    
pattern = re.compile("([A-Z][a-z]+) ([A-Z]*)")

for x in data:
    match = pattern.match(x)
    
    if match:
        print(x)
    else:
        print("None")