# remainder = []

# for i in range(10):
#      n = int(input())
#      m = n % 42
#      if m not in remainder:
#         remainder.append(m)
     
# print(len(remainder))

# 중복없이이 개수를 세려면 set!!
remainder= set()

for i in range(10):
     n = int(input())
     m = n % 42
     remainder.add(m)
     
print(len(remainder))


# len도 표시할 수 있군..