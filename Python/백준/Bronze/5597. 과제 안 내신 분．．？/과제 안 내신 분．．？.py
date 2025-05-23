students = []
for i in range(1,31):
    students.append(i)
    

numbers = []

for i in range(1,29):
    n = int(input())
    numbers.append(n)
    
missing = []

for s in students:
    if s not in numbers:
        missing.append(s)
        
missing.sort
for m in missing:
    print(m)
    

   
